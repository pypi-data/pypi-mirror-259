# encoding: utf-8
"""
RabbitMQ Input
-----------------

Uses a `RabbitMQ Queue <https://www.rabbitmq.com/>`_ as a source for file objects.
At the moment, this expects a CEDA specifc message format.
TODO: Make the callback more flexible (open to collaboration)

**Plugin name:** ``rabbitmq``

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - ``connection.host``
      - string
      - ``REQUIRED`` RabbitMQ server host
    * - ``connection.user``
      - string
      - ``REQUIRED`` Username
    * - ``connection.password``
      - string
      - ``REQUIRED`` password
    * - ``connection.vhost``
      - string
      - ``REQUIRED`` `Virtual host <https://www.rabbitmq.com/vhosts.html>`_
    * - ``connection.kwargs``
      - dict
      - connection parameter kwargs `pika.conneciton.ConnectionParameters
        <https://pika.readthedocs.io/en/stable/modules/parameters.html#connectionparameters>`_
    * - ``exchange.source_exchange``
      - dict
      - Dictionary describing the source exchange. `exchange`_
    * - ``exchange.dest_exchange``
      - dict
      - ``REQUIRED`` The final exchange. This is where the queues will be bound. `exchange`_
    * - ``queues``
      - ``list``
      - ``REQUIRED`` Queue parameters. `queues`_


exchange
^^^^^^^^

The source and dest exchange keys comprise:

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - method
      - string
      - ``REQUIRED`` Exchange name
    * - type
      - string
      - ``REQUIRED`` `Exchange type <https://medium.com/trendyol-tech/rabbitmq-exchange-types-d7e1f51ec825>`_

queues
^^^^^^

List of queue objects. Each queue object comprises:

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - method
      - string
      - ``REQUIRED`` Queue name
    * - kwargs
      - dict
      - kwargs passed to `pika.channel.queue_declare <https://pika.readthedocs.io/en/stable/modules/channel.html#pika.channel.Channel.queue_declare>`_
    * - bind_kwargs
      - dict
      - kwargs passed to `pika.channel.queue_bind <https://pika.readthedocs.io/en/stable/modules/channel.html#pika.channel.Channel.queue_bind>`_
    * - consume_kwargs
      - dict
      - kwargs passed to `pika.channel.Channel.basic_consume <https://pika.readthedocs.io/en/stable/modules/channel.html#pika.channel.Channel.basic_consume>`_

Example Configuration:

    .. code-block:: yaml

        inputs:
            - method: rabbitmq
              connection:
                host: my-rabbit-server.co.uk
                user: user
                password: '*********'
                vhost: my_virtual_host
                kwargs:
                    heartbeat: 300
              exchange:
                source_exchange:
                    name: mysource-exchange
                    type: fanout
                destination_exchange:
                    name: mydest-exchange
                    type: fanout
              queues:
                - method:
                  kwargs:
                    durable: true
                  bind_kwargs:
                    routing_key: my.routing.key
                  consume_kwargs:
                    auto_ack: false


"""
__author__ = "Richard Smith"
__date__ = "29 Sep 2021"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "richard.d.smith@stfc.ac.uk"

# Python imports
import ast
import functools
import json
import logging
from collections import namedtuple

# Third-party imports
import pika

from stac_generator.core.generator import BaseGenerator
from stac_generator.core.input import BaseInput

LOGGER = logging.getLogger(__name__)

IngestMessage = namedtuple(
    "IngestMessage", ["datetime", "filepath", "action", "filesize", "message"]
)


class RabbitMQInput(BaseInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connection_conf = kwargs.get("connection", {})
        self.exchange_conf = kwargs.get("exchange", {})
        self.queues_conf = kwargs.get("queues", [])

    @staticmethod
    def decode_message(body: bytes) -> IngestMessage:
        """
        Takes the message and turns into a dictionary.
        String message format when split on :
            date_hour = split_line[0]
            min = split_line[1]
            sec = split_line[2]
            path = split_line[3]
            action = split_line[4]
            filesize = split_line[5]
            message = ":".join(split_line[6:])

        :param body: Message body, either a json string or text
        :return: IngestMessage
            {
                'datetime': ':'.join(split_line[:3]),
                'uri': split_line[3],
                'action': split_line[4],
                'filesize': split_line[5],
                'message': ':'.join(split_line[6:])
            }

        """

        # Decode the byte string to utf-8
        body = body.decode("utf-8")

        LOGGER.info("RabbitMQ message recieved: %s", body)

        try:
            msg = json.loads(body)

        except json.JSONDecodeError:
            try:
                msg = ast.literal_eval(body)

            except (ValueError, SyntaxError):
                # Assume the message is in the old format and split on :
                split_line = body.strip().split(":")

                msg = {
                    "datetime": ":".join(split_line[:3]),
                    "uri": split_line[3],
                    "action": split_line[4],
                    "filesize": split_line[5],
                    "message": ":".join(split_line[6:]),
                }

        if "uri" not in msg:
            msg["uri"] = msg["filepath"]

        return msg

    def _connect(self, generator) -> pika.channel.Channel:
        """
        Start Pika connection to server. This is run in each thread.

        :return: pika channel
        """

        # Get the username and password for rabbit
        rabbit_user = self.connection_conf.get("user")
        rabbit_password = self.connection_conf.get("password")

        # Get the server variables
        rabbit_server = self.connection_conf.get("host")
        rabbit_vhost = self.connection_conf.get("vhost")

        # Create the credentials object
        credentials = pika.PlainCredentials(rabbit_user, rabbit_password)

        # Start the rabbitMQ connection
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=rabbit_server,
                credentials=credentials,
                virtual_host=rabbit_vhost,
                **self.connection_conf.get("kwargs", {}),
            )
        )

        # Create a new channel
        channel = connection.channel()

        channel.exchange_declare(
            exchange=self.exchange_conf.get("name", "stac"),
            exchange_type=self.exchange_conf.get("type", "topic"),
            **self.exchange_conf.get("kwargs", {}),
        )
        channel.basic_qos(prefetch_count=1)

        # Declare queue and bind queue to the dest exchange
        for queue in self.queues_conf:
            declare_kwargs = queue.get("kwargs", {})
            bind_kwargs = queue.get("bind_kwargs", {})
            consume_kwargs = queue.get("consume_kwargs", {})

            channel.queue_declare(queue=queue["name"], **declare_kwargs)
            channel.queue_bind(
                exchange=self.exchange_conf["name"], queue=queue["name"], **bind_kwargs
            )

            # Set callback
            callback = functools.partial(
                self.callback, connection=connection, generator=generator
            )
            channel.basic_consume(
                queue=queue["name"], on_message_callback=callback, **consume_kwargs
            )

        return channel

    @staticmethod
    def _acknowledge_message(channel: pika.channel.Channel, delivery_tag: str):
        """
        Acknowledge message

        :param channel: Channel which message came from
        :param delivery_tag: Message id
        """

        LOGGER.debug("Acknowledging message: %s", delivery_tag)
        if channel.is_open:
            channel.basic_ack(delivery_tag)

    def acknowledge_message(
        self,
        channel: pika.channel.Channel,
        delivery_tag: str,
        connection: pika.connection.Connection,
    ):
        """
        Acknowledge message and move onto the next. All of the required
        params come from the message callback params.

        :param channel: callback channel param
        :param delivery_tag: from the callback method param. eg. method.delivery_tag
        :param connection: connection object from the callback param
        """
        cb = functools.partial(self._acknowledge_message, channel, delivery_tag)
        connection.add_callback_threadsafe(cb)

    def callback(
        self,
        ch: pika.channel.Channel,
        method: pika.frame.Method,
        properties: pika.frame.Header,
        body: bytes,
        connection: pika.connection.Connection,
        generator: BaseGenerator,
    ) -> None:

        # Get message
        try:
            message = self.decode_message(body)

        except IndexError:
            # Acknowledge message if the message is not compliant
            self.acknowledge_message(ch, method.delivery_tag, connection)
            return

        # Extract uri
        uri = message.pop("uri")

        if self.should_process(uri):
            LOGGER.info("Input processing: %s message: %s", uri, message)

            self.acknowledge_message(ch, method.delivery_tag, connection)
            generator.process(uri, **message)

        else:
            LOGGER.info("Input skipping: %s", uri)

    def run(self, generator: BaseGenerator):

        while True:
            channel = self._connect(generator)

            try:
                LOGGER.info("READY")
                channel.start_consuming()

            except KeyboardInterrupt:
                channel.stop_consuming()
                break

            except pika.exceptions.StreamLostError as e:
                # Log problem
                LOGGER.error("Connection lost, reconnecting", exc_info=e)
                continue

            except Exception as e:
                LOGGER.critical(e, exc_info=True)

                channel.stop_consuming()
                break

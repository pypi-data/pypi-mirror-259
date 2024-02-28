# encoding: utf-8
"""
Object Store Input
------------------

Takes an endpoint url and optionally a bucket prefix and delimiter and will
scan the items at these points in the object store, submitting each to the
asset generator

**Plugin name:** ``object_store``

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - ``session_kwargs``
      - ``dict``
      - ``REQUIRED`` Dictionary containing the S3 access and secret keys
    * - ``endpoint_url``
      - ``string``
      - ``REQUIRED`` URL for S3 endpoint
    * - ``bucket``
      - ``string``
      - Bucket to be scanned. If ``None`` all buckets in endpoint will be scanned.
    * - ``prefix``
      - ``string``
      - Only items with prefix will be scanned
    * - ``delimiter``
      - ``string``
      - Group items after delimiter into one object

Example Configuration:
    .. code-block:: yaml

        inputs:
            - method: object_store
                endpoint_url: https://cedadev-o.s3-ext.jc.rl.ac.uk
                session_kwargs: {
                    aws_access_key_id: ACCESS_KEY,
                    aws_secret_access_key: SECRET_KEY
                }
                bucket: my_bucket
                prefix: directory_or_file
                delimiter: .zarr/

"""
__author__ = "Rhys Evans"
__date__ = "02 Jun 2021"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "rhys.r.evans@stfc.ac.uk"


import logging

import boto3

from stac_generator.core.generator import BaseGenerator
from stac_generator.core.input import BaseInput

LOGGER = logging.getLogger(__name__)


class ObjectStoreInput(BaseInput):
    """ """

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.endpoint_url = kwargs.get("endpoint_url")
        session = boto3.session.Session(**kwargs["session_kwargs"])

        s3 = session.resource(
            "s3",
            endpoint_url=self.endpoint_url,
        )

        self.client = s3.meta.client
        self.buckets = (
            [s3.Bucket(kwargs["bucket"])] if "bucket" in kwargs else s3.buckets.all()
        )

        self.prefix = kwargs.get("prefix", "")
        self.delimiter = kwargs.get("delimiter", "")

    def run(self, generator: BaseGenerator):

        for bucket in self.buckets:
            total_files = 0

            for obj in bucket.objects.filter(
                Prefix=self.prefix, Delimiter=self.delimiter
            ):

                generator.process(
                    f"{self.endpoint_url}/{bucket.name}/{obj.key}",
                    client=self.client,
                )
                total_files += 1

            LOGGER.info(f"Processed {total_files} files from {bucket}")

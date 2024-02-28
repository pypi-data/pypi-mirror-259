# encoding: utf-8
"""
Elasticsearch
-------------

An output backend which outputs the content generated to elasticsearch
using the Elasticsearch API

**Plugin name:** ``elasticsearch_bulk``

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - ``connection_kwargs``
      - ``dict``
      - ``REQUIRED`` Connection kwargs passed to the `elasticsearch client  <https://elasticsearch-py.readthedocs.io/en/latest/api.html#elasticsearch>`_
    * - ``index.name``
      - ``str``
      - ``REQUIRED`` The index to output the content.
    * - ``index.mapping``
      - ``str``
      - Path to a yaml file which defines the mapping for the index

Example Configuration:
    .. code-block:: yaml

        outputs:
            - method: elasticsearch_bulk
              connection_kwargs:
                hosts: ['host1','host2']
              index:
                name: 'assets-2021-06-02'
"""
__author__ = "Richard Smith"
__date__ = "01 Jun 2021"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "richard.d.smith@stfc.ac.uk"

import logging
from typing import Dict

from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

from stac_generator.core.bulk_output import BaseBulkOutput
from stac_generator.core.utils import Coordinates, load_yaml

LOGGER = logging.getLogger(__name__)


class ElasticsearchBulkOutput(BaseBulkOutput):
    """
    Connects to an elasticsearch instance and exports the
    documents to elasticsearch.

    """

    CLEAN_METHODS = ["_format_bbox", "_format_temporal_extent"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        index_conf = kwargs["index"]

        self.es = Elasticsearch(**kwargs["connection_kwargs"])
        self.index_name = index_conf["name"]

        # Create the index, if it doesn't already exist
        if index_conf.get("mapping"):
            if not self.es.indices.exists(self.index_name):
                mapping = load_yaml(index_conf.get("mapping"))
                self.es.indices.create(self.index_name, body=mapping)

    @staticmethod
    def _format_bbox(data: Dict) -> Dict:
        """
        Convert WGS84 coordinates into GeoJSON and
        format for Elasticsearch. Replaces the bbox key.

        :param data: Input data dictionary
        """
        body = data["body"]

        if body.get("bbox"):
            bbox = body.pop("bbox")

            body["spatial"] = {
                "bbox": {
                    "type": "envelope",
                    "coordinates": Coordinates.from_wgs84(bbox).to_geojson(),
                }
            }

        return data

    @staticmethod
    def _format_temporal_extent(data: Dict) -> Dict:
        """
        Convert `extent object<https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md#extent-object>_` for Elasticsearch.

        :param data: Input data dictionary
        """
        body = data["body"]

        if body.get("extent", {}).get("temporal"):
            temporal_extent = body["extent"].pop("temporal")

            if temporal_extent[0][0]:
                body["extent"]["temporal"] = {"gte": temporal_extent[0][0]}
            if temporal_extent[0][1]:
                temporal = body["extent"].get("temporal", {})
                temporal["lte"] = temporal_extent[0][1]
                body["extent"]["temporal"] = temporal

        return data

    def clean(self, data: Dict) -> Dict:
        """
        Condition the input dictionary for elasticsearch
        :param data: Input dictionary
        :returns: Dictionary produced as a result of the clean methods
        """

        for method in self.CLEAN_METHODS:
            m = getattr(self, method)
            data = m(data)

        return data

    def action_iterator(self, data_list: list) -> dict:
        """
        Generate an iterator of elasticsearch actions.

        :param data_list: List of output data

        :returns: elasticsearch action
        """
        for data in data_list:
            data = self.clean(data)

            yield {
                "_op_type": "update",
                "_index": self.index_name,
                "_id": data["id"],
                "doc": data["body"],
                "doc_as_upsert": True,
            }

    def export(self, data_list: list) -> None:
        """
        Export using elasticsearch bulk helper.
        """
        for okay, info in streaming_bulk(
            self.es, self.action_iterator(data_list), yield_ok=False
        ):
            if not okay:
                LOGGER.error(
                    "Unable to index %s: %s",
                    info["update"]["_id"],
                    info["update"]["error"],
                )

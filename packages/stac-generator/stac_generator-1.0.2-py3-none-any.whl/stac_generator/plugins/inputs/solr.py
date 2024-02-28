"""
Solr Input
----------

Uses a Solr index node for a source for file
objects.

**Plugin name:** ``solr``

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - ``index_node``
      - string
      - ``REQUIRED`` Solr index
    * - ``search_params``
      - dict
      - request params to send to Solr


Example Configuration:
    .. code-block:: yaml

        inputs:
            - method: solr
              index_node: url.index-node.ac.uk
              search_params:
                q: "facet: value"
                rows: 10000
"""
__author__ = "Mahir Rahman"
__date__ = "23 Mar 2022"
__copyright__ = "Copyright 2022 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "kazi.mahir@stfc.ac.uk"

import logging
import sys

import requests

from stac_generator.core.generator import BaseGenerator
from stac_generator.core.input import BaseInput

LOGGER = logging.getLogger(__name__)


class SolrInput(BaseInput):

    DEFAULT_ROWS = 10000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index_node = kwargs.get("index_node")
        self.core = kwargs.get("core", "files")
        self.url = f"http://{self.index_node}/solr/{self.core}/select"

        search_params = kwargs.get("search_params", {})
        self.params = {
            "indent": search_params.get("indent", "on"),
            "q": search_params.get("q", "*:*"),
            "wt": search_params.get("wt", "json"),
            "rows": search_params.get("rows", self.DEFAULT_ROWS),
            "sort": search_params.get("sort", "id asc"),
            "cursorMark": "*",
        }

    def iter_docs(self):
        """
        Core loop to iterate through the Solr response.
        """
        n = 0
        while True:
            try:
                resp = requests.get(self.url, self.params)
            except requests.exceptions.ConnectionError as e:
                LOGGER.error(f"Failed to establish connection to {self.url}:\n" f"{e}")
                sys.exit(1)

            resp = resp.json()
            docs = resp["response"]["docs"]

            # Return the list of files to the for loop and continue paginating
            yield from docs

            n += len(docs)
            LOGGER.info(f"{n}/{resp['response']['numFound']}\n")
            if not docs:
                LOGGER.error("no docs found")
                break
            LOGGER.info(f"Next cursormark at position {n}")

            # Change the search params to get next page.
            self.params["cursorMark"] = resp["nextCursorMark"]

    def run(self, generator: BaseGenerator):
        for doc in self.iter_docs():
            uri: str = doc.get("id")

            LOGGER.info(f"Input processing: {uri}")

            # transform id to a uri
            # by replacing '.' with '/' up until the filename
            uri = uri.replace(".", "/", uri.split("|")[0].count(".") - 1)

            generator.process(uri)

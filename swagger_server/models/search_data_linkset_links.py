# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SearchDataLinksetLinks(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link_text: str=None, link_url: str=None):  # noqa: E501
        """SearchDataLinksetLinks - a model defined in Swagger

        :param link_text: The link_text of this SearchDataLinksetLinks.  # noqa: E501
        :type link_text: str
        :param link_url: The link_url of this SearchDataLinksetLinks.  # noqa: E501
        :type link_url: str
        """
        self.swagger_types = {
            'link_text': str,
            'link_url': str
        }

        self.attribute_map = {
            'link_text': 'link_text',
            'link_url': 'link_url'
        }
        self._link_text = link_text
        self._link_url = link_url

    @classmethod
    def from_dict(cls, dikt) -> 'SearchDataLinksetLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The search_data_linkset_links of this SearchDataLinksetLinks.  # noqa: E501
        :rtype: SearchDataLinksetLinks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link_text(self) -> str:
        """Gets the link_text of this SearchDataLinksetLinks.

        Text for the link  # noqa: E501

        :return: The link_text of this SearchDataLinksetLinks.
        :rtype: str
        """
        return self._link_text

    @link_text.setter
    def link_text(self, link_text: str):
        """Sets the link_text of this SearchDataLinksetLinks.

        Text for the link  # noqa: E501

        :param link_text: The link_text of this SearchDataLinksetLinks.
        :type link_text: str
        """

        self._link_text = link_text

    @property
    def link_url(self) -> str:
        """Gets the link_url of this SearchDataLinksetLinks.

        URL for the link  # noqa: E501

        :return: The link_url of this SearchDataLinksetLinks.
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url: str):
        """Sets the link_url of this SearchDataLinksetLinks.

        URL for the link  # noqa: E501

        :param link_url: The link_url of this SearchDataLinksetLinks.
        :type link_url: str
        """

        self._link_url = link_url
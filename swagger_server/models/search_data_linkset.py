# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.search_data_linkset_links import SearchDataLinksetLinks  # noqa: F401,E501
from swagger_server import util


class SearchDataLinkset(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, linkset_title: str=None, linkset_description: str=None, links: List[SearchDataLinksetLinks]=None):  # noqa: E501
        """SearchDataLinkset - a model defined in Swagger

        :param linkset_title: The linkset_title of this SearchDataLinkset.  # noqa: E501
        :type linkset_title: str
        :param linkset_description: The linkset_description of this SearchDataLinkset.  # noqa: E501
        :type linkset_description: str
        :param links: The links of this SearchDataLinkset.  # noqa: E501
        :type links: List[SearchDataLinksetLinks]
        """
        self.swagger_types = {
            'linkset_title': str,
            'linkset_description': str,
            'links': List[SearchDataLinksetLinks]
        }

        self.attribute_map = {
            'linkset_title': 'linkset_title',
            'linkset_description': 'linkset_description',
            'links': 'links'
        }
        self._linkset_title = linkset_title
        self._linkset_description = linkset_description
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'SearchDataLinkset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The search_data_linkset of this SearchDataLinkset.  # noqa: E501
        :rtype: SearchDataLinkset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def linkset_title(self) -> str:
        """Gets the linkset_title of this SearchDataLinkset.

        User friendly title for a link set  # noqa: E501

        :return: The linkset_title of this SearchDataLinkset.
        :rtype: str
        """
        return self._linkset_title

    @linkset_title.setter
    def linkset_title(self, linkset_title: str):
        """Sets the linkset_title of this SearchDataLinkset.

        User friendly title for a link set  # noqa: E501

        :param linkset_title: The linkset_title of this SearchDataLinkset.
        :type linkset_title: str
        """

        self._linkset_title = linkset_title

    @property
    def linkset_description(self) -> str:
        """Gets the linkset_description of this SearchDataLinkset.

        Text description of a link set  # noqa: E501

        :return: The linkset_description of this SearchDataLinkset.
        :rtype: str
        """
        return self._linkset_description

    @linkset_description.setter
    def linkset_description(self, linkset_description: str):
        """Sets the linkset_description of this SearchDataLinkset.

        Text description of a link set  # noqa: E501

        :param linkset_description: The linkset_description of this SearchDataLinkset.
        :type linkset_description: str
        """

        self._linkset_description = linkset_description

    @property
    def links(self) -> List[SearchDataLinksetLinks]:
        """Gets the links of this SearchDataLinkset.


        :return: The links of this SearchDataLinkset.
        :rtype: List[SearchDataLinksetLinks]
        """
        return self._links

    @links.setter
    def links(self, links: List[SearchDataLinksetLinks]):
        """Sets the links of this SearchDataLinkset.


        :param links: The links of this SearchDataLinkset.
        :type links: List[SearchDataLinksetLinks]
        """

        self._links = links
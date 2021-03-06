# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IndexSearchAttributes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, attrib_name: str = None, attrib_type: str = None, attrib_path: str = None,
                 attrib_example: str = None, info: str = None, shortcut_text: str = None):  # noqa: E501
        """IndexSearchAttributes - a model defined in Swagger

        :param attrib_name: The attrib_name of this IndexSearchAttributes.  # noqa: E501
        :type attrib_name: str
        :param attrib_type: The attrib_type of this IndexSearchAttributes.  # noqa: E501
        :type attrib_type: str
        :param attrib_path: The attrib_path of this IndexSearchAttributes.  # noqa: E501
        :type attrib_path: str
        :param attrib_example: The attrib_example of this IndexSearchAttributes.  # noqa: E501
        :type attrib_example: str
        :param info: The info of this IndexSearchAttributes.  # noqa: E501
        :type info: str
        :param shortcut_text: The shortcut_text of this IndexSearchAttributes.  # noqa: E501
        :type shortcut_text: str
        """
        self.swagger_types = {
            'attrib_name': str,
            'attrib_type': str,
            'attrib_path': str,
            'attrib_example': str,
            'info': str,
            'shortcut_text': str
        }

        self.attribute_map = {
            'attrib_name': 'attrib_name',
            'attrib_type': 'attrib_type',
            'attrib_path': 'attrib_path',
            'attrib_example': 'attrib_example',
            'info': 'info',
            'shortcut_text': 'shortcut_text'
        }
        self._attrib_name = attrib_name
        self._attrib_type = attrib_type
        self._attrib_path = attrib_path
        self._attrib_example = attrib_example
        self._info = info
        self._shortcut_text = shortcut_text

    @classmethod
    def from_dict(cls, dikt) -> 'IndexSearchAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The index-search-attributes of this IndexSearchAttributes.  # noqa: E501
        :rtype: IndexSearchAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attrib_name(self) -> str:
        """Gets the attrib_name of this IndexSearchAttributes.

        attribute name as defined in the base search schema  # noqa: E501

        :return: The attrib_name of this IndexSearchAttributes.
        :rtype: str
        """
        return self._attrib_name

    @attrib_name.setter
    def attrib_name(self, attrib_name: str):
        """Sets the attrib_name of this IndexSearchAttributes.

        attribute name as defined in the base search schema  # noqa: E501

        :param attrib_name: The attrib_name of this IndexSearchAttributes.
        :type attrib_name: str
        """

        self._attrib_name = attrib_name

    @property
    def attrib_type(self) -> str:
        """Gets the attrib_type of this IndexSearchAttributes.

        cue for the type of search attribute in the underlying schema  # noqa: E501

        :return: The attrib_type of this IndexSearchAttributes.
        :rtype: str
        """
        return self._attrib_type

    @attrib_type.setter
    def attrib_type(self, attrib_type: str):
        """Sets the attrib_type of this IndexSearchAttributes.

        cue for the type of search attribute in the underlying schema  # noqa: E501

        :param attrib_type: The attrib_type of this IndexSearchAttributes.
        :type attrib_type: str
        """
        allowed_values = ["date", "string", "int", "float", "boolean"]  # noqa: E501
        if attrib_type not in allowed_values:
            raise ValueError(
                "Invalid value for `attrib_type` ({0}), must be one of {1}"
                    .format(attrib_type, allowed_values)
            )

        self._attrib_type = attrib_type

    @property
    def attrib_path(self) -> str:
        """Gets the attrib_path of this IndexSearchAttributes.

        Absolute path of the search attribute in nested elastic search indexed document  # noqa: E501

        :return: The attrib_path of this IndexSearchAttributes.
        :rtype: str
        """
        return self._attrib_path

    @attrib_path.setter
    def attrib_path(self, attrib_path: str):
        """Sets the attrib_path of this IndexSearchAttributes.

        Absolute path of the search attribute in nested elastic search indexed document  # noqa: E501

        :param attrib_path: The attrib_path of this IndexSearchAttributes.
        :type attrib_path: str
        """

        self._attrib_path = attrib_path

    @property
    def attrib_example(self) -> str:
        """Gets the attrib_example of this IndexSearchAttributes.

        example for search attribute  # noqa: E501

        :return: The attrib_example of this IndexSearchAttributes.
        :rtype: str
        """
        return self._attrib_example

    @attrib_example.setter
    def attrib_example(self, attrib_example: str):
        """Sets the attrib_example of this IndexSearchAttributes.

        example for search attribute  # noqa: E501

        :param attrib_example: The attrib_example of this IndexSearchAttributes.
        :type attrib_example: str
        """

        self._attrib_example = attrib_example

    @property
    def info(self) -> str:
        """Gets the info of this IndexSearchAttributes.

        Documentation about the use of the given search type  # noqa: E501

        :return: The info of this IndexSearchAttributes.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info: str):
        """Sets the info of this IndexSearchAttributes.

        Documentation about the use of the given search type  # noqa: E501

        :param info: The info of this IndexSearchAttributes.
        :type info: str
        """

        self._info = info

    @property
    def shortcut_text(self) -> str:
        """Gets the shortcut_text of this IndexSearchAttributes.

        Text shortcut suitable for use in free text advanced search operations, such that Author:XXXX would cause a specific search on the author information in the target index, if not specified it defaults to the attrib_name  # noqa: E501

        :return: The shortcut_text of this IndexSearchAttributes.
        :rtype: str
        """
        return self._shortcut_text

    @shortcut_text.setter
    def shortcut_text(self, shortcut_text: str):
        """Sets the shortcut_text of this IndexSearchAttributes.

        Text shortcut suitable for use in free text advanced search operations, such that Author:XXXX would cause a specific search on the author information in the target index, if not specified it defaults to the attrib_name  # noqa: E501

        :param shortcut_text: The shortcut_text of this IndexSearchAttributes.
        :type shortcut_text: str
        """

        self._shortcut_text = shortcut_text

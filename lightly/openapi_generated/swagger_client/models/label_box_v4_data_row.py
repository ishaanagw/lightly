# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class LabelBoxV4DataRow(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'row_data': 'RedirectedReadUrl',
        'global_key': 'str',
        'media_type': 'str'
    }

    attribute_map = {
        'row_data': 'row_data',
        'global_key': 'global_key',
        'media_type': 'media_type'
    }

    def __init__(self, row_data=None, global_key=None, media_type=None, _configuration=None):  # noqa: E501
        """LabelBoxV4DataRow - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._row_data = None
        self._global_key = None
        self._media_type = None
        self.discriminator = None

        self.row_data = row_data
        if global_key is not None:
            self.global_key = global_key
        if media_type is not None:
            self.media_type = media_type

    @property
    def row_data(self):
        """Gets the row_data of this LabelBoxV4DataRow.  # noqa: E501


        :return: The row_data of this LabelBoxV4DataRow.  # noqa: E501
        :rtype: RedirectedReadUrl
        """
        return self._row_data

    @row_data.setter
    def row_data(self, row_data):
        """Sets the row_data of this LabelBoxV4DataRow.


        :param row_data: The row_data of this LabelBoxV4DataRow.  # noqa: E501
        :type: RedirectedReadUrl
        """
        if self._configuration.client_side_validation and row_data is None:
            raise ValueError("Invalid value for `row_data`, must not be `None`")  # noqa: E501

        self._row_data = row_data

    @property
    def global_key(self):
        """Gets the global_key of this LabelBoxV4DataRow.  # noqa: E501

        The task_id for importing into LabelBox.  # noqa: E501

        :return: The global_key of this LabelBoxV4DataRow.  # noqa: E501
        :rtype: str
        """
        return self._global_key

    @global_key.setter
    def global_key(self, global_key):
        """Sets the global_key of this LabelBoxV4DataRow.

        The task_id for importing into LabelBox.  # noqa: E501

        :param global_key: The global_key of this LabelBoxV4DataRow.  # noqa: E501
        :type: str
        """

        self._global_key = global_key

    @property
    def media_type(self):
        """Gets the media_type of this LabelBoxV4DataRow.  # noqa: E501

        LabelBox media type, e.g. IMAGE  # noqa: E501

        :return: The media_type of this LabelBoxV4DataRow.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this LabelBoxV4DataRow.

        LabelBox media type, e.g. IMAGE  # noqa: E501

        :param media_type: The media_type of this LabelBoxV4DataRow.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LabelBoxV4DataRow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LabelBoxV4DataRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LabelBoxV4DataRow):
            return True

        return self.to_dict() != other.to_dict()

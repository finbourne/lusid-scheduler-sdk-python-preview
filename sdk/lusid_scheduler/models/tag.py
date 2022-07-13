# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.581
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_scheduler.configuration import Configuration


class Tag(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'name': 'str',
        'pull_time': 'datetime',
        'push_time': 'datetime',
        'signed': 'bool',
        'immutable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'pull_time': 'pullTime',
        'push_time': 'pushTime',
        'signed': 'signed',
        'immutable': 'immutable'
    }

    required_map = {
        'name': 'optional',
        'pull_time': 'optional',
        'push_time': 'optional',
        'signed': 'optional',
        'immutable': 'optional'
    }

    def __init__(self, name=None, pull_time=None, push_time=None, signed=None, immutable=None, local_vars_configuration=None):  # noqa: E501
        """Tag - a model defined in OpenAPI"
        
        :param name:  The name of the tag
        :type name: str
        :param pull_time:  The latest pull time
        :type pull_time: datetime
        :param push_time:  The date of the tag's push
        :type push_time: datetime
        :param signed:  Indicates whether the tag is signed
        :type signed: bool
        :param immutable:  Indicates whether the tag is immutable
        :type immutable: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._pull_time = None
        self._push_time = None
        self._signed = None
        self._immutable = None
        self.discriminator = None

        self.name = name
        if pull_time is not None:
            self.pull_time = pull_time
        if push_time is not None:
            self.push_time = push_time
        if signed is not None:
            self.signed = signed
        if immutable is not None:
            self.immutable = immutable

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501

        The name of the tag  # noqa: E501

        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        The name of the tag  # noqa: E501

        :param name: The name of this Tag.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def pull_time(self):
        """Gets the pull_time of this Tag.  # noqa: E501

        The latest pull time  # noqa: E501

        :return: The pull_time of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._pull_time

    @pull_time.setter
    def pull_time(self, pull_time):
        """Sets the pull_time of this Tag.

        The latest pull time  # noqa: E501

        :param pull_time: The pull_time of this Tag.  # noqa: E501
        :type pull_time: datetime
        """

        self._pull_time = pull_time

    @property
    def push_time(self):
        """Gets the push_time of this Tag.  # noqa: E501

        The date of the tag's push  # noqa: E501

        :return: The push_time of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._push_time

    @push_time.setter
    def push_time(self, push_time):
        """Sets the push_time of this Tag.

        The date of the tag's push  # noqa: E501

        :param push_time: The push_time of this Tag.  # noqa: E501
        :type push_time: datetime
        """

        self._push_time = push_time

    @property
    def signed(self):
        """Gets the signed of this Tag.  # noqa: E501

        Indicates whether the tag is signed  # noqa: E501

        :return: The signed of this Tag.  # noqa: E501
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """Sets the signed of this Tag.

        Indicates whether the tag is signed  # noqa: E501

        :param signed: The signed of this Tag.  # noqa: E501
        :type signed: bool
        """

        self._signed = signed

    @property
    def immutable(self):
        """Gets the immutable of this Tag.  # noqa: E501

        Indicates whether the tag is immutable  # noqa: E501

        :return: The immutable of this Tag.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this Tag.

        Indicates whether the tag is immutable  # noqa: E501

        :param immutable: The immutable of this Tag.  # noqa: E501
        :type immutable: bool
        """

        self._immutable = immutable

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Tag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tag):
            return True

        return self.to_dict() != other.to_dict()

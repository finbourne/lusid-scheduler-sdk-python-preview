# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.716
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


class Notification(object):
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
        'fire_on': 'str',
        'transport': 'str',
        'destination': 'list[str]'
    }

    attribute_map = {
        'fire_on': 'fireOn',
        'transport': 'transport',
        'destination': 'destination'
    }

    required_map = {
        'fire_on': 'optional',
        'transport': 'optional',
        'destination': 'optional'
    }

    def __init__(self, fire_on=None, transport=None, destination=None, local_vars_configuration=None):  # noqa: E501
        """Notification - a model defined in OpenAPI"
        
        :param fire_on:  Condition for the notification
        :type fire_on: str
        :param transport:  The type of the notification
        :type transport: str
        :param destination:  Where the notification should be sent
        :type destination: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._fire_on = None
        self._transport = None
        self._destination = None
        self.discriminator = None

        self.fire_on = fire_on
        self.transport = transport
        self.destination = destination

    @property
    def fire_on(self):
        """Gets the fire_on of this Notification.  # noqa: E501

        Condition for the notification  # noqa: E501

        :return: The fire_on of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._fire_on

    @fire_on.setter
    def fire_on(self, fire_on):
        """Sets the fire_on of this Notification.

        Condition for the notification  # noqa: E501

        :param fire_on: The fire_on of this Notification.  # noqa: E501
        :type fire_on: str
        """

        self._fire_on = fire_on

    @property
    def transport(self):
        """Gets the transport of this Notification.  # noqa: E501

        The type of the notification  # noqa: E501

        :return: The transport of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this Notification.

        The type of the notification  # noqa: E501

        :param transport: The transport of this Notification.  # noqa: E501
        :type transport: str
        """

        self._transport = transport

    @property
    def destination(self):
        """Gets the destination of this Notification.  # noqa: E501

        Where the notification should be sent  # noqa: E501

        :return: The destination of this Notification.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Notification.

        Where the notification should be sent  # noqa: E501

        :param destination: The destination of this Notification.  # noqa: E501
        :type destination: list[str]
        """

        self._destination = destination

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
        if not isinstance(other, Notification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Notification):
            return True

        return self.to_dict() != other.to_dict()

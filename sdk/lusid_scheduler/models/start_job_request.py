# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.236
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


class StartJobRequest(object):
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
        'arguments': 'dict(str, str)',
        'notifications': 'list[Notification]'
    }

    attribute_map = {
        'arguments': 'arguments',
        'notifications': 'notifications'
    }

    required_map = {
        'arguments': 'optional',
        'notifications': 'optional'
    }

    def __init__(self, arguments=None, notifications=None, local_vars_configuration=None):  # noqa: E501
        """StartJobRequest - a model defined in OpenAPI"
        
        :param arguments:  All arguments needed for the Job to run
        :type arguments: dict(str, str)
        :param notifications:  Notifications for this Job
        :type notifications: list[lusid_scheduler.Notification]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._arguments = None
        self._notifications = None
        self.discriminator = None

        self.arguments = arguments
        self.notifications = notifications

    @property
    def arguments(self):
        """Gets the arguments of this StartJobRequest.  # noqa: E501

        All arguments needed for the Job to run  # noqa: E501

        :return: The arguments of this StartJobRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this StartJobRequest.

        All arguments needed for the Job to run  # noqa: E501

        :param arguments: The arguments of this StartJobRequest.  # noqa: E501
        :type arguments: dict(str, str)
        """

        self._arguments = arguments

    @property
    def notifications(self):
        """Gets the notifications of this StartJobRequest.  # noqa: E501

        Notifications for this Job  # noqa: E501

        :return: The notifications of this StartJobRequest.  # noqa: E501
        :rtype: list[lusid_scheduler.Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this StartJobRequest.

        Notifications for this Job  # noqa: E501

        :param notifications: The notifications of this StartJobRequest.  # noqa: E501
        :type notifications: list[lusid_scheduler.Notification]
        """

        self._notifications = notifications

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
        if not isinstance(other, StartJobRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StartJobRequest):
            return True

        return self.to_dict() != other.to_dict()
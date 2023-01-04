# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.708
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


class Trigger(object):
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
        'time_trigger': 'TimeTrigger'
    }

    attribute_map = {
        'time_trigger': 'timeTrigger'
    }

    required_map = {
        'time_trigger': 'optional'
    }

    def __init__(self, time_trigger=None, local_vars_configuration=None):  # noqa: E501
        """Trigger - a model defined in OpenAPI"
        
        :param time_trigger: 
        :type time_trigger: lusid_scheduler.TimeTrigger

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._time_trigger = None
        self.discriminator = None

        if time_trigger is not None:
            self.time_trigger = time_trigger

    @property
    def time_trigger(self):
        """Gets the time_trigger of this Trigger.  # noqa: E501


        :return: The time_trigger of this Trigger.  # noqa: E501
        :rtype: lusid_scheduler.TimeTrigger
        """
        return self._time_trigger

    @time_trigger.setter
    def time_trigger(self, time_trigger):
        """Sets the time_trigger of this Trigger.


        :param time_trigger: The time_trigger of this Trigger.  # noqa: E501
        :type time_trigger: lusid_scheduler.TimeTrigger
        """

        self._time_trigger = time_trigger

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
        if not isinstance(other, Trigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trigger):
            return True

        return self.to_dict() != other.to_dict()

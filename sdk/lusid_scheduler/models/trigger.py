# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.588
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
        'bucket_watcher_trigger': 'BucketWatcherTrigger',
        'time_trigger': 'TimeTrigger',
        'combined_trigger': 'CombinedTrigger'
    }

    attribute_map = {
        'bucket_watcher_trigger': 'bucketWatcherTrigger',
        'time_trigger': 'timeTrigger',
        'combined_trigger': 'combinedTrigger'
    }

    required_map = {
        'bucket_watcher_trigger': 'optional',
        'time_trigger': 'optional',
        'combined_trigger': 'optional'
    }

    def __init__(self, bucket_watcher_trigger=None, time_trigger=None, combined_trigger=None, local_vars_configuration=None):  # noqa: E501
        """Trigger - a model defined in OpenAPI"
        
        :param bucket_watcher_trigger: 
        :type bucket_watcher_trigger: lusid_scheduler.BucketWatcherTrigger
        :param time_trigger: 
        :type time_trigger: lusid_scheduler.TimeTrigger
        :param combined_trigger: 
        :type combined_trigger: lusid_scheduler.CombinedTrigger

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bucket_watcher_trigger = None
        self._time_trigger = None
        self._combined_trigger = None
        self.discriminator = None

        if bucket_watcher_trigger is not None:
            self.bucket_watcher_trigger = bucket_watcher_trigger
        if time_trigger is not None:
            self.time_trigger = time_trigger
        if combined_trigger is not None:
            self.combined_trigger = combined_trigger

    @property
    def bucket_watcher_trigger(self):
        """Gets the bucket_watcher_trigger of this Trigger.  # noqa: E501


        :return: The bucket_watcher_trigger of this Trigger.  # noqa: E501
        :rtype: lusid_scheduler.BucketWatcherTrigger
        """
        return self._bucket_watcher_trigger

    @bucket_watcher_trigger.setter
    def bucket_watcher_trigger(self, bucket_watcher_trigger):
        """Sets the bucket_watcher_trigger of this Trigger.


        :param bucket_watcher_trigger: The bucket_watcher_trigger of this Trigger.  # noqa: E501
        :type bucket_watcher_trigger: lusid_scheduler.BucketWatcherTrigger
        """

        self._bucket_watcher_trigger = bucket_watcher_trigger

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

    @property
    def combined_trigger(self):
        """Gets the combined_trigger of this Trigger.  # noqa: E501


        :return: The combined_trigger of this Trigger.  # noqa: E501
        :rtype: lusid_scheduler.CombinedTrigger
        """
        return self._combined_trigger

    @combined_trigger.setter
    def combined_trigger(self, combined_trigger):
        """Sets the combined_trigger of this Trigger.


        :param combined_trigger: The combined_trigger of this Trigger.  # noqa: E501
        :type combined_trigger: lusid_scheduler.CombinedTrigger
        """

        self._combined_trigger = combined_trigger

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

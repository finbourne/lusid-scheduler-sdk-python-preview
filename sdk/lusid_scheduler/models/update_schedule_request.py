# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.685
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


class UpdateScheduleRequest(object):
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
        'job_id': 'ResourceId',
        'name': 'str',
        'description': 'str',
        'author': 'str',
        'owner': 'str',
        'arguments': 'dict(str, str)',
        'trigger': 'Trigger',
        'notifications': 'list[Notification]',
        'enabled': 'bool'
    }

    attribute_map = {
        'job_id': 'jobId',
        'name': 'name',
        'description': 'description',
        'author': 'author',
        'owner': 'owner',
        'arguments': 'arguments',
        'trigger': 'trigger',
        'notifications': 'notifications',
        'enabled': 'enabled'
    }

    required_map = {
        'job_id': 'required',
        'name': 'required',
        'description': 'required',
        'author': 'optional',
        'owner': 'optional',
        'arguments': 'optional',
        'trigger': 'optional',
        'notifications': 'required',
        'enabled': 'optional'
    }

    def __init__(self, job_id=None, name=None, description=None, author=None, owner=None, arguments=None, trigger=None, notifications=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """UpdateScheduleRequest - a model defined in OpenAPI"
        
        :param job_id:  (required)
        :type job_id: lusid_scheduler.ResourceId
        :param name:  The updated name of the schedule (required)
        :type name: str
        :param description:  The updated description of the schedule (required)
        :type description: str
        :param author:  The updated author of the schedule
        :type author: str
        :param owner:  The update owner of the schedule
        :type owner: str
        :param arguments:  Updated arguments to be passed to the job  Note: The new arguments will completely replace old arguments
        :type arguments: dict(str, str)
        :param trigger: 
        :type trigger: lusid_scheduler.Trigger
        :param notifications:  Updated notifications for this schedule (required)
        :type notifications: list[lusid_scheduler.Notification]
        :param enabled:  Specify whether schedule is enabled or not  Defaults to true
        :type enabled: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._job_id = None
        self._name = None
        self._description = None
        self._author = None
        self._owner = None
        self._arguments = None
        self._trigger = None
        self._notifications = None
        self._enabled = None
        self.discriminator = None

        self.job_id = job_id
        self.name = name
        self.description = description
        self.author = author
        self.owner = owner
        self.arguments = arguments
        if trigger is not None:
            self.trigger = trigger
        self.notifications = notifications
        if enabled is not None:
            self.enabled = enabled

    @property
    def job_id(self):
        """Gets the job_id of this UpdateScheduleRequest.  # noqa: E501


        :return: The job_id of this UpdateScheduleRequest.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateScheduleRequest.


        :param job_id: The job_id of this UpdateScheduleRequest.  # noqa: E501
        :type job_id: lusid_scheduler.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this UpdateScheduleRequest.  # noqa: E501

        The updated name of the schedule  # noqa: E501

        :return: The name of this UpdateScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateScheduleRequest.

        The updated name of the schedule  # noqa: E501

        :param name: The name of this UpdateScheduleRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 512):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[\s\S]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateScheduleRequest.  # noqa: E501

        The updated description of the schedule  # noqa: E501

        :return: The description of this UpdateScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateScheduleRequest.

        The updated description of the schedule  # noqa: E501

        :param description: The description of this UpdateScheduleRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 512):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def author(self):
        """Gets the author of this UpdateScheduleRequest.  # noqa: E501

        The updated author of the schedule  # noqa: E501

        :return: The author of this UpdateScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this UpdateScheduleRequest.

        The updated author of the schedule  # noqa: E501

        :param author: The author of this UpdateScheduleRequest.  # noqa: E501
        :type author: str
        """
        if (self.local_vars_configuration.client_side_validation and
                author is not None and len(author) > 512):
            raise ValueError("Invalid value for `author`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                author is not None and len(author) < 0):
            raise ValueError("Invalid value for `author`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                author is not None and not re.search(r'^[\s\S]*$', author)):  # noqa: E501
            raise ValueError(r"Invalid value for `author`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._author = author

    @property
    def owner(self):
        """Gets the owner of this UpdateScheduleRequest.  # noqa: E501

        The update owner of the schedule  # noqa: E501

        :return: The owner of this UpdateScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdateScheduleRequest.

        The update owner of the schedule  # noqa: E501

        :param owner: The owner of this UpdateScheduleRequest.  # noqa: E501
        :type owner: str
        """
        if (self.local_vars_configuration.client_side_validation and
                owner is not None and len(owner) > 512):
            raise ValueError("Invalid value for `owner`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                owner is not None and len(owner) < 0):
            raise ValueError("Invalid value for `owner`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                owner is not None and not re.search(r'^[\s\S]*$', owner)):  # noqa: E501
            raise ValueError(r"Invalid value for `owner`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._owner = owner

    @property
    def arguments(self):
        """Gets the arguments of this UpdateScheduleRequest.  # noqa: E501

        Updated arguments to be passed to the job  Note: The new arguments will completely replace old arguments  # noqa: E501

        :return: The arguments of this UpdateScheduleRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this UpdateScheduleRequest.

        Updated arguments to be passed to the job  Note: The new arguments will completely replace old arguments  # noqa: E501

        :param arguments: The arguments of this UpdateScheduleRequest.  # noqa: E501
        :type arguments: dict(str, str)
        """

        self._arguments = arguments

    @property
    def trigger(self):
        """Gets the trigger of this UpdateScheduleRequest.  # noqa: E501


        :return: The trigger of this UpdateScheduleRequest.  # noqa: E501
        :rtype: lusid_scheduler.Trigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this UpdateScheduleRequest.


        :param trigger: The trigger of this UpdateScheduleRequest.  # noqa: E501
        :type trigger: lusid_scheduler.Trigger
        """

        self._trigger = trigger

    @property
    def notifications(self):
        """Gets the notifications of this UpdateScheduleRequest.  # noqa: E501

        Updated notifications for this schedule  # noqa: E501

        :return: The notifications of this UpdateScheduleRequest.  # noqa: E501
        :rtype: list[lusid_scheduler.Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this UpdateScheduleRequest.

        Updated notifications for this schedule  # noqa: E501

        :param notifications: The notifications of this UpdateScheduleRequest.  # noqa: E501
        :type notifications: list[lusid_scheduler.Notification]
        """
        if self.local_vars_configuration.client_side_validation and notifications is None:  # noqa: E501
            raise ValueError("Invalid value for `notifications`, must not be `None`")  # noqa: E501

        self._notifications = notifications

    @property
    def enabled(self):
        """Gets the enabled of this UpdateScheduleRequest.  # noqa: E501

        Specify whether schedule is enabled or not  Defaults to true  # noqa: E501

        :return: The enabled of this UpdateScheduleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateScheduleRequest.

        Specify whether schedule is enabled or not  Defaults to true  # noqa: E501

        :param enabled: The enabled of this UpdateScheduleRequest.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, UpdateScheduleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateScheduleRequest):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.807
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


class ScheduleDefinition(object):
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
        'schedule_identifier': 'ResourceId',
        'job_id': 'ResourceId',
        'name': 'str',
        'description': 'str',
        'author': 'str',
        'owner': 'str',
        'use_as_auth': 'str',
        'arguments': 'dict(str, str)',
        'trigger': 'Trigger',
        'notifications': 'list[Notification]',
        'enabled': 'bool'
    }

    attribute_map = {
        'schedule_identifier': 'scheduleIdentifier',
        'job_id': 'jobId',
        'name': 'name',
        'description': 'description',
        'author': 'author',
        'owner': 'owner',
        'use_as_auth': 'useAsAuth',
        'arguments': 'arguments',
        'trigger': 'trigger',
        'notifications': 'notifications',
        'enabled': 'enabled'
    }

    required_map = {
        'schedule_identifier': 'required',
        'job_id': 'optional',
        'name': 'optional',
        'description': 'optional',
        'author': 'optional',
        'owner': 'optional',
        'use_as_auth': 'optional',
        'arguments': 'optional',
        'trigger': 'optional',
        'notifications': 'optional',
        'enabled': 'optional'
    }

    def __init__(self, schedule_identifier=None, job_id=None, name=None, description=None, author=None, owner=None, use_as_auth=None, arguments=None, trigger=None, notifications=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleDefinition - a model defined in OpenAPI"
        
        :param schedule_identifier:  (required)
        :type schedule_identifier: lusid_scheduler.ResourceId
        :param job_id: 
        :type job_id: lusid_scheduler.ResourceId
        :param name:  A display name for this Schedule
        :type name: str
        :param description:  A description of the Schedule
        :type description: str
        :param author:  Name of the author of this schedule
        :type author: str
        :param owner:  Name of owner of this schedule
        :type owner: str
        :param use_as_auth:  User to runs schedule when automatically run and authenticates   requests in the schedule
        :type use_as_auth: str
        :param arguments:  All arguments specified by this Schedule that will be passed in to the Job
        :type arguments: dict(str, str)
        :param trigger: 
        :type trigger: lusid_scheduler.Trigger
        :param notifications:  Notifications for this Schedule
        :type notifications: list[lusid_scheduler.Notification]
        :param enabled:  The status of this schedule
        :type enabled: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._schedule_identifier = None
        self._job_id = None
        self._name = None
        self._description = None
        self._author = None
        self._owner = None
        self._use_as_auth = None
        self._arguments = None
        self._trigger = None
        self._notifications = None
        self._enabled = None
        self.discriminator = None

        self.schedule_identifier = schedule_identifier
        if job_id is not None:
            self.job_id = job_id
        self.name = name
        self.description = description
        self.author = author
        self.owner = owner
        self.use_as_auth = use_as_auth
        self.arguments = arguments
        if trigger is not None:
            self.trigger = trigger
        self.notifications = notifications
        if enabled is not None:
            self.enabled = enabled

    @property
    def schedule_identifier(self):
        """Gets the schedule_identifier of this ScheduleDefinition.  # noqa: E501


        :return: The schedule_identifier of this ScheduleDefinition.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._schedule_identifier

    @schedule_identifier.setter
    def schedule_identifier(self, schedule_identifier):
        """Sets the schedule_identifier of this ScheduleDefinition.


        :param schedule_identifier: The schedule_identifier of this ScheduleDefinition.  # noqa: E501
        :type schedule_identifier: lusid_scheduler.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and schedule_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule_identifier`, must not be `None`")  # noqa: E501

        self._schedule_identifier = schedule_identifier

    @property
    def job_id(self):
        """Gets the job_id of this ScheduleDefinition.  # noqa: E501


        :return: The job_id of this ScheduleDefinition.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ScheduleDefinition.


        :param job_id: The job_id of this ScheduleDefinition.  # noqa: E501
        :type job_id: lusid_scheduler.ResourceId
        """

        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this ScheduleDefinition.  # noqa: E501

        A display name for this Schedule  # noqa: E501

        :return: The name of this ScheduleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScheduleDefinition.

        A display name for this Schedule  # noqa: E501

        :param name: The name of this ScheduleDefinition.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ScheduleDefinition.  # noqa: E501

        A description of the Schedule  # noqa: E501

        :return: The description of this ScheduleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScheduleDefinition.

        A description of the Schedule  # noqa: E501

        :param description: The description of this ScheduleDefinition.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def author(self):
        """Gets the author of this ScheduleDefinition.  # noqa: E501

        Name of the author of this schedule  # noqa: E501

        :return: The author of this ScheduleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ScheduleDefinition.

        Name of the author of this schedule  # noqa: E501

        :param author: The author of this ScheduleDefinition.  # noqa: E501
        :type author: str
        """

        self._author = author

    @property
    def owner(self):
        """Gets the owner of this ScheduleDefinition.  # noqa: E501

        Name of owner of this schedule  # noqa: E501

        :return: The owner of this ScheduleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ScheduleDefinition.

        Name of owner of this schedule  # noqa: E501

        :param owner: The owner of this ScheduleDefinition.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def use_as_auth(self):
        """Gets the use_as_auth of this ScheduleDefinition.  # noqa: E501

        User to runs schedule when automatically run and authenticates   requests in the schedule  # noqa: E501

        :return: The use_as_auth of this ScheduleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._use_as_auth

    @use_as_auth.setter
    def use_as_auth(self, use_as_auth):
        """Sets the use_as_auth of this ScheduleDefinition.

        User to runs schedule when automatically run and authenticates   requests in the schedule  # noqa: E501

        :param use_as_auth: The use_as_auth of this ScheduleDefinition.  # noqa: E501
        :type use_as_auth: str
        """

        self._use_as_auth = use_as_auth

    @property
    def arguments(self):
        """Gets the arguments of this ScheduleDefinition.  # noqa: E501

        All arguments specified by this Schedule that will be passed in to the Job  # noqa: E501

        :return: The arguments of this ScheduleDefinition.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ScheduleDefinition.

        All arguments specified by this Schedule that will be passed in to the Job  # noqa: E501

        :param arguments: The arguments of this ScheduleDefinition.  # noqa: E501
        :type arguments: dict(str, str)
        """

        self._arguments = arguments

    @property
    def trigger(self):
        """Gets the trigger of this ScheduleDefinition.  # noqa: E501


        :return: The trigger of this ScheduleDefinition.  # noqa: E501
        :rtype: lusid_scheduler.Trigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this ScheduleDefinition.


        :param trigger: The trigger of this ScheduleDefinition.  # noqa: E501
        :type trigger: lusid_scheduler.Trigger
        """

        self._trigger = trigger

    @property
    def notifications(self):
        """Gets the notifications of this ScheduleDefinition.  # noqa: E501

        Notifications for this Schedule  # noqa: E501

        :return: The notifications of this ScheduleDefinition.  # noqa: E501
        :rtype: list[lusid_scheduler.Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this ScheduleDefinition.

        Notifications for this Schedule  # noqa: E501

        :param notifications: The notifications of this ScheduleDefinition.  # noqa: E501
        :type notifications: list[lusid_scheduler.Notification]
        """

        self._notifications = notifications

    @property
    def enabled(self):
        """Gets the enabled of this ScheduleDefinition.  # noqa: E501

        The status of this schedule  # noqa: E501

        :return: The enabled of this ScheduleDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScheduleDefinition.

        The status of this schedule  # noqa: E501

        :param enabled: The enabled of this ScheduleDefinition.  # noqa: E501
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
        if not isinstance(other, ScheduleDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleDefinition):
            return True

        return self.to_dict() != other.to_dict()

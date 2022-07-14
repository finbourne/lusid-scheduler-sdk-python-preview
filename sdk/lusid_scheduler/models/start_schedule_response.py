# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.583
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


class StartScheduleResponse(object):
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
        'schedule_id': 'ResourceId',
        'job_id': 'ResourceId',
        'run_id': 'str',
        'status': 'str',
        'result': 'str'
    }

    attribute_map = {
        'schedule_id': 'scheduleId',
        'job_id': 'jobId',
        'run_id': 'runId',
        'status': 'status',
        'result': 'result'
    }

    required_map = {
        'schedule_id': 'optional',
        'job_id': 'optional',
        'run_id': 'optional',
        'status': 'optional',
        'result': 'optional'
    }

    def __init__(self, schedule_id=None, job_id=None, run_id=None, status=None, result=None, local_vars_configuration=None):  # noqa: E501
        """StartScheduleResponse - a model defined in OpenAPI"
        
        :param schedule_id: 
        :type schedule_id: lusid_scheduler.ResourceId
        :param job_id: 
        :type job_id: lusid_scheduler.ResourceId
        :param run_id:  Unique RunId of the started schedule
        :type run_id: str
        :param status:  Status of the started schedule
        :type status: str
        :param result:  Link to the result of the job run when completed
        :type result: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._schedule_id = None
        self._job_id = None
        self._run_id = None
        self._status = None
        self._result = None
        self.discriminator = None

        if schedule_id is not None:
            self.schedule_id = schedule_id
        if job_id is not None:
            self.job_id = job_id
        self.run_id = run_id
        self.status = status
        self.result = result

    @property
    def schedule_id(self):
        """Gets the schedule_id of this StartScheduleResponse.  # noqa: E501


        :return: The schedule_id of this StartScheduleResponse.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this StartScheduleResponse.


        :param schedule_id: The schedule_id of this StartScheduleResponse.  # noqa: E501
        :type schedule_id: lusid_scheduler.ResourceId
        """

        self._schedule_id = schedule_id

    @property
    def job_id(self):
        """Gets the job_id of this StartScheduleResponse.  # noqa: E501


        :return: The job_id of this StartScheduleResponse.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StartScheduleResponse.


        :param job_id: The job_id of this StartScheduleResponse.  # noqa: E501
        :type job_id: lusid_scheduler.ResourceId
        """

        self._job_id = job_id

    @property
    def run_id(self):
        """Gets the run_id of this StartScheduleResponse.  # noqa: E501

        Unique RunId of the started schedule  # noqa: E501

        :return: The run_id of this StartScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this StartScheduleResponse.

        Unique RunId of the started schedule  # noqa: E501

        :param run_id: The run_id of this StartScheduleResponse.  # noqa: E501
        :type run_id: str
        """

        self._run_id = run_id

    @property
    def status(self):
        """Gets the status of this StartScheduleResponse.  # noqa: E501

        Status of the started schedule  # noqa: E501

        :return: The status of this StartScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StartScheduleResponse.

        Status of the started schedule  # noqa: E501

        :param status: The status of this StartScheduleResponse.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def result(self):
        """Gets the result of this StartScheduleResponse.  # noqa: E501

        Link to the result of the job run when completed  # noqa: E501

        :return: The result of this StartScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StartScheduleResponse.

        Link to the result of the job run when completed  # noqa: E501

        :param result: The result of this StartScheduleResponse.  # noqa: E501
        :type result: str
        """

        self._result = result

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
        if not isinstance(other, StartScheduleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StartScheduleResponse):
            return True

        return self.to_dict() != other.to_dict()

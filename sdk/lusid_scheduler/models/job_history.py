# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.674
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


class JobHistory(object):
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
        'run_id': 'str',
        'job_id': 'ResourceId',
        'name': 'str',
        'initialised_date': 'datetime',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'arguments': 'dict(str, str)',
        'environment_variables': 'dict(str, str)',
        'job_status': 'str',
        'job_result': 'str',
        'description': 'str',
        'schedule_id': 'ResourceId',
        'result_url': 'str',
        'manually_triggered_by': 'str',
        'command': 'str',
        'message': 'str'
    }

    attribute_map = {
        'run_id': 'runId',
        'job_id': 'jobId',
        'name': 'name',
        'initialised_date': 'initialisedDate',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'arguments': 'arguments',
        'environment_variables': 'environmentVariables',
        'job_status': 'jobStatus',
        'job_result': 'jobResult',
        'description': 'description',
        'schedule_id': 'scheduleId',
        'result_url': 'resultUrl',
        'manually_triggered_by': 'manuallyTriggeredBy',
        'command': 'command',
        'message': 'message'
    }

    required_map = {
        'run_id': 'optional',
        'job_id': 'optional',
        'name': 'optional',
        'initialised_date': 'optional',
        'start_date': 'optional',
        'end_date': 'optional',
        'arguments': 'optional',
        'environment_variables': 'optional',
        'job_status': 'optional',
        'job_result': 'optional',
        'description': 'optional',
        'schedule_id': 'optional',
        'result_url': 'optional',
        'manually_triggered_by': 'optional',
        'command': 'optional',
        'message': 'optional'
    }

    def __init__(self, run_id=None, job_id=None, name=None, initialised_date=None, start_date=None, end_date=None, arguments=None, environment_variables=None, job_status=None, job_result=None, description=None, schedule_id=None, result_url=None, manually_triggered_by=None, command=None, message=None, local_vars_configuration=None):  # noqa: E501
        """JobHistory - a model defined in OpenAPI"
        
        :param run_id:  Unique id of the job run
        :type run_id: str
        :param job_id: 
        :type job_id: lusid_scheduler.ResourceId
        :param name:  Name of the job
        :type name: str
        :param initialised_date:  The date when the job was initialised
        :type initialised_date: datetime
        :param start_date:  The date when the job started running in Scheduler
        :type start_date: datetime
        :param end_date:  End date of the job  Defaults to null if the job has not started or not completed yet  If value is null and job has not started, status will be `Pending`  If value is null and job has not completed, but is running, status will be `Running`
        :type end_date: datetime
        :param arguments:  All arguments used in in this job run
        :type arguments: dict(str, str)
        :param environment_variables:  All environment variables used in this job run
        :type environment_variables: dict(str, str)
        :param job_status:  Current job status
        :type job_status: str
        :param job_result:  Description of the job result
        :type job_result: str
        :param description:  Description of the job
        :type description: str
        :param schedule_id: 
        :type schedule_id: lusid_scheduler.ResourceId
        :param result_url:  URI to results. Defaults to null if not available
        :type result_url: str
        :param manually_triggered_by:  UserId of the user that triggered the job.  Defaults to null if job was ran on a Schedule
        :type manually_triggered_by: str
        :param command:  The command used to run the job
        :type command: str
        :param message:  Output message generated by the job runner  Value will be null when the job is in a `Running` or `Pending` status
        :type message: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._job_id = None
        self._name = None
        self._initialised_date = None
        self._start_date = None
        self._end_date = None
        self._arguments = None
        self._environment_variables = None
        self._job_status = None
        self._job_result = None
        self._description = None
        self._schedule_id = None
        self._result_url = None
        self._manually_triggered_by = None
        self._command = None
        self._message = None
        self.discriminator = None

        self.run_id = run_id
        if job_id is not None:
            self.job_id = job_id
        self.name = name
        if initialised_date is not None:
            self.initialised_date = initialised_date
        self.start_date = start_date
        self.end_date = end_date
        self.arguments = arguments
        self.environment_variables = environment_variables
        self.job_status = job_status
        self.job_result = job_result
        self.description = description
        if schedule_id is not None:
            self.schedule_id = schedule_id
        self.result_url = result_url
        self.manually_triggered_by = manually_triggered_by
        self.command = command
        self.message = message

    @property
    def run_id(self):
        """Gets the run_id of this JobHistory.  # noqa: E501

        Unique id of the job run  # noqa: E501

        :return: The run_id of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this JobHistory.

        Unique id of the job run  # noqa: E501

        :param run_id: The run_id of this JobHistory.  # noqa: E501
        :type run_id: str
        """

        self._run_id = run_id

    @property
    def job_id(self):
        """Gets the job_id of this JobHistory.  # noqa: E501


        :return: The job_id of this JobHistory.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobHistory.


        :param job_id: The job_id of this JobHistory.  # noqa: E501
        :type job_id: lusid_scheduler.ResourceId
        """

        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this JobHistory.  # noqa: E501

        Name of the job  # noqa: E501

        :return: The name of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobHistory.

        Name of the job  # noqa: E501

        :param name: The name of this JobHistory.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def initialised_date(self):
        """Gets the initialised_date of this JobHistory.  # noqa: E501

        The date when the job was initialised  # noqa: E501

        :return: The initialised_date of this JobHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._initialised_date

    @initialised_date.setter
    def initialised_date(self, initialised_date):
        """Sets the initialised_date of this JobHistory.

        The date when the job was initialised  # noqa: E501

        :param initialised_date: The initialised_date of this JobHistory.  # noqa: E501
        :type initialised_date: datetime
        """

        self._initialised_date = initialised_date

    @property
    def start_date(self):
        """Gets the start_date of this JobHistory.  # noqa: E501

        The date when the job started running in Scheduler  # noqa: E501

        :return: The start_date of this JobHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this JobHistory.

        The date when the job started running in Scheduler  # noqa: E501

        :param start_date: The start_date of this JobHistory.  # noqa: E501
        :type start_date: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this JobHistory.  # noqa: E501

        End date of the job  Defaults to null if the job has not started or not completed yet  If value is null and job has not started, status will be `Pending`  If value is null and job has not completed, but is running, status will be `Running`  # noqa: E501

        :return: The end_date of this JobHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this JobHistory.

        End date of the job  Defaults to null if the job has not started or not completed yet  If value is null and job has not started, status will be `Pending`  If value is null and job has not completed, but is running, status will be `Running`  # noqa: E501

        :param end_date: The end_date of this JobHistory.  # noqa: E501
        :type end_date: datetime
        """

        self._end_date = end_date

    @property
    def arguments(self):
        """Gets the arguments of this JobHistory.  # noqa: E501

        All arguments used in in this job run  # noqa: E501

        :return: The arguments of this JobHistory.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this JobHistory.

        All arguments used in in this job run  # noqa: E501

        :param arguments: The arguments of this JobHistory.  # noqa: E501
        :type arguments: dict(str, str)
        """

        self._arguments = arguments

    @property
    def environment_variables(self):
        """Gets the environment_variables of this JobHistory.  # noqa: E501

        All environment variables used in this job run  # noqa: E501

        :return: The environment_variables of this JobHistory.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """Sets the environment_variables of this JobHistory.

        All environment variables used in this job run  # noqa: E501

        :param environment_variables: The environment_variables of this JobHistory.  # noqa: E501
        :type environment_variables: dict(str, str)
        """

        self._environment_variables = environment_variables

    @property
    def job_status(self):
        """Gets the job_status of this JobHistory.  # noqa: E501

        Current job status  # noqa: E501

        :return: The job_status of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this JobHistory.

        Current job status  # noqa: E501

        :param job_status: The job_status of this JobHistory.  # noqa: E501
        :type job_status: str
        """

        self._job_status = job_status

    @property
    def job_result(self):
        """Gets the job_result of this JobHistory.  # noqa: E501

        Description of the job result  # noqa: E501

        :return: The job_result of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this JobHistory.

        Description of the job result  # noqa: E501

        :param job_result: The job_result of this JobHistory.  # noqa: E501
        :type job_result: str
        """

        self._job_result = job_result

    @property
    def description(self):
        """Gets the description of this JobHistory.  # noqa: E501

        Description of the job  # noqa: E501

        :return: The description of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobHistory.

        Description of the job  # noqa: E501

        :param description: The description of this JobHistory.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def schedule_id(self):
        """Gets the schedule_id of this JobHistory.  # noqa: E501


        :return: The schedule_id of this JobHistory.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this JobHistory.


        :param schedule_id: The schedule_id of this JobHistory.  # noqa: E501
        :type schedule_id: lusid_scheduler.ResourceId
        """

        self._schedule_id = schedule_id

    @property
    def result_url(self):
        """Gets the result_url of this JobHistory.  # noqa: E501

        URI to results. Defaults to null if not available  # noqa: E501

        :return: The result_url of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url):
        """Sets the result_url of this JobHistory.

        URI to results. Defaults to null if not available  # noqa: E501

        :param result_url: The result_url of this JobHistory.  # noqa: E501
        :type result_url: str
        """

        self._result_url = result_url

    @property
    def manually_triggered_by(self):
        """Gets the manually_triggered_by of this JobHistory.  # noqa: E501

        UserId of the user that triggered the job.  Defaults to null if job was ran on a Schedule  # noqa: E501

        :return: The manually_triggered_by of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._manually_triggered_by

    @manually_triggered_by.setter
    def manually_triggered_by(self, manually_triggered_by):
        """Sets the manually_triggered_by of this JobHistory.

        UserId of the user that triggered the job.  Defaults to null if job was ran on a Schedule  # noqa: E501

        :param manually_triggered_by: The manually_triggered_by of this JobHistory.  # noqa: E501
        :type manually_triggered_by: str
        """

        self._manually_triggered_by = manually_triggered_by

    @property
    def command(self):
        """Gets the command of this JobHistory.  # noqa: E501

        The command used to run the job  # noqa: E501

        :return: The command of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this JobHistory.

        The command used to run the job  # noqa: E501

        :param command: The command of this JobHistory.  # noqa: E501
        :type command: str
        """

        self._command = command

    @property
    def message(self):
        """Gets the message of this JobHistory.  # noqa: E501

        Output message generated by the job runner  Value will be null when the job is in a `Running` or `Pending` status  # noqa: E501

        :return: The message of this JobHistory.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobHistory.

        Output message generated by the job runner  Value will be null when the job is in a `Running` or `Pending` status  # noqa: E501

        :param message: The message of this JobHistory.  # noqa: E501
        :type message: str
        """

        self._message = message

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
        if not isinstance(other, JobHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobHistory):
            return True

        return self.to_dict() != other.to_dict()

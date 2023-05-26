# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.791
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


class ScanReport(object):
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
        'severity': 'str',
        'status': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'scan_duration': 'int',
        'summary': 'ScanSummary',
        'vulnerabilities': 'list[Vulnerability]'
    }

    attribute_map = {
        'severity': 'severity',
        'status': 'status',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'scan_duration': 'scanDuration',
        'summary': 'summary',
        'vulnerabilities': 'vulnerabilities'
    }

    required_map = {
        'severity': 'optional',
        'status': 'optional',
        'start_time': 'optional',
        'end_time': 'optional',
        'scan_duration': 'optional',
        'summary': 'optional',
        'vulnerabilities': 'optional'
    }

    def __init__(self, severity=None, status=None, start_time=None, end_time=None, scan_duration=None, summary=None, vulnerabilities=None, local_vars_configuration=None):  # noqa: E501
        """ScanReport - a model defined in OpenAPI"
        
        :param severity:  The overall severity. For example : \"High\" or \"None\"
        :type severity: str
        :param status:  The status of the report
        :type status: str
        :param start_time:  The start time of the scanning process
        :type start_time: datetime
        :param end_time:  The end time of the scanning process
        :type end_time: datetime
        :param scan_duration:  The duration of the scan in seconds
        :type scan_duration: int
        :param summary: 
        :type summary: lusid_scheduler.ScanSummary
        :param vulnerabilities:  List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability
        :type vulnerabilities: list[lusid_scheduler.Vulnerability]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._severity = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._scan_duration = None
        self._summary = None
        self._vulnerabilities = None
        self.discriminator = None

        self.severity = severity
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.scan_duration = scan_duration
        if summary is not None:
            self.summary = summary
        self.vulnerabilities = vulnerabilities

    @property
    def severity(self):
        """Gets the severity of this ScanReport.  # noqa: E501

        The overall severity. For example : \"High\" or \"None\"  # noqa: E501

        :return: The severity of this ScanReport.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ScanReport.

        The overall severity. For example : \"High\" or \"None\"  # noqa: E501

        :param severity: The severity of this ScanReport.  # noqa: E501
        :type severity: str
        """

        self._severity = severity

    @property
    def status(self):
        """Gets the status of this ScanReport.  # noqa: E501

        The status of the report  # noqa: E501

        :return: The status of this ScanReport.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScanReport.

        The status of the report  # noqa: E501

        :param status: The status of this ScanReport.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ScanReport.  # noqa: E501

        The start time of the scanning process  # noqa: E501

        :return: The start_time of this ScanReport.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScanReport.

        The start time of the scanning process  # noqa: E501

        :param start_time: The start_time of this ScanReport.  # noqa: E501
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScanReport.  # noqa: E501

        The end time of the scanning process  # noqa: E501

        :return: The end_time of this ScanReport.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScanReport.

        The end time of the scanning process  # noqa: E501

        :param end_time: The end_time of this ScanReport.  # noqa: E501
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def scan_duration(self):
        """Gets the scan_duration of this ScanReport.  # noqa: E501

        The duration of the scan in seconds  # noqa: E501

        :return: The scan_duration of this ScanReport.  # noqa: E501
        :rtype: int
        """
        return self._scan_duration

    @scan_duration.setter
    def scan_duration(self, scan_duration):
        """Sets the scan_duration of this ScanReport.

        The duration of the scan in seconds  # noqa: E501

        :param scan_duration: The scan_duration of this ScanReport.  # noqa: E501
        :type scan_duration: int
        """

        self._scan_duration = scan_duration

    @property
    def summary(self):
        """Gets the summary of this ScanReport.  # noqa: E501


        :return: The summary of this ScanReport.  # noqa: E501
        :rtype: lusid_scheduler.ScanSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ScanReport.


        :param summary: The summary of this ScanReport.  # noqa: E501
        :type summary: lusid_scheduler.ScanSummary
        """

        self._summary = summary

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this ScanReport.  # noqa: E501

        List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability  # noqa: E501

        :return: The vulnerabilities of this ScanReport.  # noqa: E501
        :rtype: list[lusid_scheduler.Vulnerability]
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this ScanReport.

        List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability  # noqa: E501

        :param vulnerabilities: The vulnerabilities of this ScanReport.  # noqa: E501
        :type vulnerabilities: list[lusid_scheduler.Vulnerability]
        """

        self._vulnerabilities = vulnerabilities

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
        if not isinstance(other, ScanReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanReport):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.829
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


class ArgumentDefinition(object):
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
        'data_type': 'str',
        'required': 'bool',
        'description': 'str',
        'order': 'int',
        'constraints': 'str',
        'passed_as': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'data_type': 'dataType',
        'required': 'required',
        'description': 'description',
        'order': 'order',
        'constraints': 'constraints',
        'passed_as': 'passedAs',
        'default_value': 'defaultValue'
    }

    required_map = {
        'data_type': 'required',
        'required': 'optional',
        'description': 'required',
        'order': 'required',
        'constraints': 'optional',
        'passed_as': 'required',
        'default_value': 'optional'
    }

    def __init__(self, data_type=None, required=None, description=None, order=None, constraints=None, passed_as=None, default_value=None, local_vars_configuration=None):  # noqa: E501
        """ArgumentDefinition - a model defined in OpenAPI"
        
        :param data_type:  Data type of the argument (required)
        :type data_type: str
        :param required:  Optionality of the argument
        :type required: bool
        :param description:  Argument description (required)
        :type description: str
        :param order:  The order of the argument (required)
        :type order: int
        :param constraints:  Constrains of the argument value
        :type constraints: str
        :param passed_as:  Specifies how this argument should be passed in  Allowed values are: CommandLine or EnvironmentVariable    Defaults to: CommandLine (required)
        :type passed_as: str
        :param default_value:  Specify a default value for this argument if no value is provided  The value needs to be convertible to the associated data type
        :type default_value: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data_type = None
        self._required = None
        self._description = None
        self._order = None
        self._constraints = None
        self._passed_as = None
        self._default_value = None
        self.discriminator = None

        self.data_type = data_type
        if required is not None:
            self.required = required
        self.description = description
        self.order = order
        self.constraints = constraints
        self.passed_as = passed_as
        self.default_value = default_value

    @property
    def data_type(self):
        """Gets the data_type of this ArgumentDefinition.  # noqa: E501

        Data type of the argument  # noqa: E501

        :return: The data_type of this ArgumentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ArgumentDefinition.

        Data type of the argument  # noqa: E501

        :param data_type: The data_type of this ArgumentDefinition.  # noqa: E501
        :type data_type: str
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_type is not None and len(data_type) < 1):
            raise ValueError("Invalid value for `data_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._data_type = data_type

    @property
    def required(self):
        """Gets the required of this ArgumentDefinition.  # noqa: E501

        Optionality of the argument  # noqa: E501

        :return: The required of this ArgumentDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ArgumentDefinition.

        Optionality of the argument  # noqa: E501

        :param required: The required of this ArgumentDefinition.  # noqa: E501
        :type required: bool
        """

        self._required = required

    @property
    def description(self):
        """Gets the description of this ArgumentDefinition.  # noqa: E501

        Argument description  # noqa: E501

        :return: The description of this ArgumentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArgumentDefinition.

        Argument description  # noqa: E501

        :param description: The description of this ArgumentDefinition.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def order(self):
        """Gets the order of this ArgumentDefinition.  # noqa: E501

        The order of the argument  # noqa: E501

        :return: The order of this ArgumentDefinition.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ArgumentDefinition.

        The order of the argument  # noqa: E501

        :param order: The order of this ArgumentDefinition.  # noqa: E501
        :type order: int
        """
        if self.local_vars_configuration.client_side_validation and order is None:  # noqa: E501
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def constraints(self):
        """Gets the constraints of this ArgumentDefinition.  # noqa: E501

        Constrains of the argument value  # noqa: E501

        :return: The constraints of this ArgumentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this ArgumentDefinition.

        Constrains of the argument value  # noqa: E501

        :param constraints: The constraints of this ArgumentDefinition.  # noqa: E501
        :type constraints: str
        """

        self._constraints = constraints

    @property
    def passed_as(self):
        """Gets the passed_as of this ArgumentDefinition.  # noqa: E501

        Specifies how this argument should be passed in  Allowed values are: CommandLine or EnvironmentVariable    Defaults to: CommandLine  # noqa: E501

        :return: The passed_as of this ArgumentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._passed_as

    @passed_as.setter
    def passed_as(self, passed_as):
        """Sets the passed_as of this ArgumentDefinition.

        Specifies how this argument should be passed in  Allowed values are: CommandLine or EnvironmentVariable    Defaults to: CommandLine  # noqa: E501

        :param passed_as: The passed_as of this ArgumentDefinition.  # noqa: E501
        :type passed_as: str
        """
        if self.local_vars_configuration.client_side_validation and passed_as is None:  # noqa: E501
            raise ValueError("Invalid value for `passed_as`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                passed_as is not None and len(passed_as) < 1):
            raise ValueError("Invalid value for `passed_as`, length must be greater than or equal to `1`")  # noqa: E501

        self._passed_as = passed_as

    @property
    def default_value(self):
        """Gets the default_value of this ArgumentDefinition.  # noqa: E501

        Specify a default value for this argument if no value is provided  The value needs to be convertible to the associated data type  # noqa: E501

        :return: The default_value of this ArgumentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ArgumentDefinition.

        Specify a default value for this argument if no value is provided  The value needs to be convertible to the associated data type  # noqa: E501

        :param default_value: The default_value of this ArgumentDefinition.  # noqa: E501
        :type default_value: str
        """

        self._default_value = default_value

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
        if not isinstance(other, ArgumentDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArgumentDefinition):
            return True

        return self.to_dict() != other.to_dict()

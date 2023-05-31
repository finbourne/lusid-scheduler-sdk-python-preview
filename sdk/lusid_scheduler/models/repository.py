# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.792
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


class Repository(object):
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
        'name': 'str',
        'creation_time': 'datetime',
        'last_update': 'datetime',
        'description': 'str',
        'pull_count': 'int',
        'image_count': 'int',
        'images': 'Link',
        'links': 'list[Link]'
    }

    attribute_map = {
        'name': 'name',
        'creation_time': 'creationTime',
        'last_update': 'lastUpdate',
        'description': 'description',
        'pull_count': 'pullCount',
        'image_count': 'imageCount',
        'images': 'images',
        'links': 'links'
    }

    required_map = {
        'name': 'optional',
        'creation_time': 'optional',
        'last_update': 'optional',
        'description': 'optional',
        'pull_count': 'optional',
        'image_count': 'optional',
        'images': 'optional',
        'links': 'optional'
    }

    def __init__(self, name=None, creation_time=None, last_update=None, description=None, pull_count=None, image_count=None, images=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Repository - a model defined in OpenAPI"
        
        :param name:  The identifier of the repository
        :type name: str
        :param creation_time:  Date of  repository creation
        :type creation_time: datetime
        :param last_update:  The last update of the repository
        :type last_update: datetime
        :param description:  Description of the repository
        :type description: str
        :param pull_count:  Number of times images were pulled from this repository
        :type pull_count: int
        :param image_count:  The number of versions of this image
        :type image_count: int
        :param images: 
        :type images: lusid_scheduler.Link
        :param links: 
        :type links: list[lusid_scheduler.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._creation_time = None
        self._last_update = None
        self._description = None
        self._pull_count = None
        self._image_count = None
        self._images = None
        self._links = None
        self.discriminator = None

        self.name = name
        if creation_time is not None:
            self.creation_time = creation_time
        if last_update is not None:
            self.last_update = last_update
        self.description = description
        if pull_count is not None:
            self.pull_count = pull_count
        if image_count is not None:
            self.image_count = image_count
        if images is not None:
            self.images = images
        self.links = links

    @property
    def name(self):
        """Gets the name of this Repository.  # noqa: E501

        The identifier of the repository  # noqa: E501

        :return: The name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Repository.

        The identifier of the repository  # noqa: E501

        :param name: The name of this Repository.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this Repository.  # noqa: E501

        Date of  repository creation  # noqa: E501

        :return: The creation_time of this Repository.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Repository.

        Date of  repository creation  # noqa: E501

        :param creation_time: The creation_time of this Repository.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def last_update(self):
        """Gets the last_update of this Repository.  # noqa: E501

        The last update of the repository  # noqa: E501

        :return: The last_update of this Repository.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Repository.

        The last update of the repository  # noqa: E501

        :param last_update: The last_update of this Repository.  # noqa: E501
        :type last_update: datetime
        """

        self._last_update = last_update

    @property
    def description(self):
        """Gets the description of this Repository.  # noqa: E501

        Description of the repository  # noqa: E501

        :return: The description of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Repository.

        Description of the repository  # noqa: E501

        :param description: The description of this Repository.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def pull_count(self):
        """Gets the pull_count of this Repository.  # noqa: E501

        Number of times images were pulled from this repository  # noqa: E501

        :return: The pull_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._pull_count

    @pull_count.setter
    def pull_count(self, pull_count):
        """Sets the pull_count of this Repository.

        Number of times images were pulled from this repository  # noqa: E501

        :param pull_count: The pull_count of this Repository.  # noqa: E501
        :type pull_count: int
        """

        self._pull_count = pull_count

    @property
    def image_count(self):
        """Gets the image_count of this Repository.  # noqa: E501

        The number of versions of this image  # noqa: E501

        :return: The image_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._image_count

    @image_count.setter
    def image_count(self, image_count):
        """Sets the image_count of this Repository.

        The number of versions of this image  # noqa: E501

        :param image_count: The image_count of this Repository.  # noqa: E501
        :type image_count: int
        """

        self._image_count = image_count

    @property
    def images(self):
        """Gets the images of this Repository.  # noqa: E501


        :return: The images of this Repository.  # noqa: E501
        :rtype: lusid_scheduler.Link
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Repository.


        :param images: The images of this Repository.  # noqa: E501
        :type images: lusid_scheduler.Link
        """

        self._images = images

    @property
    def links(self):
        """Gets the links of this Repository.  # noqa: E501


        :return: The links of this Repository.  # noqa: E501
        :rtype: list[lusid_scheduler.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Repository.


        :param links: The links of this Repository.  # noqa: E501
        :type links: list[lusid_scheduler.Link]
        """

        self._links = links

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
        if not isinstance(other, Repository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Repository):
            return True

        return self.to_dict() != other.to_dict()

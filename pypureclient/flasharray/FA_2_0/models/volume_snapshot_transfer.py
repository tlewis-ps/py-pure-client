# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from ....properties import Property
import pprint
import re

import six


class VolumeSnapshotTransfer(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'started': 'int',
        'progress': 'float',
        'completed': 'int',
        'data_transferred': 'int',
        'physical_bytes_written': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'started': 'started',
        'progress': 'progress',
        'completed': 'completed',
        'data_transferred': 'data_transferred',
        'physical_bytes_written': 'physical_bytes_written'
    }

    required_args = {
    }

    def __init__(self, **kwargs):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            started (int): The timestamp of when the snapshot replication process started. Measured in milliseconds since the UNIX epoch.
            progress (float): The percentage progress of the snapshot transfer from the source array to the target. Displayed in decimal format.
            completed (int): The timestamp of when the snapshot replication process completed. Measured in milliseconds since since the UNIX epoch.
            data_transferred (int): The number of bytes transferred from the source array to the target as part of the replication process. The data transferred amount is calculated as the size difference between the current and previous snapshots after data reduction. Measured in bytes.
            physical_bytes_written (int): The amount of data persisted on the target due to replication. Measured in bytes.
        """
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        for arg in self.required_args:
            if arg not in kwargs:
                raise Exception("Required argument {} is missing".format(arg))

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshotTransfer`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(VolumeSnapshotTransfer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VolumeSnapshotTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

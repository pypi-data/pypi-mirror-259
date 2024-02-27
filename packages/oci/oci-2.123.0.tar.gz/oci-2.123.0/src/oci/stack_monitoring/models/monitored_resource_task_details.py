# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceTaskDetails(object):
    """
    The request details for the performing the task.
    """

    #: A constant which can be used with the type property of a MonitoredResourceTaskDetails.
    #: This constant has a value of "IMPORT_OCI_TELEMETRY_RESOURCES"
    TYPE_IMPORT_OCI_TELEMETRY_RESOURCES = "IMPORT_OCI_TELEMETRY_RESOURCES"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceTaskDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.stack_monitoring.models.ImportOciTelemetryResourcesTaskDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this MonitoredResourceTaskDetails.
            Allowed values for this property are: "IMPORT_OCI_TELEMETRY_RESOURCES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'IMPORT_OCI_TELEMETRY_RESOURCES':
            return 'ImportOciTelemetryResourcesTaskDetails'
        else:
            return 'MonitoredResourceTaskDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MonitoredResourceTaskDetails.
        Task type.

        Allowed values for this property are: "IMPORT_OCI_TELEMETRY_RESOURCES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MonitoredResourceTaskDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MonitoredResourceTaskDetails.
        Task type.


        :param type: The type of this MonitoredResourceTaskDetails.
        :type: str
        """
        allowed_values = ["IMPORT_OCI_TELEMETRY_RESOURCES"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

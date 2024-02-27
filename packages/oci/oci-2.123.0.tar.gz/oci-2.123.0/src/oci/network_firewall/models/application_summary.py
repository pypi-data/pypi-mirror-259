# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationSummary(object):
    """
    Summary object for application element in the network firewall policy.
    """

    #: A constant which can be used with the type property of a ApplicationSummary.
    #: This constant has a value of "ICMP"
    TYPE_ICMP = "ICMP"

    #: A constant which can be used with the type property of a ApplicationSummary.
    #: This constant has a value of "ICMP_V6"
    TYPE_ICMP_V6 = "ICMP_V6"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.network_firewall.models.Icmp6ApplicationSummary`
        * :class:`~oci.network_firewall.models.IcmpApplicationSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ApplicationSummary.
            Allowed values for this property are: "ICMP", "ICMP_V6", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param name:
            The value to assign to the name property of this ApplicationSummary.
        :type name: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this ApplicationSummary.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'parent_resource_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'parent_resource_id': 'parentResourceId'
        }

        self._type = None
        self._name = None
        self._parent_resource_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'ICMP_V6':
            return 'Icmp6ApplicationSummary'

        if type == 'ICMP':
            return 'IcmpApplicationSummary'
        else:
            return 'ApplicationSummary'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ApplicationSummary.
        Describes the type of Application.

        Allowed values for this property are: "ICMP", "ICMP_V6", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ApplicationSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApplicationSummary.
        Describes the type of Application.


        :param type: The type of this ApplicationSummary.
        :type: str
        """
        allowed_values = ["ICMP", "ICMP_V6"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ApplicationSummary.
        Name of the application.


        :return: The name of this ApplicationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApplicationSummary.
        Name of the application.


        :param name: The name of this ApplicationSummary.
        :type: str
        """
        self._name = name

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this ApplicationSummary.
        OCID of the Network Firewall Policy this application belongs to.


        :return: The parent_resource_id of this ApplicationSummary.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this ApplicationSummary.
        OCID of the Network Firewall Policy this application belongs to.


        :param parent_resource_id: The parent_resource_id of this ApplicationSummary.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

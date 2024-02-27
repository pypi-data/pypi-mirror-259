# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopNetworkConfiguration(object):
    """
    Provides information about the network configuration of the desktop pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopNetworkConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this DesktopNetworkConfiguration.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DesktopNetworkConfiguration.
        :type subnet_id: str

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId'
        }

        self._vcn_id = None
        self._subnet_id = None

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DesktopNetworkConfiguration.
        The OCID of the VCN used by the desktop pool.


        :return: The vcn_id of this DesktopNetworkConfiguration.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DesktopNetworkConfiguration.
        The OCID of the VCN used by the desktop pool.


        :param vcn_id: The vcn_id of this DesktopNetworkConfiguration.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DesktopNetworkConfiguration.
        The OCID of the subnet to use for the desktop pool.


        :return: The subnet_id of this DesktopNetworkConfiguration.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DesktopNetworkConfiguration.
        The OCID of the subnet to use for the desktop pool.


        :param subnet_id: The subnet_id of this DesktopNetworkConfiguration.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

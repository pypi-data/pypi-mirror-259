# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .capacity_source import CapacitySource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedCapacitySource(CapacitySource):
    """
    A capacity source of bare metal hosts that is dedicated to a user.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedCapacitySource object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DedicatedCapacitySource.capacity_type` attribute
        of this class is ``DEDICATED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity_type:
            The value to assign to the capacity_type property of this DedicatedCapacitySource.
            Allowed values for this property are: "DEDICATED"
        :type capacity_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DedicatedCapacitySource.
        :type compartment_id: str

        """
        self.swagger_types = {
            'capacity_type': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'capacity_type': 'capacityType',
            'compartment_id': 'compartmentId'
        }

        self._capacity_type = None
        self._compartment_id = None
        self._capacity_type = 'DEDICATED'

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DedicatedCapacitySource.
        The `OCID`__ of the compartment of this capacity source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DedicatedCapacitySource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DedicatedCapacitySource.
        The `OCID`__ of the compartment of this capacity source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DedicatedCapacitySource.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

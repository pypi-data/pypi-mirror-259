# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailableSoftwareSourceSummary(object):
    """
    A software source which can be added to a managed instance. Once a software source is added, packages from that software source can be installed on that managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailableSoftwareSourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AvailableSoftwareSourceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AvailableSoftwareSourceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AvailableSoftwareSourceSummary.
        :type display_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AvailableSoftwareSourceSummary.
        unique identifier that is immutable on creation.


        :return: The id of this AvailableSoftwareSourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AvailableSoftwareSourceSummary.
        unique identifier that is immutable on creation.


        :param id: The id of this AvailableSoftwareSourceSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AvailableSoftwareSourceSummary.
        The OCID for the compartment.


        :return: The compartment_id of this AvailableSoftwareSourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AvailableSoftwareSourceSummary.
        The OCID for the compartment.


        :param compartment_id: The compartment_id of this AvailableSoftwareSourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AvailableSoftwareSourceSummary.
        User friendly name for the software source.


        :return: The display_name of this AvailableSoftwareSourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AvailableSoftwareSourceSummary.
        User friendly name for the software source.


        :param display_name: The display_name of this AvailableSoftwareSourceSummary.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

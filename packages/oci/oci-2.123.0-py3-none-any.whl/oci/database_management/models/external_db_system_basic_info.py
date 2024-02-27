# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemBasicInfo(object):
    """
    The basic information about an external DB system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemBasicInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalDbSystemBasicInfo.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemBasicInfo.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDbSystemBasicInfo.
        :type compartment_id: str

        :param exadata_infra_info:
            The value to assign to the exadata_infra_info property of this ExternalDbSystemBasicInfo.
        :type exadata_infra_info: oci.database_management.models.ExternalExadataInfraBasicInfo

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'exadata_infra_info': 'ExternalExadataInfraBasicInfo'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'exadata_infra_info': 'exadataInfraInfo'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._exadata_infra_info = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalDbSystemBasicInfo.
        The `OCID`__ of the external DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalDbSystemBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalDbSystemBasicInfo.
        The `OCID`__ of the external DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalDbSystemBasicInfo.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalDbSystemBasicInfo.
        The user-friendly name for the DB system. The name does not have to be unique.


        :return: The display_name of this ExternalDbSystemBasicInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalDbSystemBasicInfo.
        The user-friendly name for the DB system. The name does not have to be unique.


        :param display_name: The display_name of this ExternalDbSystemBasicInfo.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalDbSystemBasicInfo.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalDbSystemBasicInfo.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalDbSystemBasicInfo.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalDbSystemBasicInfo.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def exadata_infra_info(self):
        """
        Gets the exadata_infra_info of this ExternalDbSystemBasicInfo.

        :return: The exadata_infra_info of this ExternalDbSystemBasicInfo.
        :rtype: oci.database_management.models.ExternalExadataInfraBasicInfo
        """
        return self._exadata_infra_info

    @exadata_infra_info.setter
    def exadata_infra_info(self, exadata_infra_info):
        """
        Sets the exadata_infra_info of this ExternalDbSystemBasicInfo.

        :param exadata_infra_info: The exadata_infra_info of this ExternalDbSystemBasicInfo.
        :type: oci.database_management.models.ExternalExadataInfraBasicInfo
        """
        self._exadata_infra_info = exadata_infra_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

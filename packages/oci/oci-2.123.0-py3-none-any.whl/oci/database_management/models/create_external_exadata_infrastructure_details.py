# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExternalExadataInfrastructureDetails(object):
    """
    The details required to create the external Exadata infrastructure.
    """

    #: A constant which can be used with the license_model property of a CreateExternalExadataInfrastructureDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateExternalExadataInfrastructureDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExternalExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param discovery_key:
            The value to assign to the discovery_key property of this CreateExternalExadataInfrastructureDetails.
        :type discovery_key: str

        :param license_model:
            The value to assign to the license_model property of this CreateExternalExadataInfrastructureDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateExternalExadataInfrastructureDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateExternalExadataInfrastructureDetails.
        :type display_name: str

        :param db_system_ids:
            The value to assign to the db_system_ids property of this CreateExternalExadataInfrastructureDetails.
        :type db_system_ids: list[str]

        :param storage_server_names:
            The value to assign to the storage_server_names property of this CreateExternalExadataInfrastructureDetails.
        :type storage_server_names: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateExternalExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateExternalExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'discovery_key': 'str',
            'license_model': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'db_system_ids': 'list[str]',
            'storage_server_names': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'discovery_key': 'discoveryKey',
            'license_model': 'licenseModel',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'db_system_ids': 'dbSystemIds',
            'storage_server_names': 'storageServerNames',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._discovery_key = None
        self._license_model = None
        self._compartment_id = None
        self._display_name = None
        self._db_system_ids = None
        self._storage_server_names = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def discovery_key(self):
        """
        Gets the discovery_key of this CreateExternalExadataInfrastructureDetails.
        The unique key of the discovery request.


        :return: The discovery_key of this CreateExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._discovery_key

    @discovery_key.setter
    def discovery_key(self, discovery_key):
        """
        Sets the discovery_key of this CreateExternalExadataInfrastructureDetails.
        The unique key of the discovery request.


        :param discovery_key: The discovery_key of this CreateExternalExadataInfrastructureDetails.
        :type: str
        """
        self._discovery_key = discovery_key

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateExternalExadataInfrastructureDetails.
        The Oracle license model that applies to the database management resources.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateExternalExadataInfrastructureDetails.
        The Oracle license model that applies to the database management resources.


        :param license_model: The license_model of this CreateExternalExadataInfrastructureDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                f"Invalid value for `license_model`, must be None or one of {allowed_values}"
            )
        self._license_model = license_model

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateExternalExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateExternalExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateExternalExadataInfrastructureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateExternalExadataInfrastructureDetails.
        The name of the Exadata infrastructure.


        :return: The display_name of this CreateExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateExternalExadataInfrastructureDetails.
        The name of the Exadata infrastructure.


        :param display_name: The display_name of this CreateExternalExadataInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def db_system_ids(self):
        """
        **[Required]** Gets the db_system_ids of this CreateExternalExadataInfrastructureDetails.
        The list of DB systems in the Exadata infrastructure.


        :return: The db_system_ids of this CreateExternalExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._db_system_ids

    @db_system_ids.setter
    def db_system_ids(self, db_system_ids):
        """
        Sets the db_system_ids of this CreateExternalExadataInfrastructureDetails.
        The list of DB systems in the Exadata infrastructure.


        :param db_system_ids: The db_system_ids of this CreateExternalExadataInfrastructureDetails.
        :type: list[str]
        """
        self._db_system_ids = db_system_ids

    @property
    def storage_server_names(self):
        """
        Gets the storage_server_names of this CreateExternalExadataInfrastructureDetails.
        The list of all the Exadata storage server names to be included for monitoring purposes. If not specified, all the Exadata storage servers associated with the DB systems are included.


        :return: The storage_server_names of this CreateExternalExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._storage_server_names

    @storage_server_names.setter
    def storage_server_names(self, storage_server_names):
        """
        Sets the storage_server_names of this CreateExternalExadataInfrastructureDetails.
        The list of all the Exadata storage server names to be included for monitoring purposes. If not specified, all the Exadata storage servers associated with the DB systems are included.


        :param storage_server_names: The storage_server_names of this CreateExternalExadataInfrastructureDetails.
        :type: list[str]
        """
        self._storage_server_names = storage_server_names

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateExternalExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateExternalExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateExternalExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateExternalExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateExternalExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateExternalExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateExternalExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateExternalExadataInfrastructureDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

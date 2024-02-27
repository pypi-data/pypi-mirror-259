# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAmazonRedshiftConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Amazon Redshift Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAmazonRedshiftConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateAmazonRedshiftConnectionDetails.connection_type` attribute
        of this class is ``AMAZON_REDSHIFT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateAmazonRedshiftConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateAmazonRedshiftConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAmazonRedshiftConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAmazonRedshiftConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAmazonRedshiftConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAmazonRedshiftConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateAmazonRedshiftConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateAmazonRedshiftConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateAmazonRedshiftConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateAmazonRedshiftConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this CreateAmazonRedshiftConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param technology_type:
            The value to assign to the technology_type property of this CreateAmazonRedshiftConnectionDetails.
        :type technology_type: str

        :param connection_url:
            The value to assign to the connection_url property of this CreateAmazonRedshiftConnectionDetails.
        :type connection_url: str

        :param username:
            The value to assign to the username property of this CreateAmazonRedshiftConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateAmazonRedshiftConnectionDetails.
        :type password: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'technology_type': 'str',
            'connection_url': 'str',
            'username': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'technology_type': 'technologyType',
            'connection_url': 'connectionUrl',
            'username': 'username',
            'password': 'password'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._technology_type = None
        self._connection_url = None
        self._username = None
        self._password = None
        self._connection_type = 'AMAZON_REDSHIFT'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateAmazonRedshiftConnectionDetails.
        The Amazon Redshift technology type.


        :return: The technology_type of this CreateAmazonRedshiftConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateAmazonRedshiftConnectionDetails.
        The Amazon Redshift technology type.


        :param technology_type: The technology_type of this CreateAmazonRedshiftConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def connection_url(self):
        """
        **[Required]** Gets the connection_url of this CreateAmazonRedshiftConnectionDetails.
        Connection URL.
        e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'


        :return: The connection_url of this CreateAmazonRedshiftConnectionDetails.
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """
        Sets the connection_url of this CreateAmazonRedshiftConnectionDetails.
        Connection URL.
        e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'


        :param connection_url: The connection_url of this CreateAmazonRedshiftConnectionDetails.
        :type: str
        """
        self._connection_url = connection_url

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateAmazonRedshiftConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :return: The username of this CreateAmazonRedshiftConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateAmazonRedshiftConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :param username: The username of this CreateAmazonRedshiftConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateAmazonRedshiftConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.


        :return: The password of this CreateAmazonRedshiftConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateAmazonRedshiftConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.


        :param password: The password of this CreateAmazonRedshiftConnectionDetails.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

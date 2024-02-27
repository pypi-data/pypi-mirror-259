# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemSummary(object):
    """
    Summary information about a database system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbSystemSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DbSystemSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbSystemSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DbSystemSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DbSystemSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbSystemSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbSystemSummary.
        :type lifecycle_details: str

        :param system_type:
            The value to assign to the system_type property of this DbSystemSummary.
        :type system_type: str

        :param instance_count:
            The value to assign to the instance_count property of this DbSystemSummary.
        :type instance_count: int

        :param shape:
            The value to assign to the shape property of this DbSystemSummary.
        :type shape: str

        :param instance_ocpu_count:
            The value to assign to the instance_ocpu_count property of this DbSystemSummary.
        :type instance_ocpu_count: int

        :param instance_memory_size_in_gbs:
            The value to assign to the instance_memory_size_in_gbs property of this DbSystemSummary.
        :type instance_memory_size_in_gbs: int

        :param db_version:
            The value to assign to the db_version property of this DbSystemSummary.
        :type db_version: str

        :param config_id:
            The value to assign to the config_id property of this DbSystemSummary.
        :type config_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DbSystemSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DbSystemSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DbSystemSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'system_type': 'str',
            'instance_count': 'int',
            'shape': 'str',
            'instance_ocpu_count': 'int',
            'instance_memory_size_in_gbs': 'int',
            'db_version': 'str',
            'config_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'system_type': 'systemType',
            'instance_count': 'instanceCount',
            'shape': 'shape',
            'instance_ocpu_count': 'instanceOcpuCount',
            'instance_memory_size_in_gbs': 'instanceMemorySizeInGBs',
            'db_version': 'dbVersion',
            'config_id': 'configId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._system_type = None
        self._instance_count = None
        self._shape = None
        self._instance_ocpu_count = None
        self._instance_memory_size_in_gbs = None
        self._db_version = None
        self._config_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbSystemSummary.
        A unique identifier for the database system. Immutable on creation.


        :return: The id of this DbSystemSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystemSummary.
        A unique identifier for the database system. Immutable on creation.


        :param id: The id of this DbSystemSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DbSystemSummary.
        A user-friendly display name for the database system. Avoid entering confidential information.


        :return: The display_name of this DbSystemSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbSystemSummary.
        A user-friendly display name for the database system. Avoid entering confidential information.


        :param display_name: The display_name of this DbSystemSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbSystemSummary.
        The `OCID`__ of the compartment that contains the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbSystemSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbSystemSummary.
        The `OCID`__ of the compartment that contains the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbSystemSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DbSystemSummary.
        The date and time that the database system was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this DbSystemSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbSystemSummary.
        The date and time that the database system was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this DbSystemSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DbSystemSummary.
        The date and time that the database system was updated, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this DbSystemSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DbSystemSummary.
        The date and time that the database system was updated, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this DbSystemSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbSystemSummary.
        The current state of the database system.


        :return: The lifecycle_state of this DbSystemSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbSystemSummary.
        The current state of the database system.


        :param lifecycle_state: The lifecycle_state of this DbSystemSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DbSystemSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DbSystemSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DbSystemSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DbSystemSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def system_type(self):
        """
        **[Required]** Gets the system_type of this DbSystemSummary.
        Type of the database system.


        :return: The system_type of this DbSystemSummary.
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """
        Sets the system_type of this DbSystemSummary.
        Type of the database system.


        :param system_type: The system_type of this DbSystemSummary.
        :type: str
        """
        self._system_type = system_type

    @property
    def instance_count(self):
        """
        **[Required]** Gets the instance_count of this DbSystemSummary.
        Count of database instances, or nodes, in the database system.


        :return: The instance_count of this DbSystemSummary.
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """
        Sets the instance_count of this DbSystemSummary.
        Count of database instances, or nodes, in the database system.


        :param instance_count: The instance_count of this DbSystemSummary.
        :type: int
        """
        self._instance_count = instance_count

    @property
    def shape(self):
        """
        Gets the shape of this DbSystemSummary.
        The name of the shape for the database instance node.
        Example: `VM.Standard.E4.Flex`


        :return: The shape of this DbSystemSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DbSystemSummary.
        The name of the shape for the database instance node.
        Example: `VM.Standard.E4.Flex`


        :param shape: The shape of this DbSystemSummary.
        :type: str
        """
        self._shape = shape

    @property
    def instance_ocpu_count(self):
        """
        **[Required]** Gets the instance_ocpu_count of this DbSystemSummary.
        The total number of OCPUs available to each database instance node.


        :return: The instance_ocpu_count of this DbSystemSummary.
        :rtype: int
        """
        return self._instance_ocpu_count

    @instance_ocpu_count.setter
    def instance_ocpu_count(self, instance_ocpu_count):
        """
        Sets the instance_ocpu_count of this DbSystemSummary.
        The total number of OCPUs available to each database instance node.


        :param instance_ocpu_count: The instance_ocpu_count of this DbSystemSummary.
        :type: int
        """
        self._instance_ocpu_count = instance_ocpu_count

    @property
    def instance_memory_size_in_gbs(self):
        """
        **[Required]** Gets the instance_memory_size_in_gbs of this DbSystemSummary.
        The total amount of memory available to each database instance node, in gigabytes.


        :return: The instance_memory_size_in_gbs of this DbSystemSummary.
        :rtype: int
        """
        return self._instance_memory_size_in_gbs

    @instance_memory_size_in_gbs.setter
    def instance_memory_size_in_gbs(self, instance_memory_size_in_gbs):
        """
        Sets the instance_memory_size_in_gbs of this DbSystemSummary.
        The total amount of memory available to each database instance node, in gigabytes.


        :param instance_memory_size_in_gbs: The instance_memory_size_in_gbs of this DbSystemSummary.
        :type: int
        """
        self._instance_memory_size_in_gbs = instance_memory_size_in_gbs

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this DbSystemSummary.
        Version of database system software.


        :return: The db_version of this DbSystemSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DbSystemSummary.
        Version of database system software.


        :param db_version: The db_version of this DbSystemSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def config_id(self):
        """
        Gets the config_id of this DbSystemSummary.
        The `OCID`__ of the configuration associated with the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The config_id of this DbSystemSummary.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """
        Sets the config_id of this DbSystemSummary.
        The `OCID`__ of the configuration associated with the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param config_id: The config_id of this DbSystemSummary.
        :type: str
        """
        self._config_id = config_id

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this DbSystemSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DbSystemSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DbSystemSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DbSystemSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this DbSystemSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DbSystemSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DbSystemSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DbSystemSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DbSystemSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DbSystemSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DbSystemSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DbSystemSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

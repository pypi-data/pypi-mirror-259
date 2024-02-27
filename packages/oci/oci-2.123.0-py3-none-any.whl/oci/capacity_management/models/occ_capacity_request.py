# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccCapacityRequest(object):
    """
    A single request of some quantity of a specific server type, in a specific location and expected delivery date. The maximum amount possible to request is the smallest number between the number of servers available for purchase and the number of servers allowed by the constraints (For example, power, network, physical space, and so on).
    """

    #: A constant which can be used with the namespace property of a OccCapacityRequest.
    #: This constant has a value of "COMPUTE"
    NAMESPACE_COMPUTE = "COMPUTE"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "CREATED"
    REQUEST_STATE_CREATED = "CREATED"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "SUBMITTED"
    REQUEST_STATE_SUBMITTED = "SUBMITTED"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "REJECTED"
    REQUEST_STATE_REJECTED = "REJECTED"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "IN_PROGRESS"
    REQUEST_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "COMPLETED"
    REQUEST_STATE_COMPLETED = "COMPLETED"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "PARTIALLY_COMPLETED"
    REQUEST_STATE_PARTIALLY_COMPLETED = "PARTIALLY_COMPLETED"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "CANCELLED"
    REQUEST_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the request_state property of a OccCapacityRequest.
    #: This constant has a value of "DELETED"
    REQUEST_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OccCapacityRequest.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OccCapacityRequest.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OccCapacityRequest.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OccCapacityRequest.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OccCapacityRequest.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OccCapacityRequest.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OccCapacityRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OccCapacityRequest.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OccCapacityRequest.
        :type compartment_id: str

        :param occ_availability_catalog_id:
            The value to assign to the occ_availability_catalog_id property of this OccCapacityRequest.
        :type occ_availability_catalog_id: str

        :param display_name:
            The value to assign to the display_name property of this OccCapacityRequest.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OccCapacityRequest.
        :type description: str

        :param namespace:
            The value to assign to the namespace property of this OccCapacityRequest.
            Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type namespace: str

        :param occ_customer_group_id:
            The value to assign to the occ_customer_group_id property of this OccCapacityRequest.
        :type occ_customer_group_id: str

        :param region:
            The value to assign to the region property of this OccCapacityRequest.
        :type region: str

        :param availability_domain:
            The value to assign to the availability_domain property of this OccCapacityRequest.
        :type availability_domain: str

        :param date_expected_capacity_handover:
            The value to assign to the date_expected_capacity_handover property of this OccCapacityRequest.
        :type date_expected_capacity_handover: datetime

        :param request_state:
            The value to assign to the request_state property of this OccCapacityRequest.
            Allowed values for this property are: "CREATED", "SUBMITTED", "REJECTED", "IN_PROGRESS", "COMPLETED", "PARTIALLY_COMPLETED", "CANCELLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_state: str

        :param time_created:
            The value to assign to the time_created property of this OccCapacityRequest.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OccCapacityRequest.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OccCapacityRequest.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OccCapacityRequest.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OccCapacityRequest.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OccCapacityRequest.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OccCapacityRequest.
        :type system_tags: dict(str, dict(str, object))

        :param details:
            The value to assign to the details property of this OccCapacityRequest.
        :type details: list[oci.capacity_management.models.OccCapacityRequestBaseDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'occ_availability_catalog_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'namespace': 'str',
            'occ_customer_group_id': 'str',
            'region': 'str',
            'availability_domain': 'str',
            'date_expected_capacity_handover': 'datetime',
            'request_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'details': 'list[OccCapacityRequestBaseDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'occ_availability_catalog_id': 'occAvailabilityCatalogId',
            'display_name': 'displayName',
            'description': 'description',
            'namespace': 'namespace',
            'occ_customer_group_id': 'occCustomerGroupId',
            'region': 'region',
            'availability_domain': 'availabilityDomain',
            'date_expected_capacity_handover': 'dateExpectedCapacityHandover',
            'request_state': 'requestState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'details': 'details'
        }

        self._id = None
        self._compartment_id = None
        self._occ_availability_catalog_id = None
        self._display_name = None
        self._description = None
        self._namespace = None
        self._occ_customer_group_id = None
        self._region = None
        self._availability_domain = None
        self._date_expected_capacity_handover = None
        self._request_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OccCapacityRequest.
        The OCID of the capacity request.


        :return: The id of this OccCapacityRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OccCapacityRequest.
        The OCID of the capacity request.


        :param id: The id of this OccCapacityRequest.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OccCapacityRequest.
        The OCID of the tenancy from which the request was made.


        :return: The compartment_id of this OccCapacityRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OccCapacityRequest.
        The OCID of the tenancy from which the request was made.


        :param compartment_id: The compartment_id of this OccCapacityRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def occ_availability_catalog_id(self):
        """
        **[Required]** Gets the occ_availability_catalog_id of this OccCapacityRequest.
        The OCID of the availability catalog against which the capacity request was placed.


        :return: The occ_availability_catalog_id of this OccCapacityRequest.
        :rtype: str
        """
        return self._occ_availability_catalog_id

    @occ_availability_catalog_id.setter
    def occ_availability_catalog_id(self, occ_availability_catalog_id):
        """
        Sets the occ_availability_catalog_id of this OccCapacityRequest.
        The OCID of the availability catalog against which the capacity request was placed.


        :param occ_availability_catalog_id: The occ_availability_catalog_id of this OccCapacityRequest.
        :type: str
        """
        self._occ_availability_catalog_id = occ_availability_catalog_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OccCapacityRequest.
        The display name of the capacity request.


        :return: The display_name of this OccCapacityRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OccCapacityRequest.
        The display name of the capacity request.


        :param display_name: The display_name of this OccCapacityRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OccCapacityRequest.
        Meaningful text about the capacity request.


        :return: The description of this OccCapacityRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OccCapacityRequest.
        Meaningful text about the capacity request.


        :param description: The description of this OccCapacityRequest.
        :type: str
        """
        self._description = description

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this OccCapacityRequest.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.

        Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The namespace of this OccCapacityRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OccCapacityRequest.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.


        :param namespace: The namespace of this OccCapacityRequest.
        :type: str
        """
        allowed_values = ["COMPUTE"]
        if not value_allowed_none_or_none_sentinel(namespace, allowed_values):
            namespace = 'UNKNOWN_ENUM_VALUE'
        self._namespace = namespace

    @property
    def occ_customer_group_id(self):
        """
        **[Required]** Gets the occ_customer_group_id of this OccCapacityRequest.
        The OCID of the customer group to which this customer belongs to.


        :return: The occ_customer_group_id of this OccCapacityRequest.
        :rtype: str
        """
        return self._occ_customer_group_id

    @occ_customer_group_id.setter
    def occ_customer_group_id(self, occ_customer_group_id):
        """
        Sets the occ_customer_group_id of this OccCapacityRequest.
        The OCID of the customer group to which this customer belongs to.


        :param occ_customer_group_id: The occ_customer_group_id of this OccCapacityRequest.
        :type: str
        """
        self._occ_customer_group_id = occ_customer_group_id

    @property
    def region(self):
        """
        **[Required]** Gets the region of this OccCapacityRequest.
        The name of the region for which the capacity request was made.


        :return: The region of this OccCapacityRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this OccCapacityRequest.
        The name of the region for which the capacity request was made.


        :param region: The region of this OccCapacityRequest.
        :type: str
        """
        self._region = region

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this OccCapacityRequest.
        The availability domain (AD) for which the capacity request was made.


        :return: The availability_domain of this OccCapacityRequest.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this OccCapacityRequest.
        The availability domain (AD) for which the capacity request was made.


        :param availability_domain: The availability_domain of this OccCapacityRequest.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def date_expected_capacity_handover(self):
        """
        **[Required]** Gets the date_expected_capacity_handover of this OccCapacityRequest.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :return: The date_expected_capacity_handover of this OccCapacityRequest.
        :rtype: datetime
        """
        return self._date_expected_capacity_handover

    @date_expected_capacity_handover.setter
    def date_expected_capacity_handover(self, date_expected_capacity_handover):
        """
        Sets the date_expected_capacity_handover of this OccCapacityRequest.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :param date_expected_capacity_handover: The date_expected_capacity_handover of this OccCapacityRequest.
        :type: datetime
        """
        self._date_expected_capacity_handover = date_expected_capacity_handover

    @property
    def request_state(self):
        """
        **[Required]** Gets the request_state of this OccCapacityRequest.
        The different states the capacity request goes through.

        Allowed values for this property are: "CREATED", "SUBMITTED", "REJECTED", "IN_PROGRESS", "COMPLETED", "PARTIALLY_COMPLETED", "CANCELLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_state of this OccCapacityRequest.
        :rtype: str
        """
        return self._request_state

    @request_state.setter
    def request_state(self, request_state):
        """
        Sets the request_state of this OccCapacityRequest.
        The different states the capacity request goes through.


        :param request_state: The request_state of this OccCapacityRequest.
        :type: str
        """
        allowed_values = ["CREATED", "SUBMITTED", "REJECTED", "IN_PROGRESS", "COMPLETED", "PARTIALLY_COMPLETED", "CANCELLED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(request_state, allowed_values):
            request_state = 'UNKNOWN_ENUM_VALUE'
        self._request_state = request_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OccCapacityRequest.
        The time when the capacity request was created.


        :return: The time_created of this OccCapacityRequest.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OccCapacityRequest.
        The time when the capacity request was created.


        :param time_created: The time_created of this OccCapacityRequest.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this OccCapacityRequest.
        The time when the capacity request was updated.


        :return: The time_updated of this OccCapacityRequest.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OccCapacityRequest.
        The time when the capacity request was updated.


        :param time_updated: The time_updated of this OccCapacityRequest.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OccCapacityRequest.
        The current lifecycle state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OccCapacityRequest.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OccCapacityRequest.
        The current lifecycle state of the resource.


        :param lifecycle_state: The lifecycle_state of this OccCapacityRequest.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OccCapacityRequest.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :return: The lifecycle_details of this OccCapacityRequest.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OccCapacityRequest.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :param lifecycle_details: The lifecycle_details of this OccCapacityRequest.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OccCapacityRequest.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OccCapacityRequest.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OccCapacityRequest.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OccCapacityRequest.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OccCapacityRequest.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OccCapacityRequest.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OccCapacityRequest.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OccCapacityRequest.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OccCapacityRequest.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OccCapacityRequest.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OccCapacityRequest.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OccCapacityRequest.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def details(self):
        """
        **[Required]** Gets the details of this OccCapacityRequest.
        A list of resources requested as part of this request


        :return: The details of this OccCapacityRequest.
        :rtype: list[oci.capacity_management.models.OccCapacityRequestBaseDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this OccCapacityRequest.
        A list of resources requested as part of this request


        :param details: The details of this OccCapacityRequest.
        :type: list[oci.capacity_management.models.OccCapacityRequestBaseDetails]
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FsuCycleSummary(object):
    """
    Exadata Fleet Update Cycle Summary.
    """

    #: A constant which can be used with the type property of a FsuCycleSummary.
    #: This constant has a value of "PATCH"
    TYPE_PATCH = "PATCH"

    #: A constant which can be used with the collection_type property of a FsuCycleSummary.
    #: This constant has a value of "DB"
    COLLECTION_TYPE_DB = "DB"

    #: A constant which can be used with the collection_type property of a FsuCycleSummary.
    #: This constant has a value of "GI"
    COLLECTION_TYPE_GI = "GI"

    #: A constant which can be used with the last_completed_action property of a FsuCycleSummary.
    #: This constant has a value of "STAGE"
    LAST_COMPLETED_ACTION_STAGE = "STAGE"

    #: A constant which can be used with the last_completed_action property of a FsuCycleSummary.
    #: This constant has a value of "PRECHECK_STAGE"
    LAST_COMPLETED_ACTION_PRECHECK_STAGE = "PRECHECK_STAGE"

    #: A constant which can be used with the last_completed_action property of a FsuCycleSummary.
    #: This constant has a value of "PRECHECK_APPLY"
    LAST_COMPLETED_ACTION_PRECHECK_APPLY = "PRECHECK_APPLY"

    #: A constant which can be used with the last_completed_action property of a FsuCycleSummary.
    #: This constant has a value of "APPLY"
    LAST_COMPLETED_ACTION_APPLY = "APPLY"

    #: A constant which can be used with the last_completed_action property of a FsuCycleSummary.
    #: This constant has a value of "ROLLBACK_AND_REMOVE_TARGET"
    LAST_COMPLETED_ACTION_ROLLBACK_AND_REMOVE_TARGET = "ROLLBACK_AND_REMOVE_TARGET"

    #: A constant which can be used with the last_completed_action property of a FsuCycleSummary.
    #: This constant has a value of "CLEANUP"
    LAST_COMPLETED_ACTION_CLEANUP = "CLEANUP"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FsuCycleSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new FsuCycleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FsuCycleSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FsuCycleSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FsuCycleSummary.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this FsuCycleSummary.
            Allowed values for this property are: "PATCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param fsu_collection_id:
            The value to assign to the fsu_collection_id property of this FsuCycleSummary.
        :type fsu_collection_id: str

        :param collection_type:
            The value to assign to the collection_type property of this FsuCycleSummary.
            Allowed values for this property are: "DB", "GI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type collection_type: str

        :param executing_fsu_action_id:
            The value to assign to the executing_fsu_action_id property of this FsuCycleSummary.
        :type executing_fsu_action_id: str

        :param next_action_to_execute:
            The value to assign to the next_action_to_execute property of this FsuCycleSummary.
        :type next_action_to_execute: list[oci.fleet_software_update.models.NextActionToExecuteDetails]

        :param last_completed_action:
            The value to assign to the last_completed_action property of this FsuCycleSummary.
            Allowed values for this property are: "STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_completed_action: str

        :param goal_version_details:
            The value to assign to the goal_version_details property of this FsuCycleSummary.
        :type goal_version_details: oci.fleet_software_update.models.FsuGoalVersionDetails

        :param time_created:
            The value to assign to the time_created property of this FsuCycleSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FsuCycleSummary.
        :type time_updated: datetime

        :param time_finished:
            The value to assign to the time_finished property of this FsuCycleSummary.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FsuCycleSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "IN_PROGRESS", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FsuCycleSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FsuCycleSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FsuCycleSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this FsuCycleSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'fsu_collection_id': 'str',
            'collection_type': 'str',
            'executing_fsu_action_id': 'str',
            'next_action_to_execute': 'list[NextActionToExecuteDetails]',
            'last_completed_action': 'str',
            'goal_version_details': 'FsuGoalVersionDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'fsu_collection_id': 'fsuCollectionId',
            'collection_type': 'collectionType',
            'executing_fsu_action_id': 'executingFsuActionId',
            'next_action_to_execute': 'nextActionToExecute',
            'last_completed_action': 'lastCompletedAction',
            'goal_version_details': 'goalVersionDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._fsu_collection_id = None
        self._collection_type = None
        self._executing_fsu_action_id = None
        self._next_action_to_execute = None
        self._last_completed_action = None
        self._goal_version_details = None
        self._time_created = None
        self._time_updated = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FsuCycleSummary.
        OCID identifier for the Exadata Fleet Update Cycle.


        :return: The id of this FsuCycleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FsuCycleSummary.
        OCID identifier for the Exadata Fleet Update Cycle.


        :param id: The id of this FsuCycleSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this FsuCycleSummary.
        Exadata Fleet Update Cycle display name.


        :return: The display_name of this FsuCycleSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FsuCycleSummary.
        Exadata Fleet Update Cycle display name.


        :param display_name: The display_name of this FsuCycleSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FsuCycleSummary.
        Compartment Identifier.


        :return: The compartment_id of this FsuCycleSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FsuCycleSummary.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this FsuCycleSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FsuCycleSummary.
        Type of Exadata Fleet Update Cycle.

        Allowed values for this property are: "PATCH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this FsuCycleSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FsuCycleSummary.
        Type of Exadata Fleet Update Cycle.


        :param type: The type of this FsuCycleSummary.
        :type: str
        """
        allowed_values = ["PATCH"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def fsu_collection_id(self):
        """
        **[Required]** Gets the fsu_collection_id of this FsuCycleSummary.
        OCID identifier for the Collection ID the Exadata Fleet Update Cycle is assigned to.


        :return: The fsu_collection_id of this FsuCycleSummary.
        :rtype: str
        """
        return self._fsu_collection_id

    @fsu_collection_id.setter
    def fsu_collection_id(self, fsu_collection_id):
        """
        Sets the fsu_collection_id of this FsuCycleSummary.
        OCID identifier for the Collection ID the Exadata Fleet Update Cycle is assigned to.


        :param fsu_collection_id: The fsu_collection_id of this FsuCycleSummary.
        :type: str
        """
        self._fsu_collection_id = fsu_collection_id

    @property
    def collection_type(self):
        """
        **[Required]** Gets the collection_type of this FsuCycleSummary.
        Type of Collection this Exadata Fleet Update Cycle belongs to.

        Allowed values for this property are: "DB", "GI", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The collection_type of this FsuCycleSummary.
        :rtype: str
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        """
        Sets the collection_type of this FsuCycleSummary.
        Type of Collection this Exadata Fleet Update Cycle belongs to.


        :param collection_type: The collection_type of this FsuCycleSummary.
        :type: str
        """
        allowed_values = ["DB", "GI"]
        if not value_allowed_none_or_none_sentinel(collection_type, allowed_values):
            collection_type = 'UNKNOWN_ENUM_VALUE'
        self._collection_type = collection_type

    @property
    def executing_fsu_action_id(self):
        """
        Gets the executing_fsu_action_id of this FsuCycleSummary.
        OCID identifier for the Action that is currently in execution, if applicable.


        :return: The executing_fsu_action_id of this FsuCycleSummary.
        :rtype: str
        """
        return self._executing_fsu_action_id

    @executing_fsu_action_id.setter
    def executing_fsu_action_id(self, executing_fsu_action_id):
        """
        Sets the executing_fsu_action_id of this FsuCycleSummary.
        OCID identifier for the Action that is currently in execution, if applicable.


        :param executing_fsu_action_id: The executing_fsu_action_id of this FsuCycleSummary.
        :type: str
        """
        self._executing_fsu_action_id = executing_fsu_action_id

    @property
    def next_action_to_execute(self):
        """
        Gets the next_action_to_execute of this FsuCycleSummary.
        In this array all the possible actions will be listed. The first element is the suggested Action.


        :return: The next_action_to_execute of this FsuCycleSummary.
        :rtype: list[oci.fleet_software_update.models.NextActionToExecuteDetails]
        """
        return self._next_action_to_execute

    @next_action_to_execute.setter
    def next_action_to_execute(self, next_action_to_execute):
        """
        Sets the next_action_to_execute of this FsuCycleSummary.
        In this array all the possible actions will be listed. The first element is the suggested Action.


        :param next_action_to_execute: The next_action_to_execute of this FsuCycleSummary.
        :type: list[oci.fleet_software_update.models.NextActionToExecuteDetails]
        """
        self._next_action_to_execute = next_action_to_execute

    @property
    def last_completed_action(self):
        """
        Gets the last_completed_action of this FsuCycleSummary.
        The latest Action type that was completed in the Exadata Fleet Update Cycle.
        No value would indicate that the Cycle has not completed any Action yet.

        Allowed values for this property are: "STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_completed_action of this FsuCycleSummary.
        :rtype: str
        """
        return self._last_completed_action

    @last_completed_action.setter
    def last_completed_action(self, last_completed_action):
        """
        Sets the last_completed_action of this FsuCycleSummary.
        The latest Action type that was completed in the Exadata Fleet Update Cycle.
        No value would indicate that the Cycle has not completed any Action yet.


        :param last_completed_action: The last_completed_action of this FsuCycleSummary.
        :type: str
        """
        allowed_values = ["STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"]
        if not value_allowed_none_or_none_sentinel(last_completed_action, allowed_values):
            last_completed_action = 'UNKNOWN_ENUM_VALUE'
        self._last_completed_action = last_completed_action

    @property
    def goal_version_details(self):
        """
        **[Required]** Gets the goal_version_details of this FsuCycleSummary.

        :return: The goal_version_details of this FsuCycleSummary.
        :rtype: oci.fleet_software_update.models.FsuGoalVersionDetails
        """
        return self._goal_version_details

    @goal_version_details.setter
    def goal_version_details(self, goal_version_details):
        """
        Sets the goal_version_details of this FsuCycleSummary.

        :param goal_version_details: The goal_version_details of this FsuCycleSummary.
        :type: oci.fleet_software_update.models.FsuGoalVersionDetails
        """
        self._goal_version_details = goal_version_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FsuCycleSummary.
        The date and time the Exadata Fleet Update Cycle was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this FsuCycleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FsuCycleSummary.
        The date and time the Exadata Fleet Update Cycle was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this FsuCycleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this FsuCycleSummary.
        The date and time the Exadata Fleet Update Cycle was updated,
        as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this FsuCycleSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this FsuCycleSummary.
        The date and time the Exadata Fleet Update Cycle was updated,
        as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this FsuCycleSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_finished(self):
        """
        Gets the time_finished of this FsuCycleSummary.
        The date and time the Exadata Fleet Update Cycle was finished,
        as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this FsuCycleSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this FsuCycleSummary.
        The date and time the Exadata Fleet Update Cycle was finished,
        as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_finished: The time_finished of this FsuCycleSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FsuCycleSummary.
        The current state of the Exadata Fleet Update Cycle.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "IN_PROGRESS", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FsuCycleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FsuCycleSummary.
        The current state of the Exadata Fleet Update Cycle.


        :param lifecycle_state: The lifecycle_state of this FsuCycleSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "IN_PROGRESS", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FsuCycleSummary.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this FsuCycleSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FsuCycleSummary.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this FsuCycleSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FsuCycleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this FsuCycleSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FsuCycleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this FsuCycleSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FsuCycleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this FsuCycleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FsuCycleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this FsuCycleSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this FsuCycleSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this FsuCycleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this FsuCycleSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this FsuCycleSummary.
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

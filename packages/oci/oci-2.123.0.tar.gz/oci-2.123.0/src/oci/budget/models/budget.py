# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190111


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Budget(object):
    """
    A budget.
    """

    #: A constant which can be used with the reset_period property of a Budget.
    #: This constant has a value of "MONTHLY"
    RESET_PERIOD_MONTHLY = "MONTHLY"

    #: A constant which can be used with the processing_period_type property of a Budget.
    #: This constant has a value of "INVOICE"
    PROCESSING_PERIOD_TYPE_INVOICE = "INVOICE"

    #: A constant which can be used with the processing_period_type property of a Budget.
    #: This constant has a value of "MONTH"
    PROCESSING_PERIOD_TYPE_MONTH = "MONTH"

    #: A constant which can be used with the processing_period_type property of a Budget.
    #: This constant has a value of "SINGLE_USE"
    PROCESSING_PERIOD_TYPE_SINGLE_USE = "SINGLE_USE"

    #: A constant which can be used with the target_type property of a Budget.
    #: This constant has a value of "COMPARTMENT"
    TARGET_TYPE_COMPARTMENT = "COMPARTMENT"

    #: A constant which can be used with the target_type property of a Budget.
    #: This constant has a value of "TAG"
    TARGET_TYPE_TAG = "TAG"

    #: A constant which can be used with the lifecycle_state property of a Budget.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Budget.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new Budget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Budget.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Budget.
        :type compartment_id: str

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this Budget.
        :type target_compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Budget.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Budget.
        :type description: str

        :param amount:
            The value to assign to the amount property of this Budget.
        :type amount: float

        :param reset_period:
            The value to assign to the reset_period property of this Budget.
            Allowed values for this property are: "MONTHLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reset_period: str

        :param budget_processing_period_start_offset:
            The value to assign to the budget_processing_period_start_offset property of this Budget.
        :type budget_processing_period_start_offset: int

        :param processing_period_type:
            The value to assign to the processing_period_type property of this Budget.
            Allowed values for this property are: "INVOICE", "MONTH", "SINGLE_USE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type processing_period_type: str

        :param start_date:
            The value to assign to the start_date property of this Budget.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this Budget.
        :type end_date: datetime

        :param target_type:
            The value to assign to the target_type property of this Budget.
            Allowed values for this property are: "COMPARTMENT", "TAG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_type: str

        :param targets:
            The value to assign to the targets property of this Budget.
        :type targets: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Budget.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param alert_rule_count:
            The value to assign to the alert_rule_count property of this Budget.
        :type alert_rule_count: int

        :param version:
            The value to assign to the version property of this Budget.
        :type version: int

        :param actual_spend:
            The value to assign to the actual_spend property of this Budget.
        :type actual_spend: float

        :param forecasted_spend:
            The value to assign to the forecasted_spend property of this Budget.
        :type forecasted_spend: float

        :param time_spend_computed:
            The value to assign to the time_spend_computed property of this Budget.
        :type time_spend_computed: datetime

        :param time_created:
            The value to assign to the time_created property of this Budget.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Budget.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Budget.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Budget.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'target_compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'amount': 'float',
            'reset_period': 'str',
            'budget_processing_period_start_offset': 'int',
            'processing_period_type': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'target_type': 'str',
            'targets': 'list[str]',
            'lifecycle_state': 'str',
            'alert_rule_count': 'int',
            'version': 'int',
            'actual_spend': 'float',
            'forecasted_spend': 'float',
            'time_spend_computed': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'target_compartment_id': 'targetCompartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'amount': 'amount',
            'reset_period': 'resetPeriod',
            'budget_processing_period_start_offset': 'budgetProcessingPeriodStartOffset',
            'processing_period_type': 'processingPeriodType',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'target_type': 'targetType',
            'targets': 'targets',
            'lifecycle_state': 'lifecycleState',
            'alert_rule_count': 'alertRuleCount',
            'version': 'version',
            'actual_spend': 'actualSpend',
            'forecasted_spend': 'forecastedSpend',
            'time_spend_computed': 'timeSpendComputed',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._target_compartment_id = None
        self._display_name = None
        self._description = None
        self._amount = None
        self._reset_period = None
        self._budget_processing_period_start_offset = None
        self._processing_period_type = None
        self._start_date = None
        self._end_date = None
        self._target_type = None
        self._targets = None
        self._lifecycle_state = None
        self._alert_rule_count = None
        self._version = None
        self._actual_spend = None
        self._forecasted_spend = None
        self._time_spend_computed = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Budget.
        The OCID of the budget.


        :return: The id of this Budget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Budget.
        The OCID of the budget.


        :param id: The id of this Budget.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Budget.
        The OCID of the compartment.


        :return: The compartment_id of this Budget.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Budget.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this Budget.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_compartment_id(self):
        """
        Gets the target_compartment_id of this Budget.
        This is DEPRECATED. For backwards compatability, the property is populated when
        the targetType is \"COMPARTMENT\", and targets contain the specific target compartment OCID.
        For all other scenarios, this property will be left empty.


        :return: The target_compartment_id of this Budget.
        :rtype: str
        """
        return self._target_compartment_id

    @target_compartment_id.setter
    def target_compartment_id(self, target_compartment_id):
        """
        Sets the target_compartment_id of this Budget.
        This is DEPRECATED. For backwards compatability, the property is populated when
        the targetType is \"COMPARTMENT\", and targets contain the specific target compartment OCID.
        For all other scenarios, this property will be left empty.


        :param target_compartment_id: The target_compartment_id of this Budget.
        :type: str
        """
        self._target_compartment_id = target_compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Budget.
        The display name of the budget. Avoid entering confidential information.


        :return: The display_name of this Budget.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Budget.
        The display name of the budget. Avoid entering confidential information.


        :param display_name: The display_name of this Budget.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Budget.
        The description of the budget.


        :return: The description of this Budget.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Budget.
        The description of the budget.


        :param description: The description of this Budget.
        :type: str
        """
        self._description = description

    @property
    def amount(self):
        """
        **[Required]** Gets the amount of this Budget.
        The amount of the budget expressed in the currency of the customer's rate card.


        :return: The amount of this Budget.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Budget.
        The amount of the budget expressed in the currency of the customer's rate card.


        :param amount: The amount of this Budget.
        :type: float
        """
        self._amount = amount

    @property
    def reset_period(self):
        """
        **[Required]** Gets the reset_period of this Budget.
        The reset period for the budget.

        Allowed values for this property are: "MONTHLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reset_period of this Budget.
        :rtype: str
        """
        return self._reset_period

    @reset_period.setter
    def reset_period(self, reset_period):
        """
        Sets the reset_period of this Budget.
        The reset period for the budget.


        :param reset_period: The reset_period of this Budget.
        :type: str
        """
        allowed_values = ["MONTHLY"]
        if not value_allowed_none_or_none_sentinel(reset_period, allowed_values):
            reset_period = 'UNKNOWN_ENUM_VALUE'
        self._reset_period = reset_period

    @property
    def budget_processing_period_start_offset(self):
        """
        Gets the budget_processing_period_start_offset of this Budget.
        The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.


        :return: The budget_processing_period_start_offset of this Budget.
        :rtype: int
        """
        return self._budget_processing_period_start_offset

    @budget_processing_period_start_offset.setter
    def budget_processing_period_start_offset(self, budget_processing_period_start_offset):
        """
        Sets the budget_processing_period_start_offset of this Budget.
        The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.


        :param budget_processing_period_start_offset: The budget_processing_period_start_offset of this Budget.
        :type: int
        """
        self._budget_processing_period_start_offset = budget_processing_period_start_offset

    @property
    def processing_period_type(self):
        """
        Gets the processing_period_type of this Budget.
        The budget processing period type. Valid values are INVOICE, MONTH, and SINGLE_USE.

        Allowed values for this property are: "INVOICE", "MONTH", "SINGLE_USE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The processing_period_type of this Budget.
        :rtype: str
        """
        return self._processing_period_type

    @processing_period_type.setter
    def processing_period_type(self, processing_period_type):
        """
        Sets the processing_period_type of this Budget.
        The budget processing period type. Valid values are INVOICE, MONTH, and SINGLE_USE.


        :param processing_period_type: The processing_period_type of this Budget.
        :type: str
        """
        allowed_values = ["INVOICE", "MONTH", "SINGLE_USE"]
        if not value_allowed_none_or_none_sentinel(processing_period_type, allowed_values):
            processing_period_type = 'UNKNOWN_ENUM_VALUE'
        self._processing_period_type = processing_period_type

    @property
    def start_date(self):
        """
        Gets the start_date of this Budget.
        The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.


        :return: The start_date of this Budget.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Budget.
        The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.


        :param start_date: The start_date of this Budget.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Budget.
        The time when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.


        :return: The end_date of this Budget.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Budget.
        The time when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.


        :param end_date: The end_date of this Budget.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def target_type(self):
        """
        Gets the target_type of this Budget.
        The type of target on which the budget is applied.

        Allowed values for this property are: "COMPARTMENT", "TAG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_type of this Budget.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this Budget.
        The type of target on which the budget is applied.


        :param target_type: The target_type of this Budget.
        :type: str
        """
        allowed_values = ["COMPARTMENT", "TAG"]
        if not value_allowed_none_or_none_sentinel(target_type, allowed_values):
            target_type = 'UNKNOWN_ENUM_VALUE'
        self._target_type = target_type

    @property
    def targets(self):
        """
        Gets the targets of this Budget.
        The list of targets on which the budget is applied.
          If the targetType is \"COMPARTMENT\", the targets contain the list of compartment OCIDs.
          If the targetType is \"TAG\", the targets contain the list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\".


        :return: The targets of this Budget.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this Budget.
        The list of targets on which the budget is applied.
          If the targetType is \"COMPARTMENT\", the targets contain the list of compartment OCIDs.
          If the targetType is \"TAG\", the targets contain the list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\".


        :param targets: The targets of this Budget.
        :type: list[str]
        """
        self._targets = targets

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Budget.
        The current state of the budget.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Budget.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Budget.
        The current state of the budget.


        :param lifecycle_state: The lifecycle_state of this Budget.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def alert_rule_count(self):
        """
        **[Required]** Gets the alert_rule_count of this Budget.
        The total number of alert rules in the budget.


        :return: The alert_rule_count of this Budget.
        :rtype: int
        """
        return self._alert_rule_count

    @alert_rule_count.setter
    def alert_rule_count(self, alert_rule_count):
        """
        Sets the alert_rule_count of this Budget.
        The total number of alert rules in the budget.


        :param alert_rule_count: The alert_rule_count of this Budget.
        :type: int
        """
        self._alert_rule_count = alert_rule_count

    @property
    def version(self):
        """
        Gets the version of this Budget.
        The version of the budget. Starts from 1 and increments by 1.


        :return: The version of this Budget.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Budget.
        The version of the budget. Starts from 1 and increments by 1.


        :param version: The version of this Budget.
        :type: int
        """
        self._version = version

    @property
    def actual_spend(self):
        """
        Gets the actual_spend of this Budget.
        The actual spend in currency for the current budget cycle.


        :return: The actual_spend of this Budget.
        :rtype: float
        """
        return self._actual_spend

    @actual_spend.setter
    def actual_spend(self, actual_spend):
        """
        Sets the actual_spend of this Budget.
        The actual spend in currency for the current budget cycle.


        :param actual_spend: The actual_spend of this Budget.
        :type: float
        """
        self._actual_spend = actual_spend

    @property
    def forecasted_spend(self):
        """
        Gets the forecasted_spend of this Budget.
        The forecasted spend in currency by the end of the current budget cycle.


        :return: The forecasted_spend of this Budget.
        :rtype: float
        """
        return self._forecasted_spend

    @forecasted_spend.setter
    def forecasted_spend(self, forecasted_spend):
        """
        Sets the forecasted_spend of this Budget.
        The forecasted spend in currency by the end of the current budget cycle.


        :param forecasted_spend: The forecasted_spend of this Budget.
        :type: float
        """
        self._forecasted_spend = forecasted_spend

    @property
    def time_spend_computed(self):
        """
        Gets the time_spend_computed of this Budget.
        The time that the budget spend was last computed.


        :return: The time_spend_computed of this Budget.
        :rtype: datetime
        """
        return self._time_spend_computed

    @time_spend_computed.setter
    def time_spend_computed(self, time_spend_computed):
        """
        Sets the time_spend_computed of this Budget.
        The time that the budget spend was last computed.


        :param time_spend_computed: The time_spend_computed of this Budget.
        :type: datetime
        """
        self._time_spend_computed = time_spend_computed

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Budget.
        The time that the budget was created.


        :return: The time_created of this Budget.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Budget.
        The time that the budget was created.


        :param time_created: The time_created of this Budget.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Budget.
        The time that the budget was updated.


        :return: The time_updated of this Budget.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Budget.
        The time that the budget was updated.


        :param time_updated: The time_updated of this Budget.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Budget.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Budget.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Budget.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Budget.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Budget.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Budget.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Budget.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Budget.
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

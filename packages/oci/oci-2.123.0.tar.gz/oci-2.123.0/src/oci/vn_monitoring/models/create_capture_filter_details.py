# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCaptureFilterDetails(object):
    """
    A capture filter contains a set of rules governing what traffic a VTAP mirrors.
    """

    #: A constant which can be used with the filter_type property of a CreateCaptureFilterDetails.
    #: This constant has a value of "VTAP"
    FILTER_TYPE_VTAP = "VTAP"

    #: A constant which can be used with the filter_type property of a CreateCaptureFilterDetails.
    #: This constant has a value of "FLOWLOG"
    FILTER_TYPE_FLOWLOG = "FLOWLOG"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCaptureFilterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCaptureFilterDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCaptureFilterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateCaptureFilterDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCaptureFilterDetails.
        :type freeform_tags: dict(str, str)

        :param filter_type:
            The value to assign to the filter_type property of this CreateCaptureFilterDetails.
            Allowed values for this property are: "VTAP", "FLOWLOG"
        :type filter_type: str

        :param vtap_capture_filter_rules:
            The value to assign to the vtap_capture_filter_rules property of this CreateCaptureFilterDetails.
        :type vtap_capture_filter_rules: list[oci.vn_monitoring.models.VtapCaptureFilterRuleDetails]

        :param flow_log_capture_filter_rules:
            The value to assign to the flow_log_capture_filter_rules property of this CreateCaptureFilterDetails.
        :type flow_log_capture_filter_rules: list[oci.vn_monitoring.models.FlowLogCaptureFilterRuleDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'filter_type': 'str',
            'vtap_capture_filter_rules': 'list[VtapCaptureFilterRuleDetails]',
            'flow_log_capture_filter_rules': 'list[FlowLogCaptureFilterRuleDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'filter_type': 'filterType',
            'vtap_capture_filter_rules': 'vtapCaptureFilterRules',
            'flow_log_capture_filter_rules': 'flowLogCaptureFilterRules'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._filter_type = None
        self._vtap_capture_filter_rules = None
        self._flow_log_capture_filter_rules = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCaptureFilterDetails.
        The `OCID`__ of the compartment containing the capture filter.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCaptureFilterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCaptureFilterDetails.
        The `OCID`__ of the compartment containing the capture filter.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCaptureFilterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCaptureFilterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateCaptureFilterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCaptureFilterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateCaptureFilterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCaptureFilterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateCaptureFilterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCaptureFilterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateCaptureFilterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCaptureFilterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateCaptureFilterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCaptureFilterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateCaptureFilterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this CreateCaptureFilterDetails.
        Indicates which service will use this capture filter

        Allowed values for this property are: "VTAP", "FLOWLOG"


        :return: The filter_type of this CreateCaptureFilterDetails.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this CreateCaptureFilterDetails.
        Indicates which service will use this capture filter


        :param filter_type: The filter_type of this CreateCaptureFilterDetails.
        :type: str
        """
        allowed_values = ["VTAP", "FLOWLOG"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            raise ValueError(
                f"Invalid value for `filter_type`, must be None or one of {allowed_values}"
            )
        self._filter_type = filter_type

    @property
    def vtap_capture_filter_rules(self):
        """
        Gets the vtap_capture_filter_rules of this CreateCaptureFilterDetails.
        The set of rules governing what traffic a VTAP mirrors.


        :return: The vtap_capture_filter_rules of this CreateCaptureFilterDetails.
        :rtype: list[oci.vn_monitoring.models.VtapCaptureFilterRuleDetails]
        """
        return self._vtap_capture_filter_rules

    @vtap_capture_filter_rules.setter
    def vtap_capture_filter_rules(self, vtap_capture_filter_rules):
        """
        Sets the vtap_capture_filter_rules of this CreateCaptureFilterDetails.
        The set of rules governing what traffic a VTAP mirrors.


        :param vtap_capture_filter_rules: The vtap_capture_filter_rules of this CreateCaptureFilterDetails.
        :type: list[oci.vn_monitoring.models.VtapCaptureFilterRuleDetails]
        """
        self._vtap_capture_filter_rules = vtap_capture_filter_rules

    @property
    def flow_log_capture_filter_rules(self):
        """
        Gets the flow_log_capture_filter_rules of this CreateCaptureFilterDetails.
        The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.


        :return: The flow_log_capture_filter_rules of this CreateCaptureFilterDetails.
        :rtype: list[oci.vn_monitoring.models.FlowLogCaptureFilterRuleDetails]
        """
        return self._flow_log_capture_filter_rules

    @flow_log_capture_filter_rules.setter
    def flow_log_capture_filter_rules(self, flow_log_capture_filter_rules):
        """
        Sets the flow_log_capture_filter_rules of this CreateCaptureFilterDetails.
        The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.


        :param flow_log_capture_filter_rules: The flow_log_capture_filter_rules of this CreateCaptureFilterDetails.
        :type: list[oci.vn_monitoring.models.FlowLogCaptureFilterRuleDetails]
        """
        self._flow_log_capture_filter_rules = flow_log_capture_filter_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

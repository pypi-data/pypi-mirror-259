# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlFirewallPolicyDimensions(object):
    """
    The dimensions available for SQL Firewall policy analytics.
    """

    #: A constant which can be used with the enforcement_scope property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "ENFORCE_CONTEXT"
    ENFORCEMENT_SCOPE_ENFORCE_CONTEXT = "ENFORCE_CONTEXT"

    #: A constant which can be used with the enforcement_scope property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "ENFORCE_SQL"
    ENFORCEMENT_SCOPE_ENFORCE_SQL = "ENFORCE_SQL"

    #: A constant which can be used with the enforcement_scope property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "ENFORCE_ALL"
    ENFORCEMENT_SCOPE_ENFORCE_ALL = "ENFORCE_ALL"

    #: A constant which can be used with the violation_action property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "BLOCK"
    VIOLATION_ACTION_BLOCK = "BLOCK"

    #: A constant which can be used with the violation_action property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "OBSERVE"
    VIOLATION_ACTION_OBSERVE = "OBSERVE"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicyDimensions.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlFirewallPolicyDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param security_policy_id:
            The value to assign to the security_policy_id property of this SqlFirewallPolicyDimensions.
        :type security_policy_id: str

        :param enforcement_scope:
            The value to assign to the enforcement_scope property of this SqlFirewallPolicyDimensions.
            Allowed values for this property are: "ENFORCE_CONTEXT", "ENFORCE_SQL", "ENFORCE_ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type enforcement_scope: str

        :param violation_action:
            The value to assign to the violation_action property of this SqlFirewallPolicyDimensions.
            Allowed values for this property are: "BLOCK", "OBSERVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type violation_action: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SqlFirewallPolicyDimensions.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'security_policy_id': 'str',
            'enforcement_scope': 'str',
            'violation_action': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'security_policy_id': 'securityPolicyId',
            'enforcement_scope': 'enforcementScope',
            'violation_action': 'violationAction',
            'lifecycle_state': 'lifecycleState'
        }

        self._security_policy_id = None
        self._enforcement_scope = None
        self._violation_action = None
        self._lifecycle_state = None

    @property
    def security_policy_id(self):
        """
        Gets the security_policy_id of this SqlFirewallPolicyDimensions.
        The OCID of the security policy corresponding to the SQL Firewall policy.


        :return: The security_policy_id of this SqlFirewallPolicyDimensions.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """
        Sets the security_policy_id of this SqlFirewallPolicyDimensions.
        The OCID of the security policy corresponding to the SQL Firewall policy.


        :param security_policy_id: The security_policy_id of this SqlFirewallPolicyDimensions.
        :type: str
        """
        self._security_policy_id = security_policy_id

    @property
    def enforcement_scope(self):
        """
        Gets the enforcement_scope of this SqlFirewallPolicyDimensions.
        Specifies the SQL Firewall policy enforcement option.

        Allowed values for this property are: "ENFORCE_CONTEXT", "ENFORCE_SQL", "ENFORCE_ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The enforcement_scope of this SqlFirewallPolicyDimensions.
        :rtype: str
        """
        return self._enforcement_scope

    @enforcement_scope.setter
    def enforcement_scope(self, enforcement_scope):
        """
        Sets the enforcement_scope of this SqlFirewallPolicyDimensions.
        Specifies the SQL Firewall policy enforcement option.


        :param enforcement_scope: The enforcement_scope of this SqlFirewallPolicyDimensions.
        :type: str
        """
        allowed_values = ["ENFORCE_CONTEXT", "ENFORCE_SQL", "ENFORCE_ALL"]
        if not value_allowed_none_or_none_sentinel(enforcement_scope, allowed_values):
            enforcement_scope = 'UNKNOWN_ENUM_VALUE'
        self._enforcement_scope = enforcement_scope

    @property
    def violation_action(self):
        """
        Gets the violation_action of this SqlFirewallPolicyDimensions.
        Specifies the mode in which the SQL Firewall policy is enabled.

        Allowed values for this property are: "BLOCK", "OBSERVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The violation_action of this SqlFirewallPolicyDimensions.
        :rtype: str
        """
        return self._violation_action

    @violation_action.setter
    def violation_action(self, violation_action):
        """
        Sets the violation_action of this SqlFirewallPolicyDimensions.
        Specifies the mode in which the SQL Firewall policy is enabled.


        :param violation_action: The violation_action of this SqlFirewallPolicyDimensions.
        :type: str
        """
        allowed_values = ["BLOCK", "OBSERVE"]
        if not value_allowed_none_or_none_sentinel(violation_action, allowed_values):
            violation_action = 'UNKNOWN_ENUM_VALUE'
        self._violation_action = violation_action

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SqlFirewallPolicyDimensions.
        The current state of the SQL Firewall policy.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SqlFirewallPolicyDimensions.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SqlFirewallPolicyDimensions.
        The current state of the SQL Firewall policy.


        :param lifecycle_state: The lifecycle_state of this SqlFirewallPolicyDimensions.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

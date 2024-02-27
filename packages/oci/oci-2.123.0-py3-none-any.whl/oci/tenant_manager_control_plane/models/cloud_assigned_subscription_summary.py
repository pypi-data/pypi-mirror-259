# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401

from .assigned_subscription_summary import AssignedSubscriptionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudAssignedSubscriptionSummary(AssignedSubscriptionSummary):
    """
    Summary of assigned subscription information.
    """

    #: A constant which can be used with the lifecycle_state property of a CloudAssignedSubscriptionSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a CloudAssignedSubscriptionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CloudAssignedSubscriptionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CloudAssignedSubscriptionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CloudAssignedSubscriptionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudAssignedSubscriptionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.tenant_manager_control_plane.models.CloudAssignedSubscriptionSummary.entity_version` attribute
        of this class is ``V2`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_version:
            The value to assign to the entity_version property of this CloudAssignedSubscriptionSummary.
            Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_version: str

        :param id:
            The value to assign to the id property of this CloudAssignedSubscriptionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloudAssignedSubscriptionSummary.
        :type compartment_id: str

        :param service_name:
            The value to assign to the service_name property of this CloudAssignedSubscriptionSummary.
        :type service_name: str

        :param time_created:
            The value to assign to the time_created property of this CloudAssignedSubscriptionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CloudAssignedSubscriptionSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CloudAssignedSubscriptionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CloudAssignedSubscriptionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param subscription_number:
            The value to assign to the subscription_number property of this CloudAssignedSubscriptionSummary.
        :type subscription_number: str

        :param currency_code:
            The value to assign to the currency_code property of this CloudAssignedSubscriptionSummary.
        :type currency_code: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CloudAssignedSubscriptionSummary.
            Allowed values for this property are: "NEEDS_ATTENTION", "ACTIVE", "INACTIVE", "FAILED", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'entity_version': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'service_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'subscription_number': 'str',
            'currency_code': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'entity_version': 'entityVersion',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'service_name': 'serviceName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'subscription_number': 'subscriptionNumber',
            'currency_code': 'currencyCode',
            'lifecycle_state': 'lifecycleState'
        }

        self._entity_version = None
        self._id = None
        self._compartment_id = None
        self._service_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._subscription_number = None
        self._currency_code = None
        self._lifecycle_state = None
        self._entity_version = 'V2'

    @property
    def subscription_number(self):
        """
        **[Required]** Gets the subscription_number of this CloudAssignedSubscriptionSummary.
        Unique Oracle Cloud Subscriptions identifier that is immutable on creation.


        :return: The subscription_number of this CloudAssignedSubscriptionSummary.
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """
        Sets the subscription_number of this CloudAssignedSubscriptionSummary.
        Unique Oracle Cloud Subscriptions identifier that is immutable on creation.


        :param subscription_number: The subscription_number of this CloudAssignedSubscriptionSummary.
        :type: str
        """
        self._subscription_number = subscription_number

    @property
    def currency_code(self):
        """
        **[Required]** Gets the currency_code of this CloudAssignedSubscriptionSummary.
        Currency code. For example USD, MXN.


        :return: The currency_code of this CloudAssignedSubscriptionSummary.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CloudAssignedSubscriptionSummary.
        Currency code. For example USD, MXN.


        :param currency_code: The currency_code of this CloudAssignedSubscriptionSummary.
        :type: str
        """
        self._currency_code = currency_code

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CloudAssignedSubscriptionSummary.
        Lifecycle state of the subscription.

        Allowed values for this property are: "NEEDS_ATTENTION", "ACTIVE", "INACTIVE", "FAILED", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CloudAssignedSubscriptionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CloudAssignedSubscriptionSummary.
        Lifecycle state of the subscription.


        :param lifecycle_state: The lifecycle_state of this CloudAssignedSubscriptionSummary.
        :type: str
        """
        allowed_values = ["NEEDS_ATTENTION", "ACTIVE", "INACTIVE", "FAILED", "CREATING"]
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

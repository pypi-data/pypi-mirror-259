# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserAttributesSettingsAttributeSettings(object):
    """
    User Schema Attribute Settings
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserAttributesSettingsAttributeSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UserAttributesSettingsAttributeSettings.
        :type name: str

        :param end_user_mutability:
            The value to assign to the end_user_mutability property of this UserAttributesSettingsAttributeSettings.
        :type end_user_mutability: str

        :param end_user_mutability_canonical_values:
            The value to assign to the end_user_mutability_canonical_values property of this UserAttributesSettingsAttributeSettings.
        :type end_user_mutability_canonical_values: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'end_user_mutability': 'str',
            'end_user_mutability_canonical_values': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'end_user_mutability': 'endUserMutability',
            'end_user_mutability_canonical_values': 'endUserMutabilityCanonicalValues'
        }

        self._name = None
        self._end_user_mutability = None
        self._end_user_mutability_canonical_values = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this UserAttributesSettingsAttributeSettings.
        Fully-qualified attribute or complex mapping Name

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this UserAttributesSettingsAttributeSettings.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserAttributesSettingsAttributeSettings.
        Fully-qualified attribute or complex mapping Name

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this UserAttributesSettingsAttributeSettings.
        :type: str
        """
        self._name = name

    @property
    def end_user_mutability(self):
        """
        **[Required]** Gets the end_user_mutability of this UserAttributesSettingsAttributeSettings.
        End User mutability

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"mutabilityValues\" and attrValues.value eq \"$(endUserMutability)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The end_user_mutability of this UserAttributesSettingsAttributeSettings.
        :rtype: str
        """
        return self._end_user_mutability

    @end_user_mutability.setter
    def end_user_mutability(self, end_user_mutability):
        """
        Sets the end_user_mutability of this UserAttributesSettingsAttributeSettings.
        End User mutability

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"mutabilityValues\" and attrValues.value eq \"$(endUserMutability)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param end_user_mutability: The end_user_mutability of this UserAttributesSettingsAttributeSettings.
        :type: str
        """
        self._end_user_mutability = end_user_mutability

    @property
    def end_user_mutability_canonical_values(self):
        """
        Gets the end_user_mutability_canonical_values of this UserAttributesSettingsAttributeSettings.
        Specifies the list of User mutabilities allowed.

        **Added In:** 18.3.4

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"mutabilityValues\" and attrValues.value eq \"$(endUserMutability)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - caseExact: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The end_user_mutability_canonical_values of this UserAttributesSettingsAttributeSettings.
        :rtype: list[str]
        """
        return self._end_user_mutability_canonical_values

    @end_user_mutability_canonical_values.setter
    def end_user_mutability_canonical_values(self, end_user_mutability_canonical_values):
        """
        Sets the end_user_mutability_canonical_values of this UserAttributesSettingsAttributeSettings.
        Specifies the list of User mutabilities allowed.

        **Added In:** 18.3.4

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"mutabilityValues\" and attrValues.value eq \"$(endUserMutability)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - caseExact: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param end_user_mutability_canonical_values: The end_user_mutability_canonical_values of this UserAttributesSettingsAttributeSettings.
        :type: list[str]
        """
        self._end_user_mutability_canonical_values = end_user_mutability_canonical_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

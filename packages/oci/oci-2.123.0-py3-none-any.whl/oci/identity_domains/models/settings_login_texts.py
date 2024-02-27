# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SettingsLoginTexts(object):
    """
    Login text in different locales
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SettingsLoginTexts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this SettingsLoginTexts.
        :type value: str

        :param locale:
            The value to assign to the locale property of this SettingsLoginTexts.
        :type locale: str

        """
        self.swagger_types = {
            'value': 'str',
            'locale': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'locale': 'locale'
        }

        self._value = None
        self._locale = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SettingsLoginTexts.
        Login text

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - idcsSanitize: true
         - type: string


        :return: The value of this SettingsLoginTexts.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SettingsLoginTexts.
        Login text

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - idcsSanitize: true
         - type: string


        :param value: The value of this SettingsLoginTexts.
        :type: str
        """
        self._value = value

    @property
    def locale(self):
        """
        **[Required]** Gets the locale of this SettingsLoginTexts.
        Locale

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"locales\" and attrValues.value eq \"$(loginTexts.locale)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The locale of this SettingsLoginTexts.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this SettingsLoginTexts.
        Locale

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"locales\" and attrValues.value eq \"$(loginTexts.locale)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param locale: The locale of this SettingsLoginTexts.
        :type: str
        """
        self._locale = locale

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

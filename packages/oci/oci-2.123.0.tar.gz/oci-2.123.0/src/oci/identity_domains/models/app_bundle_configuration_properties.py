# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppBundleConfigurationProperties(object):
    """
    ConnectorBundle configuration properties

    **SCIM++ Properties:**
    - idcsCompositeKey: [name]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "Long"
    ICF_TYPE_LONG = "Long"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "String"
    ICF_TYPE_STRING = "String"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "Character"
    ICF_TYPE_CHARACTER = "Character"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "Double"
    ICF_TYPE_DOUBLE = "Double"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "Float"
    ICF_TYPE_FLOAT = "Float"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "Integer"
    ICF_TYPE_INTEGER = "Integer"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "Boolean"
    ICF_TYPE_BOOLEAN = "Boolean"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "URI"
    ICF_TYPE_URI = "URI"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "File"
    ICF_TYPE_FILE = "File"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "GuardedByteArray"
    ICF_TYPE_GUARDED_BYTE_ARRAY = "GuardedByteArray"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "GuardedString"
    ICF_TYPE_GUARDED_STRING = "GuardedString"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfLong"
    ICF_TYPE_ARRAY_OF_LONG = "ArrayOfLong"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfString"
    ICF_TYPE_ARRAY_OF_STRING = "ArrayOfString"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfCharacter"
    ICF_TYPE_ARRAY_OF_CHARACTER = "ArrayOfCharacter"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfDouble"
    ICF_TYPE_ARRAY_OF_DOUBLE = "ArrayOfDouble"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfFloat"
    ICF_TYPE_ARRAY_OF_FLOAT = "ArrayOfFloat"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfInteger"
    ICF_TYPE_ARRAY_OF_INTEGER = "ArrayOfInteger"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfBoolean"
    ICF_TYPE_ARRAY_OF_BOOLEAN = "ArrayOfBoolean"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfURI"
    ICF_TYPE_ARRAY_OF_URI = "ArrayOfURI"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfFile"
    ICF_TYPE_ARRAY_OF_FILE = "ArrayOfFile"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfGuardedByteArray"
    ICF_TYPE_ARRAY_OF_GUARDED_BYTE_ARRAY = "ArrayOfGuardedByteArray"

    #: A constant which can be used with the icf_type property of a AppBundleConfigurationProperties.
    #: This constant has a value of "ArrayOfGuardedString"
    ICF_TYPE_ARRAY_OF_GUARDED_STRING = "ArrayOfGuardedString"

    def __init__(self, **kwargs):
        """
        Initializes a new AppBundleConfigurationProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AppBundleConfigurationProperties.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this AppBundleConfigurationProperties.
        :type display_name: str

        :param icf_type:
            The value to assign to the icf_type property of this AppBundleConfigurationProperties.
            Allowed values for this property are: "Long", "String", "Character", "Double", "Float", "Integer", "Boolean", "URI", "File", "GuardedByteArray", "GuardedString", "ArrayOfLong", "ArrayOfString", "ArrayOfCharacter", "ArrayOfDouble", "ArrayOfFloat", "ArrayOfInteger", "ArrayOfBoolean", "ArrayOfURI", "ArrayOfFile", "ArrayOfGuardedByteArray", "ArrayOfGuardedString", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type icf_type: str

        :param value:
            The value to assign to the value property of this AppBundleConfigurationProperties.
        :type value: list[str]

        :param order:
            The value to assign to the order property of this AppBundleConfigurationProperties.
        :type order: int

        :param help_message:
            The value to assign to the help_message property of this AppBundleConfigurationProperties.
        :type help_message: str

        :param required:
            The value to assign to the required property of this AppBundleConfigurationProperties.
        :type required: bool

        :param confidential:
            The value to assign to the confidential property of this AppBundleConfigurationProperties.
        :type confidential: bool

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'icf_type': 'str',
            'value': 'list[str]',
            'order': 'int',
            'help_message': 'str',
            'required': 'bool',
            'confidential': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'icf_type': 'icfType',
            'value': 'value',
            'order': 'order',
            'help_message': 'helpMessage',
            'required': 'required',
            'confidential': 'confidential'
        }

        self._name = None
        self._display_name = None
        self._icf_type = None
        self._value = None
        self._order = None
        self._help_message = None
        self._required = None
        self._confidential = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AppBundleConfigurationProperties.
        Name of the bundle configuration property. This attribute maps to \\\"name\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this AppBundleConfigurationProperties.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppBundleConfigurationProperties.
        Name of the bundle configuration property. This attribute maps to \\\"name\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this AppBundleConfigurationProperties.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this AppBundleConfigurationProperties.
        Display name of the bundle configuration property. This attribute maps to \\\"displayName\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display_name of this AppBundleConfigurationProperties.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AppBundleConfigurationProperties.
        Display name of the bundle configuration property. This attribute maps to \\\"displayName\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display_name: The display_name of this AppBundleConfigurationProperties.
        :type: str
        """
        self._display_name = display_name

    @property
    def icf_type(self):
        """
        **[Required]** Gets the icf_type of this AppBundleConfigurationProperties.
        ICF data type of the bundle configuration property. This attribute maps to \\\"type\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "Long", "String", "Character", "Double", "Float", "Integer", "Boolean", "URI", "File", "GuardedByteArray", "GuardedString", "ArrayOfLong", "ArrayOfString", "ArrayOfCharacter", "ArrayOfDouble", "ArrayOfFloat", "ArrayOfInteger", "ArrayOfBoolean", "ArrayOfURI", "ArrayOfFile", "ArrayOfGuardedByteArray", "ArrayOfGuardedString", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The icf_type of this AppBundleConfigurationProperties.
        :rtype: str
        """
        return self._icf_type

    @icf_type.setter
    def icf_type(self, icf_type):
        """
        Sets the icf_type of this AppBundleConfigurationProperties.
        ICF data type of the bundle configuration property. This attribute maps to \\\"type\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param icf_type: The icf_type of this AppBundleConfigurationProperties.
        :type: str
        """
        allowed_values = ["Long", "String", "Character", "Double", "Float", "Integer", "Boolean", "URI", "File", "GuardedByteArray", "GuardedString", "ArrayOfLong", "ArrayOfString", "ArrayOfCharacter", "ArrayOfDouble", "ArrayOfFloat", "ArrayOfInteger", "ArrayOfBoolean", "ArrayOfURI", "ArrayOfFile", "ArrayOfGuardedByteArray", "ArrayOfGuardedString"]
        if not value_allowed_none_or_none_sentinel(icf_type, allowed_values):
            icf_type = 'UNKNOWN_ENUM_VALUE'
        self._icf_type = icf_type

    @property
    def value(self):
        """
        Gets the value of this AppBundleConfigurationProperties.
        Value of the bundle configuration property. This attribute maps to \\\"value\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this AppBundleConfigurationProperties.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppBundleConfigurationProperties.
        Value of the bundle configuration property. This attribute maps to \\\"value\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this AppBundleConfigurationProperties.
        :type: list[str]
        """
        self._value = value

    @property
    def order(self):
        """
        Gets the order of this AppBundleConfigurationProperties.
        Display sequence of the bundle configuration property.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The order of this AppBundleConfigurationProperties.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this AppBundleConfigurationProperties.
        Display sequence of the bundle configuration property.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :param order: The order of this AppBundleConfigurationProperties.
        :type: int
        """
        self._order = order

    @property
    def help_message(self):
        """
        Gets the help_message of this AppBundleConfigurationProperties.
        Help message of the bundle configuration property. This attribute maps to \\\"helpMessage\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The help_message of this AppBundleConfigurationProperties.
        :rtype: str
        """
        return self._help_message

    @help_message.setter
    def help_message(self, help_message):
        """
        Sets the help_message of this AppBundleConfigurationProperties.
        Help message of the bundle configuration property. This attribute maps to \\\"helpMessage\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param help_message: The help_message of this AppBundleConfigurationProperties.
        :type: str
        """
        self._help_message = help_message

    @property
    def required(self):
        """
        **[Required]** Gets the required of this AppBundleConfigurationProperties.
        If true, this bundle configuration property is required to connect to the target connected managed app. This attribute maps to \\\"isRequired\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The required of this AppBundleConfigurationProperties.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this AppBundleConfigurationProperties.
        If true, this bundle configuration property is required to connect to the target connected managed app. This attribute maps to \\\"isRequired\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param required: The required of this AppBundleConfigurationProperties.
        :type: bool
        """
        self._required = required

    @property
    def confidential(self):
        """
        Gets the confidential of this AppBundleConfigurationProperties.
        If true, this bundle configuration property value is confidential and will be encrypted in Oracle Identity Cloud Service. This attribute maps to \\\"isConfidential\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The confidential of this AppBundleConfigurationProperties.
        :rtype: bool
        """
        return self._confidential

    @confidential.setter
    def confidential(self, confidential):
        """
        Sets the confidential of this AppBundleConfigurationProperties.
        If true, this bundle configuration property value is confidential and will be encrypted in Oracle Identity Cloud Service. This attribute maps to \\\"isConfidential\\\" attribute in \\\"ConfigurationProperty\\\" in ICF.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param confidential: The confidential of this AppBundleConfigurationProperties.
        :type: bool
        """
        self._confidential = confidential

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

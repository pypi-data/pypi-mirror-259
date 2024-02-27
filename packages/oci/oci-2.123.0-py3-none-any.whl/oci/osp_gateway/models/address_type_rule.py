# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddressTypeRule(object):
    """
    Address type rule information
    """

    #: A constant which can be used with the third_party_validation property of a AddressTypeRule.
    #: This constant has a value of "OPTIONAL"
    THIRD_PARTY_VALIDATION_OPTIONAL = "OPTIONAL"

    #: A constant which can be used with the third_party_validation property of a AddressTypeRule.
    #: This constant has a value of "REQUIRED"
    THIRD_PARTY_VALIDATION_REQUIRED = "REQUIRED"

    #: A constant which can be used with the third_party_validation property of a AddressTypeRule.
    #: This constant has a value of "NEVER"
    THIRD_PARTY_VALIDATION_NEVER = "NEVER"

    def __init__(self, **kwargs):
        """
        Initializes a new AddressTypeRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param third_party_validation:
            The value to assign to the third_party_validation property of this AddressTypeRule.
            Allowed values for this property are: "OPTIONAL", "REQUIRED", "NEVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type third_party_validation: str

        :param fields:
            The value to assign to the fields property of this AddressTypeRule.
        :type fields: list[oci.osp_gateway.models.Field]

        """
        self.swagger_types = {
            'third_party_validation': 'str',
            'fields': 'list[Field]'
        }

        self.attribute_map = {
            'third_party_validation': 'thirdPartyValidation',
            'fields': 'fields'
        }

        self._third_party_validation = None
        self._fields = None

    @property
    def third_party_validation(self):
        """
        Gets the third_party_validation of this AddressTypeRule.
        Third party validation.

        Allowed values for this property are: "OPTIONAL", "REQUIRED", "NEVER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The third_party_validation of this AddressTypeRule.
        :rtype: str
        """
        return self._third_party_validation

    @third_party_validation.setter
    def third_party_validation(self, third_party_validation):
        """
        Sets the third_party_validation of this AddressTypeRule.
        Third party validation.


        :param third_party_validation: The third_party_validation of this AddressTypeRule.
        :type: str
        """
        allowed_values = ["OPTIONAL", "REQUIRED", "NEVER"]
        if not value_allowed_none_or_none_sentinel(third_party_validation, allowed_values):
            third_party_validation = 'UNKNOWN_ENUM_VALUE'
        self._third_party_validation = third_party_validation

    @property
    def fields(self):
        """
        **[Required]** Gets the fields of this AddressTypeRule.
        Address type rule fields


        :return: The fields of this AddressTypeRule.
        :rtype: list[oci.osp_gateway.models.Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this AddressTypeRule.
        Address type rule fields


        :param fields: The fields of this AddressTypeRule.
        :type: list[oci.osp_gateway.models.Field]
        """
        self._fields = fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

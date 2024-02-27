# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovalWorkflowAssignmentApprovalWorkflow(object):
    """
    Details of the Approval Workflow

    **SCIM++ Properties:**
    - caseExact: true
    - idcsSearchable: true
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the type property of a ApprovalWorkflowAssignmentApprovalWorkflow.
    #: This constant has a value of "ApprovalWorkflow"
    TYPE_APPROVAL_WORKFLOW = "ApprovalWorkflow"

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovalWorkflowAssignmentApprovalWorkflow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type value: str

        :param ocid:
            The value to assign to the ocid property of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type ocid: str

        :param type:
            The value to assign to the type property of this ApprovalWorkflowAssignmentApprovalWorkflow.
            Allowed values for this property are: "ApprovalWorkflow", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display:
            The value to assign to the display property of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type display: str

        :param ref:
            The value to assign to the ref property of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type ref: str

        """
        self.swagger_types = {
            'value': 'str',
            'ocid': 'str',
            'type': 'str',
            'display': 'str',
            'ref': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ocid': 'ocid',
            'type': 'type',
            'display': 'display',
            'ref': '$ref'
        }

        self._value = None
        self._ocid = None
        self._type = None
        self._display = None
        self._ref = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Identifier of the approval workflow

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Identifier of the approval workflow

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type: str
        """
        self._value = value

    @property
    def ocid(self):
        """
        Gets the ocid of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Unique OCI Identifier of the approval workflow

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The ocid of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Unique OCI Identifier of the approval workflow

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type: str
        """
        self._ocid = ocid

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Indicates type of the entity that is associated with this assignment (for ARM validation)

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - idcsDefaultValue: ApprovalWorkflow
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for this property are: "ApprovalWorkflow", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Indicates type of the entity that is associated with this assignment (for ARM validation)

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - idcsDefaultValue: ApprovalWorkflow
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: request
         - type: string
         - uniqueness: none


        :param type: The type of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type: str
        """
        allowed_values = ["ApprovalWorkflow"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display(self):
        """
        Gets the display of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Display name of the approval workflow

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The display of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this ApprovalWorkflowAssignmentApprovalWorkflow.
        Display name of the approval workflow

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param display: The display of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type: str
        """
        self._display = display

    @property
    def ref(self):
        """
        Gets the ref of this ApprovalWorkflowAssignmentApprovalWorkflow.
        URI of the approval workflow

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: reference
         - uniqueness: none


        :return: The ref of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this ApprovalWorkflowAssignmentApprovalWorkflow.
        URI of the approval workflow

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: reference
         - uniqueness: none


        :param ref: The ref of this ApprovalWorkflowAssignmentApprovalWorkflow.
        :type: str
        """
        self._ref = ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

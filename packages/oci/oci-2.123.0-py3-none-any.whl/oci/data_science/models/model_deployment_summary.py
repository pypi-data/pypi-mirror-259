# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelDeploymentSummary(object):
    """
    Summary information for a model deployment.
    """

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ModelDeploymentSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new ModelDeploymentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ModelDeploymentSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this ModelDeploymentSummary.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this ModelDeploymentSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ModelDeploymentSummary.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this ModelDeploymentSummary.
        :type project_id: str

        :param created_by:
            The value to assign to the created_by property of this ModelDeploymentSummary.
        :type created_by: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ModelDeploymentSummary.
        :type compartment_id: str

        :param model_deployment_configuration_details:
            The value to assign to the model_deployment_configuration_details property of this ModelDeploymentSummary.
        :type model_deployment_configuration_details: oci.data_science.models.ModelDeploymentConfigurationDetails

        :param category_log_details:
            The value to assign to the category_log_details property of this ModelDeploymentSummary.
        :type category_log_details: oci.data_science.models.CategoryLogDetails

        :param model_deployment_url:
            The value to assign to the model_deployment_url property of this ModelDeploymentSummary.
        :type model_deployment_url: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ModelDeploymentSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "FAILED", "INACTIVE", "UPDATING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ModelDeploymentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ModelDeploymentSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'created_by': 'str',
            'compartment_id': 'str',
            'model_deployment_configuration_details': 'ModelDeploymentConfigurationDetails',
            'category_log_details': 'CategoryLogDetails',
            'model_deployment_url': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'created_by': 'createdBy',
            'compartment_id': 'compartmentId',
            'model_deployment_configuration_details': 'modelDeploymentConfigurationDetails',
            'category_log_details': 'categoryLogDetails',
            'model_deployment_url': 'modelDeploymentUrl',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._time_created = None
        self._display_name = None
        self._description = None
        self._project_id = None
        self._created_by = None
        self._compartment_id = None
        self._model_deployment_configuration_details = None
        self._category_log_details = None
        self._model_deployment_url = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ModelDeploymentSummary.
        The `OCID`__ of the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelDeploymentSummary.
        The `OCID`__ of the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ModelDeploymentSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ModelDeploymentSummary.
        The date and time the resource was created, in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ModelDeploymentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ModelDeploymentSummary.
        The date and time the resource was created, in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ModelDeploymentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ModelDeploymentSummary.
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
        Example: `My ModelDeployment`


        :return: The display_name of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ModelDeploymentSummary.
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
        Example: `My ModelDeployment`


        :param display_name: The display_name of this ModelDeploymentSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ModelDeploymentSummary.
        A short description of the model deployment.


        :return: The description of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModelDeploymentSummary.
        A short description of the model deployment.


        :param description: The description of this ModelDeploymentSummary.
        :type: str
        """
        self._description = description

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this ModelDeploymentSummary.
        The `OCID`__ of the project associated with the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this ModelDeploymentSummary.
        The `OCID`__ of the project associated with the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this ModelDeploymentSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ModelDeploymentSummary.
        The `OCID`__ of the user who created the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ModelDeploymentSummary.
        The `OCID`__ of the user who created the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this ModelDeploymentSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ModelDeploymentSummary.
        The `OCID`__ of the model deployment's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ModelDeploymentSummary.
        The `OCID`__ of the model deployment's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ModelDeploymentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def model_deployment_configuration_details(self):
        """
        Gets the model_deployment_configuration_details of this ModelDeploymentSummary.

        :return: The model_deployment_configuration_details of this ModelDeploymentSummary.
        :rtype: oci.data_science.models.ModelDeploymentConfigurationDetails
        """
        return self._model_deployment_configuration_details

    @model_deployment_configuration_details.setter
    def model_deployment_configuration_details(self, model_deployment_configuration_details):
        """
        Sets the model_deployment_configuration_details of this ModelDeploymentSummary.

        :param model_deployment_configuration_details: The model_deployment_configuration_details of this ModelDeploymentSummary.
        :type: oci.data_science.models.ModelDeploymentConfigurationDetails
        """
        self._model_deployment_configuration_details = model_deployment_configuration_details

    @property
    def category_log_details(self):
        """
        Gets the category_log_details of this ModelDeploymentSummary.

        :return: The category_log_details of this ModelDeploymentSummary.
        :rtype: oci.data_science.models.CategoryLogDetails
        """
        return self._category_log_details

    @category_log_details.setter
    def category_log_details(self, category_log_details):
        """
        Sets the category_log_details of this ModelDeploymentSummary.

        :param category_log_details: The category_log_details of this ModelDeploymentSummary.
        :type: oci.data_science.models.CategoryLogDetails
        """
        self._category_log_details = category_log_details

    @property
    def model_deployment_url(self):
        """
        **[Required]** Gets the model_deployment_url of this ModelDeploymentSummary.
        The URL to interact with the model deployment.


        :return: The model_deployment_url of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._model_deployment_url

    @model_deployment_url.setter
    def model_deployment_url(self, model_deployment_url):
        """
        Sets the model_deployment_url of this ModelDeploymentSummary.
        The URL to interact with the model deployment.


        :param model_deployment_url: The model_deployment_url of this ModelDeploymentSummary.
        :type: str
        """
        self._model_deployment_url = model_deployment_url

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ModelDeploymentSummary.
        The state of the model deployment.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "FAILED", "INACTIVE", "UPDATING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ModelDeploymentSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ModelDeploymentSummary.
        The state of the model deployment.


        :param lifecycle_state: The lifecycle_state of this ModelDeploymentSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "FAILED", "INACTIVE", "UPDATING", "DELETED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ModelDeploymentSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ModelDeploymentSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ModelDeploymentSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ModelDeploymentSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ModelDeploymentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ModelDeploymentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ModelDeploymentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ModelDeploymentSummary.
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

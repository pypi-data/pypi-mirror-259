# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .artifact import Artifact
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerImageArtifact(Artifact):
    """
    Container Image artifact details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerImageArtifact object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.ContainerImageArtifact.artifact_type` attribute
        of this class is ``CONTAINER_IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ContainerImageArtifact.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ContainerImageArtifact.
        :type display_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this ContainerImageArtifact.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART"
        :type artifact_type: str

        :param status:
            The value to assign to the status property of this ContainerImageArtifact.
            Allowed values for this property are: "IN_PROGRESS", "AVAILABLE", "UNAVAILABLE"
        :type status: str

        :param status_notes:
            The value to assign to the status_notes property of this ContainerImageArtifact.
        :type status_notes: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerImageArtifact.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ContainerImageArtifact.
        :type time_created: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerImageArtifact.
        :type compartment_id: str

        :param publisher_id:
            The value to assign to the publisher_id property of this ContainerImageArtifact.
        :type publisher_id: str

        :param time_updated:
            The value to assign to the time_updated property of this ContainerImageArtifact.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ContainerImageArtifact.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ContainerImageArtifact.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ContainerImageArtifact.
        :type system_tags: dict(str, dict(str, object))

        :param container_image:
            The value to assign to the container_image property of this ContainerImageArtifact.
        :type container_image: oci.marketplace_publisher.models.ContainerImageDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'artifact_type': 'str',
            'status': 'str',
            'status_notes': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'compartment_id': 'str',
            'publisher_id': 'str',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'container_image': 'ContainerImageDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'artifact_type': 'artifactType',
            'status': 'status',
            'status_notes': 'statusNotes',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'compartment_id': 'compartmentId',
            'publisher_id': 'publisherId',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'container_image': 'containerImage'
        }

        self._id = None
        self._display_name = None
        self._artifact_type = None
        self._status = None
        self._status_notes = None
        self._lifecycle_state = None
        self._time_created = None
        self._compartment_id = None
        self._publisher_id = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._container_image = None
        self._artifact_type = 'CONTAINER_IMAGE'

    @property
    def container_image(self):
        """
        **[Required]** Gets the container_image of this ContainerImageArtifact.

        :return: The container_image of this ContainerImageArtifact.
        :rtype: oci.marketplace_publisher.models.ContainerImageDetails
        """
        return self._container_image

    @container_image.setter
    def container_image(self, container_image):
        """
        Sets the container_image of this ContainerImageArtifact.

        :param container_image: The container_image of this ContainerImageArtifact.
        :type: oci.marketplace_publisher.models.ContainerImageDetails
        """
        self._container_image = container_image

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

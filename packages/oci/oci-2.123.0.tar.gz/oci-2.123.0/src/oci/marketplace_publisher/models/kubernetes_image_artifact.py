# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .artifact import Artifact
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KubernetesImageArtifact(Artifact):
    """
    Kubernetes HelmChart Image artifact details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KubernetesImageArtifact object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.KubernetesImageArtifact.artifact_type` attribute
        of this class is ``HELM_CHART`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this KubernetesImageArtifact.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this KubernetesImageArtifact.
        :type display_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this KubernetesImageArtifact.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART"
        :type artifact_type: str

        :param status:
            The value to assign to the status property of this KubernetesImageArtifact.
            Allowed values for this property are: "IN_PROGRESS", "AVAILABLE", "UNAVAILABLE"
        :type status: str

        :param status_notes:
            The value to assign to the status_notes property of this KubernetesImageArtifact.
        :type status_notes: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this KubernetesImageArtifact.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this KubernetesImageArtifact.
        :type time_created: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this KubernetesImageArtifact.
        :type compartment_id: str

        :param publisher_id:
            The value to assign to the publisher_id property of this KubernetesImageArtifact.
        :type publisher_id: str

        :param time_updated:
            The value to assign to the time_updated property of this KubernetesImageArtifact.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this KubernetesImageArtifact.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this KubernetesImageArtifact.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this KubernetesImageArtifact.
        :type system_tags: dict(str, dict(str, object))

        :param helm_chart:
            The value to assign to the helm_chart property of this KubernetesImageArtifact.
        :type helm_chart: oci.marketplace_publisher.models.HelmChartImageDetails

        :param container_image_artifact_ids:
            The value to assign to the container_image_artifact_ids property of this KubernetesImageArtifact.
        :type container_image_artifact_ids: list[str]

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
            'helm_chart': 'HelmChartImageDetails',
            'container_image_artifact_ids': 'list[str]'
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
            'helm_chart': 'helmChart',
            'container_image_artifact_ids': 'containerImageArtifactIds'
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
        self._helm_chart = None
        self._container_image_artifact_ids = None
        self._artifact_type = 'HELM_CHART'

    @property
    def helm_chart(self):
        """
        **[Required]** Gets the helm_chart of this KubernetesImageArtifact.

        :return: The helm_chart of this KubernetesImageArtifact.
        :rtype: oci.marketplace_publisher.models.HelmChartImageDetails
        """
        return self._helm_chart

    @helm_chart.setter
    def helm_chart(self, helm_chart):
        """
        Sets the helm_chart of this KubernetesImageArtifact.

        :param helm_chart: The helm_chart of this KubernetesImageArtifact.
        :type: oci.marketplace_publisher.models.HelmChartImageDetails
        """
        self._helm_chart = helm_chart

    @property
    def container_image_artifact_ids(self):
        """
        Gets the container_image_artifact_ids of this KubernetesImageArtifact.
        List of container image artifact unique identifiers included in the helm chart.


        :return: The container_image_artifact_ids of this KubernetesImageArtifact.
        :rtype: list[str]
        """
        return self._container_image_artifact_ids

    @container_image_artifact_ids.setter
    def container_image_artifact_ids(self, container_image_artifact_ids):
        """
        Sets the container_image_artifact_ids of this KubernetesImageArtifact.
        List of container image artifact unique identifiers included in the helm chart.


        :param container_image_artifact_ids: The container_image_artifact_ids of this KubernetesImageArtifact.
        :type: list[str]
        """
        self._container_image_artifact_ids = container_image_artifact_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

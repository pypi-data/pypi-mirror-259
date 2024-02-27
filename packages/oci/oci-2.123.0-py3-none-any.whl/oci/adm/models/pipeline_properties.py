# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineProperties(object):
    """
    Pipeline properties which result from the run of the verify stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pipeline_identifier:
            The value to assign to the pipeline_identifier property of this PipelineProperties.
        :type pipeline_identifier: str

        :param pipeline_url:
            The value to assign to the pipeline_url property of this PipelineProperties.
        :type pipeline_url: str

        """
        self.swagger_types = {
            'pipeline_identifier': 'str',
            'pipeline_url': 'str'
        }

        self.attribute_map = {
            'pipeline_identifier': 'pipelineIdentifier',
            'pipeline_url': 'pipelineUrl'
        }

        self._pipeline_identifier = None
        self._pipeline_url = None

    @property
    def pipeline_identifier(self):
        """
        Gets the pipeline_identifier of this PipelineProperties.
        Unique identifier for the pipeline or action created in the Verify stage.


        :return: The pipeline_identifier of this PipelineProperties.
        :rtype: str
        """
        return self._pipeline_identifier

    @pipeline_identifier.setter
    def pipeline_identifier(self, pipeline_identifier):
        """
        Sets the pipeline_identifier of this PipelineProperties.
        Unique identifier for the pipeline or action created in the Verify stage.


        :param pipeline_identifier: The pipeline_identifier of this PipelineProperties.
        :type: str
        """
        self._pipeline_identifier = pipeline_identifier

    @property
    def pipeline_url(self):
        """
        Gets the pipeline_url of this PipelineProperties.
        The web link to the pipeline from the Verify stage.


        :return: The pipeline_url of this PipelineProperties.
        :rtype: str
        """
        return self._pipeline_url

    @pipeline_url.setter
    def pipeline_url(self, pipeline_url):
        """
        Sets the pipeline_url of this PipelineProperties.
        The web link to the pipeline from the Verify stage.


        :param pipeline_url: The pipeline_url of this PipelineProperties.
        :type: str
        """
        self._pipeline_url = pipeline_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

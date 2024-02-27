# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .training_config import TrainingConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VanillaTrainingConfig(TrainingConfig):
    """
    The Vanilla training method hyperparameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VanillaTrainingConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai.models.VanillaTrainingConfig.training_config_type` attribute
        of this class is ``VANILLA_TRAINING_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param training_config_type:
            The value to assign to the training_config_type property of this VanillaTrainingConfig.
            Allowed values for this property are: "TFEW_TRAINING_CONFIG", "VANILLA_TRAINING_CONFIG"
        :type training_config_type: str

        :param total_training_epochs:
            The value to assign to the total_training_epochs property of this VanillaTrainingConfig.
        :type total_training_epochs: int

        :param learning_rate:
            The value to assign to the learning_rate property of this VanillaTrainingConfig.
        :type learning_rate: float

        :param training_batch_size:
            The value to assign to the training_batch_size property of this VanillaTrainingConfig.
        :type training_batch_size: int

        :param early_stopping_patience:
            The value to assign to the early_stopping_patience property of this VanillaTrainingConfig.
        :type early_stopping_patience: int

        :param early_stopping_threshold:
            The value to assign to the early_stopping_threshold property of this VanillaTrainingConfig.
        :type early_stopping_threshold: float

        :param log_model_metrics_interval_in_steps:
            The value to assign to the log_model_metrics_interval_in_steps property of this VanillaTrainingConfig.
        :type log_model_metrics_interval_in_steps: int

        :param num_of_last_layers:
            The value to assign to the num_of_last_layers property of this VanillaTrainingConfig.
        :type num_of_last_layers: int

        """
        self.swagger_types = {
            'training_config_type': 'str',
            'total_training_epochs': 'int',
            'learning_rate': 'float',
            'training_batch_size': 'int',
            'early_stopping_patience': 'int',
            'early_stopping_threshold': 'float',
            'log_model_metrics_interval_in_steps': 'int',
            'num_of_last_layers': 'int'
        }

        self.attribute_map = {
            'training_config_type': 'trainingConfigType',
            'total_training_epochs': 'totalTrainingEpochs',
            'learning_rate': 'learningRate',
            'training_batch_size': 'trainingBatchSize',
            'early_stopping_patience': 'earlyStoppingPatience',
            'early_stopping_threshold': 'earlyStoppingThreshold',
            'log_model_metrics_interval_in_steps': 'logModelMetricsIntervalInSteps',
            'num_of_last_layers': 'numOfLastLayers'
        }

        self._training_config_type = None
        self._total_training_epochs = None
        self._learning_rate = None
        self._training_batch_size = None
        self._early_stopping_patience = None
        self._early_stopping_threshold = None
        self._log_model_metrics_interval_in_steps = None
        self._num_of_last_layers = None
        self._training_config_type = 'VANILLA_TRAINING_CONFIG'

    @property
    def num_of_last_layers(self):
        """
        Gets the num_of_last_layers of this VanillaTrainingConfig.
        The number of last layers to be fine-tuned.


        :return: The num_of_last_layers of this VanillaTrainingConfig.
        :rtype: int
        """
        return self._num_of_last_layers

    @num_of_last_layers.setter
    def num_of_last_layers(self, num_of_last_layers):
        """
        Sets the num_of_last_layers of this VanillaTrainingConfig.
        The number of last layers to be fine-tuned.


        :param num_of_last_layers: The num_of_last_layers of this VanillaTrainingConfig.
        :type: int
        """
        self._num_of_last_layers = num_of_last_layers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

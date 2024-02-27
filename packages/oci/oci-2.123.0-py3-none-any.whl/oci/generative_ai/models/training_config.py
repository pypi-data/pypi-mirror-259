# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrainingConfig(object):
    """
    The fine-tuning method and hyperparameters used for fine-tuning a custom model.
    """

    #: A constant which can be used with the training_config_type property of a TrainingConfig.
    #: This constant has a value of "TFEW_TRAINING_CONFIG"
    TRAINING_CONFIG_TYPE_TFEW_TRAINING_CONFIG = "TFEW_TRAINING_CONFIG"

    #: A constant which can be used with the training_config_type property of a TrainingConfig.
    #: This constant has a value of "VANILLA_TRAINING_CONFIG"
    TRAINING_CONFIG_TYPE_VANILLA_TRAINING_CONFIG = "VANILLA_TRAINING_CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new TrainingConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai.models.VanillaTrainingConfig`
        * :class:`~oci.generative_ai.models.TFewTrainingConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param training_config_type:
            The value to assign to the training_config_type property of this TrainingConfig.
            Allowed values for this property are: "TFEW_TRAINING_CONFIG", "VANILLA_TRAINING_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type training_config_type: str

        :param total_training_epochs:
            The value to assign to the total_training_epochs property of this TrainingConfig.
        :type total_training_epochs: int

        :param learning_rate:
            The value to assign to the learning_rate property of this TrainingConfig.
        :type learning_rate: float

        :param training_batch_size:
            The value to assign to the training_batch_size property of this TrainingConfig.
        :type training_batch_size: int

        :param early_stopping_patience:
            The value to assign to the early_stopping_patience property of this TrainingConfig.
        :type early_stopping_patience: int

        :param early_stopping_threshold:
            The value to assign to the early_stopping_threshold property of this TrainingConfig.
        :type early_stopping_threshold: float

        :param log_model_metrics_interval_in_steps:
            The value to assign to the log_model_metrics_interval_in_steps property of this TrainingConfig.
        :type log_model_metrics_interval_in_steps: int

        """
        self.swagger_types = {
            'training_config_type': 'str',
            'total_training_epochs': 'int',
            'learning_rate': 'float',
            'training_batch_size': 'int',
            'early_stopping_patience': 'int',
            'early_stopping_threshold': 'float',
            'log_model_metrics_interval_in_steps': 'int'
        }

        self.attribute_map = {
            'training_config_type': 'trainingConfigType',
            'total_training_epochs': 'totalTrainingEpochs',
            'learning_rate': 'learningRate',
            'training_batch_size': 'trainingBatchSize',
            'early_stopping_patience': 'earlyStoppingPatience',
            'early_stopping_threshold': 'earlyStoppingThreshold',
            'log_model_metrics_interval_in_steps': 'logModelMetricsIntervalInSteps'
        }

        self._training_config_type = None
        self._total_training_epochs = None
        self._learning_rate = None
        self._training_batch_size = None
        self._early_stopping_patience = None
        self._early_stopping_threshold = None
        self._log_model_metrics_interval_in_steps = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['trainingConfigType']

        if type == 'VANILLA_TRAINING_CONFIG':
            return 'VanillaTrainingConfig'

        if type == 'TFEW_TRAINING_CONFIG':
            return 'TFewTrainingConfig'
        else:
            return 'TrainingConfig'

    @property
    def training_config_type(self):
        """
        **[Required]** Gets the training_config_type of this TrainingConfig.
        The fine-tuning method for training a custom model.

        Allowed values for this property are: "TFEW_TRAINING_CONFIG", "VANILLA_TRAINING_CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The training_config_type of this TrainingConfig.
        :rtype: str
        """
        return self._training_config_type

    @training_config_type.setter
    def training_config_type(self, training_config_type):
        """
        Sets the training_config_type of this TrainingConfig.
        The fine-tuning method for training a custom model.


        :param training_config_type: The training_config_type of this TrainingConfig.
        :type: str
        """
        allowed_values = ["TFEW_TRAINING_CONFIG", "VANILLA_TRAINING_CONFIG"]
        if not value_allowed_none_or_none_sentinel(training_config_type, allowed_values):
            training_config_type = 'UNKNOWN_ENUM_VALUE'
        self._training_config_type = training_config_type

    @property
    def total_training_epochs(self):
        """
        Gets the total_training_epochs of this TrainingConfig.
        The maximum number of training epochs to run for.


        :return: The total_training_epochs of this TrainingConfig.
        :rtype: int
        """
        return self._total_training_epochs

    @total_training_epochs.setter
    def total_training_epochs(self, total_training_epochs):
        """
        Sets the total_training_epochs of this TrainingConfig.
        The maximum number of training epochs to run for.


        :param total_training_epochs: The total_training_epochs of this TrainingConfig.
        :type: int
        """
        self._total_training_epochs = total_training_epochs

    @property
    def learning_rate(self):
        """
        Gets the learning_rate of this TrainingConfig.
        The initial learning rate to be used during training


        :return: The learning_rate of this TrainingConfig.
        :rtype: float
        """
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """
        Sets the learning_rate of this TrainingConfig.
        The initial learning rate to be used during training


        :param learning_rate: The learning_rate of this TrainingConfig.
        :type: float
        """
        self._learning_rate = learning_rate

    @property
    def training_batch_size(self):
        """
        Gets the training_batch_size of this TrainingConfig.
        The batch size used during training.


        :return: The training_batch_size of this TrainingConfig.
        :rtype: int
        """
        return self._training_batch_size

    @training_batch_size.setter
    def training_batch_size(self, training_batch_size):
        """
        Sets the training_batch_size of this TrainingConfig.
        The batch size used during training.


        :param training_batch_size: The training_batch_size of this TrainingConfig.
        :type: int
        """
        self._training_batch_size = training_batch_size

    @property
    def early_stopping_patience(self):
        """
        Gets the early_stopping_patience of this TrainingConfig.
        Stop training if the loss metric does not improve beyond 'early_stopping_threshold' for this many times of evaluation.


        :return: The early_stopping_patience of this TrainingConfig.
        :rtype: int
        """
        return self._early_stopping_patience

    @early_stopping_patience.setter
    def early_stopping_patience(self, early_stopping_patience):
        """
        Sets the early_stopping_patience of this TrainingConfig.
        Stop training if the loss metric does not improve beyond 'early_stopping_threshold' for this many times of evaluation.


        :param early_stopping_patience: The early_stopping_patience of this TrainingConfig.
        :type: int
        """
        self._early_stopping_patience = early_stopping_patience

    @property
    def early_stopping_threshold(self):
        """
        Gets the early_stopping_threshold of this TrainingConfig.
        How much the loss must improve to prevent early stopping.


        :return: The early_stopping_threshold of this TrainingConfig.
        :rtype: float
        """
        return self._early_stopping_threshold

    @early_stopping_threshold.setter
    def early_stopping_threshold(self, early_stopping_threshold):
        """
        Sets the early_stopping_threshold of this TrainingConfig.
        How much the loss must improve to prevent early stopping.


        :param early_stopping_threshold: The early_stopping_threshold of this TrainingConfig.
        :type: float
        """
        self._early_stopping_threshold = early_stopping_threshold

    @property
    def log_model_metrics_interval_in_steps(self):
        """
        Gets the log_model_metrics_interval_in_steps of this TrainingConfig.
        Determines how frequently to log model metrics.

        Every step is logged for the first 20 steps and then follows this parameter for log frequency. Set to 0 to disable logging the model metrics.


        :return: The log_model_metrics_interval_in_steps of this TrainingConfig.
        :rtype: int
        """
        return self._log_model_metrics_interval_in_steps

    @log_model_metrics_interval_in_steps.setter
    def log_model_metrics_interval_in_steps(self, log_model_metrics_interval_in_steps):
        """
        Sets the log_model_metrics_interval_in_steps of this TrainingConfig.
        Determines how frequently to log model metrics.

        Every step is logged for the first 20 steps and then follows this parameter for log frequency. Set to 0 to disable logging the model metrics.


        :param log_model_metrics_interval_in_steps: The log_model_metrics_interval_in_steps of this TrainingConfig.
        :type: int
        """
        self._log_model_metrics_interval_in_steps = log_model_metrics_interval_in_steps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

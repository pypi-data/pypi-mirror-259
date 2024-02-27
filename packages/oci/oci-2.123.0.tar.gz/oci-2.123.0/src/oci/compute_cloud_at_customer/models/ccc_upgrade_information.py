# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221208


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CccUpgradeInformation(object):
    """
    Upgrade information that relates to a Compute Cloud@Customer infrastructure. This information
    cannot be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CccUpgradeInformation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_version:
            The value to assign to the current_version property of this CccUpgradeInformation.
        :type current_version: str

        :param time_of_scheduled_upgrade:
            The value to assign to the time_of_scheduled_upgrade property of this CccUpgradeInformation.
        :type time_of_scheduled_upgrade: datetime

        :param scheduled_upgrade_duration:
            The value to assign to the scheduled_upgrade_duration property of this CccUpgradeInformation.
        :type scheduled_upgrade_duration: str

        :param is_active:
            The value to assign to the is_active property of this CccUpgradeInformation.
        :type is_active: bool

        """
        self.swagger_types = {
            'current_version': 'str',
            'time_of_scheduled_upgrade': 'datetime',
            'scheduled_upgrade_duration': 'str',
            'is_active': 'bool'
        }

        self.attribute_map = {
            'current_version': 'currentVersion',
            'time_of_scheduled_upgrade': 'timeOfScheduledUpgrade',
            'scheduled_upgrade_duration': 'scheduledUpgradeDuration',
            'is_active': 'isActive'
        }

        self._current_version = None
        self._time_of_scheduled_upgrade = None
        self._scheduled_upgrade_duration = None
        self._is_active = None

    @property
    def current_version(self):
        """
        Gets the current_version of this CccUpgradeInformation.
        The current version of software installed on the Compute Cloud@Customer infrastructure.


        :return: The current_version of this CccUpgradeInformation.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """
        Sets the current_version of this CccUpgradeInformation.
        The current version of software installed on the Compute Cloud@Customer infrastructure.


        :param current_version: The current_version of this CccUpgradeInformation.
        :type: str
        """
        self._current_version = current_version

    @property
    def time_of_scheduled_upgrade(self):
        """
        Gets the time_of_scheduled_upgrade of this CccUpgradeInformation.
        Compute Cloud@Customer infrastructure next upgrade time. The rack might have performance
        impacts during this time.


        :return: The time_of_scheduled_upgrade of this CccUpgradeInformation.
        :rtype: datetime
        """
        return self._time_of_scheduled_upgrade

    @time_of_scheduled_upgrade.setter
    def time_of_scheduled_upgrade(self, time_of_scheduled_upgrade):
        """
        Sets the time_of_scheduled_upgrade of this CccUpgradeInformation.
        Compute Cloud@Customer infrastructure next upgrade time. The rack might have performance
        impacts during this time.


        :param time_of_scheduled_upgrade: The time_of_scheduled_upgrade of this CccUpgradeInformation.
        :type: datetime
        """
        self._time_of_scheduled_upgrade = time_of_scheduled_upgrade

    @property
    def scheduled_upgrade_duration(self):
        """
        Gets the scheduled_upgrade_duration of this CccUpgradeInformation.
        Expected duration of Compute Cloud@Customer infrastructure scheduled upgrade. The actual
        upgrade time might be longer or shorter than this duration depending on rack activity, this
        is only an estimate.


        :return: The scheduled_upgrade_duration of this CccUpgradeInformation.
        :rtype: str
        """
        return self._scheduled_upgrade_duration

    @scheduled_upgrade_duration.setter
    def scheduled_upgrade_duration(self, scheduled_upgrade_duration):
        """
        Sets the scheduled_upgrade_duration of this CccUpgradeInformation.
        Expected duration of Compute Cloud@Customer infrastructure scheduled upgrade. The actual
        upgrade time might be longer or shorter than this duration depending on rack activity, this
        is only an estimate.


        :param scheduled_upgrade_duration: The scheduled_upgrade_duration of this CccUpgradeInformation.
        :type: str
        """
        self._scheduled_upgrade_duration = scheduled_upgrade_duration

    @property
    def is_active(self):
        """
        Gets the is_active of this CccUpgradeInformation.
        Indication that the Compute Cloud@Customer infrastructure is in the process of
        an upgrade or an upgrade activity (such as preloading upgrade images).


        :return: The is_active of this CccUpgradeInformation.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this CccUpgradeInformation.
        Indication that the Compute Cloud@Customer infrastructure is in the process of
        an upgrade or an upgrade activity (such as preloading upgrade images).


        :param is_active: The is_active of this CccUpgradeInformation.
        :type: bool
        """
        self._is_active = is_active

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

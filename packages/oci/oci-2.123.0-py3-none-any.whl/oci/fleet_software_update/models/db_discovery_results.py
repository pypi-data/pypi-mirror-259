# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .db_fleet_discovery_details import DbFleetDiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbDiscoveryResults(DbFleetDiscoveryDetails):
    """
    Collection built from the results of a Succeeded Fleet Software Update Discovery resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbDiscoveryResults object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.DbDiscoveryResults.strategy` attribute
        of this class is ``DISCOVERY_RESULTS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy:
            The value to assign to the strategy property of this DbDiscoveryResults.
            Allowed values for this property are: "SEARCH_QUERY", "FILTERS", "TARGET_LIST", "DISCOVERY_RESULTS"
        :type strategy: str

        :param fsu_discovery_id:
            The value to assign to the fsu_discovery_id property of this DbDiscoveryResults.
        :type fsu_discovery_id: str

        """
        self.swagger_types = {
            'strategy': 'str',
            'fsu_discovery_id': 'str'
        }

        self.attribute_map = {
            'strategy': 'strategy',
            'fsu_discovery_id': 'fsuDiscoveryId'
        }

        self._strategy = None
        self._fsu_discovery_id = None
        self._strategy = 'DISCOVERY_RESULTS'

    @property
    def fsu_discovery_id(self):
        """
        **[Required]** Gets the fsu_discovery_id of this DbDiscoveryResults.
        OCIDs of Fleet Software Update Discovery.


        :return: The fsu_discovery_id of this DbDiscoveryResults.
        :rtype: str
        """
        return self._fsu_discovery_id

    @fsu_discovery_id.setter
    def fsu_discovery_id(self, fsu_discovery_id):
        """
        Sets the fsu_discovery_id of this DbDiscoveryResults.
        OCIDs of Fleet Software Update Discovery.


        :param fsu_discovery_id: The fsu_discovery_id of this DbDiscoveryResults.
        :type: str
        """
        self._fsu_discovery_id = fsu_discovery_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

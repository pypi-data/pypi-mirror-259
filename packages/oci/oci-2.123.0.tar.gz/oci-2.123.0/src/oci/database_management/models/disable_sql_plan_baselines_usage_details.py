# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisableSqlPlanBaselinesUsageDetails(object):
    """
    The details required to disable SQL plan baseline usage.
    It takes either credentials or databaseCredential. It's recommended to provide databaseCredential
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DisableSqlPlanBaselinesUsageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credentials:
            The value to assign to the credentials property of this DisableSqlPlanBaselinesUsageDetails.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        :param database_credential:
            The value to assign to the database_credential property of this DisableSqlPlanBaselinesUsageDetails.
        :type database_credential: oci.database_management.models.DatabaseCredentialDetails

        """
        self.swagger_types = {
            'credentials': 'ManagedDatabaseCredential',
            'database_credential': 'DatabaseCredentialDetails'
        }

        self.attribute_map = {
            'credentials': 'credentials',
            'database_credential': 'databaseCredential'
        }

        self._credentials = None
        self._database_credential = None

    @property
    def credentials(self):
        """
        Gets the credentials of this DisableSqlPlanBaselinesUsageDetails.

        :return: The credentials of this DisableSqlPlanBaselinesUsageDetails.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this DisableSqlPlanBaselinesUsageDetails.

        :param credentials: The credentials of this DisableSqlPlanBaselinesUsageDetails.
        :type: oci.database_management.models.ManagedDatabaseCredential
        """
        self._credentials = credentials

    @property
    def database_credential(self):
        """
        Gets the database_credential of this DisableSqlPlanBaselinesUsageDetails.

        :return: The database_credential of this DisableSqlPlanBaselinesUsageDetails.
        :rtype: oci.database_management.models.DatabaseCredentialDetails
        """
        return self._database_credential

    @database_credential.setter
    def database_credential(self, database_credential):
        """
        Sets the database_credential of this DisableSqlPlanBaselinesUsageDetails.

        :param database_credential: The database_credential of this DisableSqlPlanBaselinesUsageDetails.
        :type: oci.database_management.models.DatabaseCredentialDetails
        """
        self._database_credential = database_credential

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

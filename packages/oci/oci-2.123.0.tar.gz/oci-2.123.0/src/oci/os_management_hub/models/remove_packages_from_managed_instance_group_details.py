# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemovePackagesFromManagedInstanceGroupDetails(object):
    """
    The names of the packages to be removed from the managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemovePackagesFromManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_names:
            The value to assign to the package_names property of this RemovePackagesFromManagedInstanceGroupDetails.
        :type package_names: list[str]

        :param work_request_details:
            The value to assign to the work_request_details property of this RemovePackagesFromManagedInstanceGroupDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'package_names': 'list[str]',
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'package_names': 'packageNames',
            'work_request_details': 'workRequestDetails'
        }

        self._package_names = None
        self._work_request_details = None

    @property
    def package_names(self):
        """
        Gets the package_names of this RemovePackagesFromManagedInstanceGroupDetails.
        The list of package names.


        :return: The package_names of this RemovePackagesFromManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._package_names

    @package_names.setter
    def package_names(self, package_names):
        """
        Sets the package_names of this RemovePackagesFromManagedInstanceGroupDetails.
        The list of package names.


        :param package_names: The package_names of this RemovePackagesFromManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._package_names = package_names

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this RemovePackagesFromManagedInstanceGroupDetails.

        :return: The work_request_details of this RemovePackagesFromManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this RemovePackagesFromManagedInstanceGroupDetails.

        :param work_request_details: The work_request_details of this RemovePackagesFromManagedInstanceGroupDetails.
        :type: oci.os_management_hub.models.WorkRequestDetails
        """
        self._work_request_details = work_request_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

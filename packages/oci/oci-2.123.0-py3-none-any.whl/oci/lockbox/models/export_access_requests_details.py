# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220126


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportAccessRequestsDetails(object):
    """
    Details for generating report of Access Requests to export action
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportAccessRequestsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lockbox_id:
            The value to assign to the lockbox_id property of this ExportAccessRequestsDetails.
        :type lockbox_id: str

        :param time_created_after:
            The value to assign to the time_created_after property of this ExportAccessRequestsDetails.
        :type time_created_after: datetime

        :param time_created_before:
            The value to assign to the time_created_before property of this ExportAccessRequestsDetails.
        :type time_created_before: datetime

        """
        self.swagger_types = {
            'lockbox_id': 'str',
            'time_created_after': 'datetime',
            'time_created_before': 'datetime'
        }

        self.attribute_map = {
            'lockbox_id': 'lockboxId',
            'time_created_after': 'timeCreatedAfter',
            'time_created_before': 'timeCreatedBefore'
        }

        self._lockbox_id = None
        self._time_created_after = None
        self._time_created_before = None

    @property
    def lockbox_id(self):
        """
        **[Required]** Gets the lockbox_id of this ExportAccessRequestsDetails.
        The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.


        :return: The lockbox_id of this ExportAccessRequestsDetails.
        :rtype: str
        """
        return self._lockbox_id

    @lockbox_id.setter
    def lockbox_id(self, lockbox_id):
        """
        Sets the lockbox_id of this ExportAccessRequestsDetails.
        The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.


        :param lockbox_id: The lockbox_id of this ExportAccessRequestsDetails.
        :type: str
        """
        self._lockbox_id = lockbox_id

    @property
    def time_created_after(self):
        """
        **[Required]** Gets the time_created_after of this ExportAccessRequestsDetails.
        Date and time after which access requests were created, as described in `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created_after of this ExportAccessRequestsDetails.
        :rtype: datetime
        """
        return self._time_created_after

    @time_created_after.setter
    def time_created_after(self, time_created_after):
        """
        Sets the time_created_after of this ExportAccessRequestsDetails.
        Date and time after which access requests were created, as described in `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created_after: The time_created_after of this ExportAccessRequestsDetails.
        :type: datetime
        """
        self._time_created_after = time_created_after

    @property
    def time_created_before(self):
        """
        **[Required]** Gets the time_created_before of this ExportAccessRequestsDetails.
        Date and time before which access requests were created, as described in `RFC 3339`__s

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created_before of this ExportAccessRequestsDetails.
        :rtype: datetime
        """
        return self._time_created_before

    @time_created_before.setter
    def time_created_before(self, time_created_before):
        """
        Sets the time_created_before of this ExportAccessRequestsDetails.
        Date and time before which access requests were created, as described in `RFC 3339`__s

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created_before: The time_created_before of this ExportAccessRequestsDetails.
        :type: datetime
        """
        self._time_created_before = time_created_before

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadPartitionCertificatesDetails(object):
    """
    The details of the partition certificates.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UploadPartitionCertificatesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param partition_certificate:
            The value to assign to the partition_certificate property of this UploadPartitionCertificatesDetails.
        :type partition_certificate: str

        :param partition_owner_certificate:
            The value to assign to the partition_owner_certificate property of this UploadPartitionCertificatesDetails.
        :type partition_owner_certificate: str

        """
        self.swagger_types = {
            'partition_certificate': 'str',
            'partition_owner_certificate': 'str'
        }

        self.attribute_map = {
            'partition_certificate': 'partitionCertificate',
            'partition_owner_certificate': 'partitionOwnerCertificate'
        }

        self._partition_certificate = None
        self._partition_owner_certificate = None

    @property
    def partition_certificate(self):
        """
        **[Required]** Gets the partition_certificate of this UploadPartitionCertificatesDetails.
        Base64 encoded (StandardCharsets.UTF_8) Partition Certificate.


        :return: The partition_certificate of this UploadPartitionCertificatesDetails.
        :rtype: str
        """
        return self._partition_certificate

    @partition_certificate.setter
    def partition_certificate(self, partition_certificate):
        """
        Sets the partition_certificate of this UploadPartitionCertificatesDetails.
        Base64 encoded (StandardCharsets.UTF_8) Partition Certificate.


        :param partition_certificate: The partition_certificate of this UploadPartitionCertificatesDetails.
        :type: str
        """
        self._partition_certificate = partition_certificate

    @property
    def partition_owner_certificate(self):
        """
        **[Required]** Gets the partition_owner_certificate of this UploadPartitionCertificatesDetails.
        Base64 encoded (StandardCharsets.UTF_8) Partition Owner Certificate.


        :return: The partition_owner_certificate of this UploadPartitionCertificatesDetails.
        :rtype: str
        """
        return self._partition_owner_certificate

    @partition_owner_certificate.setter
    def partition_owner_certificate(self, partition_owner_certificate):
        """
        Sets the partition_owner_certificate of this UploadPartitionCertificatesDetails.
        Base64 encoded (StandardCharsets.UTF_8) Partition Owner Certificate.


        :param partition_owner_certificate: The partition_owner_certificate of this UploadPartitionCertificatesDetails.
        :type: str
        """
        self._partition_owner_certificate = partition_owner_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

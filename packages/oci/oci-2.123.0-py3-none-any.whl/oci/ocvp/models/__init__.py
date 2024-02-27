# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230701

from __future__ import absolute_import

from .change_sddc_compartment_details import ChangeSddcCompartmentDetails
from .cluster import Cluster
from .cluster_collection import ClusterCollection
from .cluster_summary import ClusterSummary
from .create_cluster_details import CreateClusterDetails
from .create_esxi_host_details import CreateEsxiHostDetails
from .create_sddc_details import CreateSddcDetails
from .datastore_details import DatastoreDetails
from .datastore_info import DatastoreInfo
from .downgrade_hcx_details import DowngradeHcxDetails
from .esxi_host import EsxiHost
from .esxi_host_collection import EsxiHostCollection
from .esxi_host_summary import EsxiHostSummary
from .hcx_license_summary import HcxLicenseSummary
from .initial_cluster_configuration import InitialClusterConfiguration
from .initial_configuration import InitialConfiguration
from .network_configuration import NetworkConfiguration
from .replace_host_details import ReplaceHostDetails
from .sddc import Sddc
from .sddc_collection import SddcCollection
from .sddc_password import SddcPassword
from .sddc_summary import SddcSummary
from .supported_commitment_summary import SupportedCommitmentSummary
from .supported_commitment_summary_collection import SupportedCommitmentSummaryCollection
from .supported_esxi_software_version_summary import SupportedEsxiSoftwareVersionSummary
from .supported_host_shape_collection import SupportedHostShapeCollection
from .supported_host_shape_summary import SupportedHostShapeSummary
from .supported_vmware_software_version_collection import SupportedVmwareSoftwareVersionCollection
from .supported_vmware_software_version_summary import SupportedVmwareSoftwareVersionSummary
from .update_cluster_details import UpdateClusterDetails
from .update_esxi_host_details import UpdateEsxiHostDetails
from .update_sddc_details import UpdateSddcDetails
from .vsphere_license import VsphereLicense
from .vsphere_upgrade_object import VsphereUpgradeObject
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for ocvp services.
ocvp_type_mapping = {
    "ChangeSddcCompartmentDetails": ChangeSddcCompartmentDetails,
    "Cluster": Cluster,
    "ClusterCollection": ClusterCollection,
    "ClusterSummary": ClusterSummary,
    "CreateClusterDetails": CreateClusterDetails,
    "CreateEsxiHostDetails": CreateEsxiHostDetails,
    "CreateSddcDetails": CreateSddcDetails,
    "DatastoreDetails": DatastoreDetails,
    "DatastoreInfo": DatastoreInfo,
    "DowngradeHcxDetails": DowngradeHcxDetails,
    "EsxiHost": EsxiHost,
    "EsxiHostCollection": EsxiHostCollection,
    "EsxiHostSummary": EsxiHostSummary,
    "HcxLicenseSummary": HcxLicenseSummary,
    "InitialClusterConfiguration": InitialClusterConfiguration,
    "InitialConfiguration": InitialConfiguration,
    "NetworkConfiguration": NetworkConfiguration,
    "ReplaceHostDetails": ReplaceHostDetails,
    "Sddc": Sddc,
    "SddcCollection": SddcCollection,
    "SddcPassword": SddcPassword,
    "SddcSummary": SddcSummary,
    "SupportedCommitmentSummary": SupportedCommitmentSummary,
    "SupportedCommitmentSummaryCollection": SupportedCommitmentSummaryCollection,
    "SupportedEsxiSoftwareVersionSummary": SupportedEsxiSoftwareVersionSummary,
    "SupportedHostShapeCollection": SupportedHostShapeCollection,
    "SupportedHostShapeSummary": SupportedHostShapeSummary,
    "SupportedVmwareSoftwareVersionCollection": SupportedVmwareSoftwareVersionCollection,
    "SupportedVmwareSoftwareVersionSummary": SupportedVmwareSoftwareVersionSummary,
    "UpdateClusterDetails": UpdateClusterDetails,
    "UpdateEsxiHostDetails": UpdateEsxiHostDetails,
    "UpdateSddcDetails": UpdateSddcDetails,
    "VsphereLicense": VsphereLicense,
    "VsphereUpgradeObject": VsphereUpgradeObject,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}

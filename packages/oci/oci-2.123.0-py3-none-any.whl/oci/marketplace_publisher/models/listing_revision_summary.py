# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingRevisionSummary(object):
    """
    The model for a summary of an Oracle Cloud Infrastructure Marketplace Publisher listing revision.
    """

    #: A constant which can be used with the package_type property of a ListingRevisionSummary.
    #: This constant has a value of "CONTAINER_IMAGE"
    PACKAGE_TYPE_CONTAINER_IMAGE = "CONTAINER_IMAGE"

    #: A constant which can be used with the package_type property of a ListingRevisionSummary.
    #: This constant has a value of "HELM_CHART"
    PACKAGE_TYPE_HELM_CHART = "HELM_CHART"

    def __init__(self, **kwargs):
        """
        Initializes a new ListingRevisionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ListingRevisionSummary.
        :type id: str

        :param listing_id:
            The value to assign to the listing_id property of this ListingRevisionSummary.
        :type listing_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ListingRevisionSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ListingRevisionSummary.
        :type display_name: str

        :param status:
            The value to assign to the status property of this ListingRevisionSummary.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ListingRevisionSummary.
        :type lifecycle_state: str

        :param package_type:
            The value to assign to the package_type property of this ListingRevisionSummary.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param pricing_type:
            The value to assign to the pricing_type property of this ListingRevisionSummary.
        :type pricing_type: str

        :param short_description:
            The value to assign to the short_description property of this ListingRevisionSummary.
        :type short_description: str

        :param tagline:
            The value to assign to the tagline property of this ListingRevisionSummary.
        :type tagline: str

        :param icon:
            The value to assign to the icon property of this ListingRevisionSummary.
        :type icon: oci.marketplace_publisher.models.ListingRevisionIconAttachment

        :param markets:
            The value to assign to the markets property of this ListingRevisionSummary.
        :type markets: list[str]

        :param categories:
            The value to assign to the categories property of this ListingRevisionSummary.
        :type categories: list[str]

        :param time_created:
            The value to assign to the time_created property of this ListingRevisionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ListingRevisionSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ListingRevisionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ListingRevisionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ListingRevisionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'listing_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'package_type': 'str',
            'pricing_type': 'str',
            'short_description': 'str',
            'tagline': 'str',
            'icon': 'ListingRevisionIconAttachment',
            'markets': 'list[str]',
            'categories': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'listing_id': 'listingId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'package_type': 'packageType',
            'pricing_type': 'pricingType',
            'short_description': 'shortDescription',
            'tagline': 'tagline',
            'icon': 'icon',
            'markets': 'markets',
            'categories': 'categories',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._listing_id = None
        self._compartment_id = None
        self._display_name = None
        self._status = None
        self._lifecycle_state = None
        self._package_type = None
        self._pricing_type = None
        self._short_description = None
        self._tagline = None
        self._icon = None
        self._markets = None
        self._categories = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ListingRevisionSummary.
        The OCID for the listing revision in Marketplace Publisher.


        :return: The id of this ListingRevisionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ListingRevisionSummary.
        The OCID for the listing revision in Marketplace Publisher.


        :param id: The id of this ListingRevisionSummary.
        :type: str
        """
        self._id = id

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this ListingRevisionSummary.
        The OCID for the listing in Marketplace Publisher.


        :return: The listing_id of this ListingRevisionSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this ListingRevisionSummary.
        The OCID for the listing in Marketplace Publisher.


        :param listing_id: The listing_id of this ListingRevisionSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ListingRevisionSummary.
        The unique identifier for the compartment.


        :return: The compartment_id of this ListingRevisionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ListingRevisionSummary.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this ListingRevisionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ListingRevisionSummary.
        The name of the listing revision.


        :return: The display_name of this ListingRevisionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ListingRevisionSummary.
        The name of the listing revision.


        :param display_name: The display_name of this ListingRevisionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ListingRevisionSummary.
        The current status of the listing revision.


        :return: The status of this ListingRevisionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ListingRevisionSummary.
        The current status of the listing revision.


        :param status: The status of this ListingRevisionSummary.
        :type: str
        """
        self._status = status

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ListingRevisionSummary.
        The current state of the Listing.


        :return: The lifecycle_state of this ListingRevisionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ListingRevisionSummary.
        The current state of the Listing.


        :param lifecycle_state: The lifecycle_state of this ListingRevisionSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this ListingRevisionSummary.
        The listing's package type.

        Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this ListingRevisionSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this ListingRevisionSummary.
        The listing's package type.


        :param package_type: The package_type of this ListingRevisionSummary.
        :type: str
        """
        allowed_values = ["CONTAINER_IMAGE", "HELM_CHART"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def pricing_type(self):
        """
        **[Required]** Gets the pricing_type of this ListingRevisionSummary.
        Pricing type of the listing.


        :return: The pricing_type of this ListingRevisionSummary.
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """
        Sets the pricing_type of this ListingRevisionSummary.
        Pricing type of the listing.


        :param pricing_type: The pricing_type of this ListingRevisionSummary.
        :type: str
        """
        self._pricing_type = pricing_type

    @property
    def short_description(self):
        """
        Gets the short_description of this ListingRevisionSummary.
        A short description of the listing revision.


        :return: The short_description of this ListingRevisionSummary.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this ListingRevisionSummary.
        A short description of the listing revision.


        :param short_description: The short_description of this ListingRevisionSummary.
        :type: str
        """
        self._short_description = short_description

    @property
    def tagline(self):
        """
        Gets the tagline of this ListingRevisionSummary.
        The tagline of the listing revision.


        :return: The tagline of this ListingRevisionSummary.
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """
        Sets the tagline of this ListingRevisionSummary.
        The tagline of the listing revision.


        :param tagline: The tagline of this ListingRevisionSummary.
        :type: str
        """
        self._tagline = tagline

    @property
    def icon(self):
        """
        Gets the icon of this ListingRevisionSummary.

        :return: The icon of this ListingRevisionSummary.
        :rtype: oci.marketplace_publisher.models.ListingRevisionIconAttachment
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this ListingRevisionSummary.

        :param icon: The icon of this ListingRevisionSummary.
        :type: oci.marketplace_publisher.models.ListingRevisionIconAttachment
        """
        self._icon = icon

    @property
    def markets(self):
        """
        Gets the markets of this ListingRevisionSummary.
        The markets where you can deploy the listing.


        :return: The markets of this ListingRevisionSummary.
        :rtype: list[str]
        """
        return self._markets

    @markets.setter
    def markets(self, markets):
        """
        Sets the markets of this ListingRevisionSummary.
        The markets where you can deploy the listing.


        :param markets: The markets of this ListingRevisionSummary.
        :type: list[str]
        """
        self._markets = markets

    @property
    def categories(self):
        """
        **[Required]** Gets the categories of this ListingRevisionSummary.
        Categories that the listing revision belongs to.


        :return: The categories of this ListingRevisionSummary.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this ListingRevisionSummary.
        Categories that the listing revision belongs to.


        :param categories: The categories of this ListingRevisionSummary.
        :type: list[str]
        """
        self._categories = categories

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ListingRevisionSummary.
        The date and time the listing revision was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ListingRevisionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ListingRevisionSummary.
        The date and time the listing revision was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ListingRevisionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ListingRevisionSummary.
        The date and time the listing revision was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ListingRevisionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ListingRevisionSummary.
        The date and time the listing revision was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ListingRevisionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ListingRevisionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ListingRevisionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ListingRevisionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ListingRevisionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ListingRevisionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ListingRevisionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ListingRevisionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ListingRevisionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ListingRevisionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ListingRevisionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ListingRevisionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ListingRevisionSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

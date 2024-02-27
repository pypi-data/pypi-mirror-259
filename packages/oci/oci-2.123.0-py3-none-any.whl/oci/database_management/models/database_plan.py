# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabasePlan(object):
    """
    The resource allocation directives must all use the share attribute, or they must all use the level and allocation attributes.
    If you use the share attribute to allocate I/O resources, then the database plan can have a maximum of 1024 directives.
    If you use the level and allocation attributes to allocate I/O resources, then the database plan can have
    a maximum of 32 directives.
    Only one directive is allowed for each database name and each profile name.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabasePlan object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this DatabasePlan.
        :type items: list[oci.database_management.models.DatabasePlanDirective]

        """
        self.swagger_types = {
            'items': 'list[DatabasePlanDirective]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this DatabasePlan.
        A list of DatabasePlanDirectives.


        :return: The items of this DatabasePlan.
        :rtype: list[oci.database_management.models.DatabasePlanDirective]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DatabasePlan.
        A list of DatabasePlanDirectives.


        :param items: The items of this DatabasePlan.
        :type: list[oci.database_management.models.DatabasePlanDirective]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

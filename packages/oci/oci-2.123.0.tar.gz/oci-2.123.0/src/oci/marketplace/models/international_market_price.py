# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InternationalMarketPrice(object):
    """
    The model for international market pricing.
    """

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "USD"
    CURRENCY_CODE_USD = "USD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CAD"
    CURRENCY_CODE_CAD = "CAD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "INR"
    CURRENCY_CODE_INR = "INR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "GBP"
    CURRENCY_CODE_GBP = "GBP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "BRL"
    CURRENCY_CODE_BRL = "BRL"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "JPY"
    CURRENCY_CODE_JPY = "JPY"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "OMR"
    CURRENCY_CODE_OMR = "OMR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "EUR"
    CURRENCY_CODE_EUR = "EUR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CHF"
    CURRENCY_CODE_CHF = "CHF"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "MXN"
    CURRENCY_CODE_MXN = "MXN"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CLP"
    CURRENCY_CODE_CLP = "CLP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "ALL"
    CURRENCY_CODE_ALL = "ALL"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "ARS"
    CURRENCY_CODE_ARS = "ARS"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "AUD"
    CURRENCY_CODE_AUD = "AUD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "BDT"
    CURRENCY_CODE_BDT = "BDT"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "BAM"
    CURRENCY_CODE_BAM = "BAM"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "BGN"
    CURRENCY_CODE_BGN = "BGN"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CNY"
    CURRENCY_CODE_CNY = "CNY"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "COP"
    CURRENCY_CODE_COP = "COP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CRC"
    CURRENCY_CODE_CRC = "CRC"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "HRK"
    CURRENCY_CODE_HRK = "HRK"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CZK"
    CURRENCY_CODE_CZK = "CZK"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "DKK"
    CURRENCY_CODE_DKK = "DKK"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "EGP"
    CURRENCY_CODE_EGP = "EGP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "HKD"
    CURRENCY_CODE_HKD = "HKD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "HUF"
    CURRENCY_CODE_HUF = "HUF"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "ISK"
    CURRENCY_CODE_ISK = "ISK"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "IDR"
    CURRENCY_CODE_IDR = "IDR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "ILS"
    CURRENCY_CODE_ILS = "ILS"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "JMD"
    CURRENCY_CODE_JMD = "JMD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "KZT"
    CURRENCY_CODE_KZT = "KZT"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "KES"
    CURRENCY_CODE_KES = "KES"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "KRW"
    CURRENCY_CODE_KRW = "KRW"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "KWD"
    CURRENCY_CODE_KWD = "KWD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "LBP"
    CURRENCY_CODE_LBP = "LBP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "MOP"
    CURRENCY_CODE_MOP = "MOP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "MYR"
    CURRENCY_CODE_MYR = "MYR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "MVR"
    CURRENCY_CODE_MVR = "MVR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "AED"
    CURRENCY_CODE_AED = "AED"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "NZD"
    CURRENCY_CODE_NZD = "NZD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "NOK"
    CURRENCY_CODE_NOK = "NOK"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "PKR"
    CURRENCY_CODE_PKR = "PKR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "PEN"
    CURRENCY_CODE_PEN = "PEN"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "PHP"
    CURRENCY_CODE_PHP = "PHP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "PLN"
    CURRENCY_CODE_PLN = "PLN"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "QAR"
    CURRENCY_CODE_QAR = "QAR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "RON"
    CURRENCY_CODE_RON = "RON"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "SAR"
    CURRENCY_CODE_SAR = "SAR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "RSD"
    CURRENCY_CODE_RSD = "RSD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "SGD"
    CURRENCY_CODE_SGD = "SGD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "ZAR"
    CURRENCY_CODE_ZAR = "ZAR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "SEK"
    CURRENCY_CODE_SEK = "SEK"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "TWD"
    CURRENCY_CODE_TWD = "TWD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "THB"
    CURRENCY_CODE_THB = "THB"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "TRY"
    CURRENCY_CODE_TRY = "TRY"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "VND"
    CURRENCY_CODE_VND = "VND"

    def __init__(self, **kwargs):
        """
        Initializes a new InternationalMarketPrice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param currency_code:
            The value to assign to the currency_code property of this InternationalMarketPrice.
            Allowed values for this property are: "USD", "CAD", "INR", "GBP", "BRL", "JPY", "OMR", "EUR", "CHF", "MXN", "CLP", "ALL", "ARS", "AUD", "BDT", "BAM", "BGN", "CNY", "COP", "CRC", "HRK", "CZK", "DKK", "EGP", "HKD", "HUF", "ISK", "IDR", "ILS", "JMD", "KZT", "KES", "KRW", "KWD", "LBP", "MOP", "MYR", "MVR", "AED", "NZD", "NOK", "PKR", "PEN", "PHP", "PLN", "QAR", "RON", "SAR", "RSD", "SGD", "ZAR", "SEK", "TWD", "THB", "TRY", "VND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type currency_code: str

        :param currency_symbol:
            The value to assign to the currency_symbol property of this InternationalMarketPrice.
        :type currency_symbol: str

        :param rate:
            The value to assign to the rate property of this InternationalMarketPrice.
        :type rate: float

        """
        self.swagger_types = {
            'currency_code': 'str',
            'currency_symbol': 'str',
            'rate': 'float'
        }

        self.attribute_map = {
            'currency_code': 'currencyCode',
            'currency_symbol': 'currencySymbol',
            'rate': 'rate'
        }

        self._currency_code = None
        self._currency_symbol = None
        self._rate = None

    @property
    def currency_code(self):
        """
        **[Required]** Gets the currency_code of this InternationalMarketPrice.
        The currency of the pricing model.

        Allowed values for this property are: "USD", "CAD", "INR", "GBP", "BRL", "JPY", "OMR", "EUR", "CHF", "MXN", "CLP", "ALL", "ARS", "AUD", "BDT", "BAM", "BGN", "CNY", "COP", "CRC", "HRK", "CZK", "DKK", "EGP", "HKD", "HUF", "ISK", "IDR", "ILS", "JMD", "KZT", "KES", "KRW", "KWD", "LBP", "MOP", "MYR", "MVR", "AED", "NZD", "NOK", "PKR", "PEN", "PHP", "PLN", "QAR", "RON", "SAR", "RSD", "SGD", "ZAR", "SEK", "TWD", "THB", "TRY", "VND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The currency_code of this InternationalMarketPrice.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this InternationalMarketPrice.
        The currency of the pricing model.


        :param currency_code: The currency_code of this InternationalMarketPrice.
        :type: str
        """
        allowed_values = ["USD", "CAD", "INR", "GBP", "BRL", "JPY", "OMR", "EUR", "CHF", "MXN", "CLP", "ALL", "ARS", "AUD", "BDT", "BAM", "BGN", "CNY", "COP", "CRC", "HRK", "CZK", "DKK", "EGP", "HKD", "HUF", "ISK", "IDR", "ILS", "JMD", "KZT", "KES", "KRW", "KWD", "LBP", "MOP", "MYR", "MVR", "AED", "NZD", "NOK", "PKR", "PEN", "PHP", "PLN", "QAR", "RON", "SAR", "RSD", "SGD", "ZAR", "SEK", "TWD", "THB", "TRY", "VND"]
        if not value_allowed_none_or_none_sentinel(currency_code, allowed_values):
            currency_code = 'UNKNOWN_ENUM_VALUE'
        self._currency_code = currency_code

    @property
    def currency_symbol(self):
        """
        Gets the currency_symbol of this InternationalMarketPrice.
        The symbol of the currency


        :return: The currency_symbol of this InternationalMarketPrice.
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """
        Sets the currency_symbol of this InternationalMarketPrice.
        The symbol of the currency


        :param currency_symbol: The currency_symbol of this InternationalMarketPrice.
        :type: str
        """
        self._currency_symbol = currency_symbol

    @property
    def rate(self):
        """
        **[Required]** Gets the rate of this InternationalMarketPrice.
        The pricing rate.


        :return: The rate of this InternationalMarketPrice.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this InternationalMarketPrice.
        The pricing rate.


        :param rate: The rate of this InternationalMarketPrice.
        :type: float
        """
        self._rate = rate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

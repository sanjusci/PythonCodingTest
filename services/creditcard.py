import re
from datetime import datetime
from decimal import Decimal

from logger import Logger

AMERICAN_EXPRESS = "(?:3[47][0-9]{13})"
DINERS_CLUB = "(?:3(?:0[0-5]|[68][0-9])[0-9]{11})"
DISCOVER = "(?:6(?:011|5[0-9]{2})(?:[0-9]{12}))"
JCB = "(?:(?:2131|1800|35\\d{3})\\d{11})"
MAESTRO = "(?:(?:5[0678]\\d\\d|6304|6390|67\\d\\d)\\d{8,15})"
MASTER_CARD = (
    "(?:(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27["
    "01][0-9]|2720)[0-9]{12})"
)
VISA = "(?:4[0-9]{12})(?:[0-9]{3})?"

CARDS_REGEX = (
    AMERICAN_EXPRESS,
    DINERS_CLUB,
    DINERS_CLUB,
    JCB,
    MAESTRO,
    MASTER_CARD,
    VISA,
)


# def validate_card(card):
#     flag = True
#     for reg in CARDS_REGEX:
#         if not re.search(reg, card) or re.search(r"(\d)\1{3}", re.sub("-", "", card)):
#             flag = False
#     if flag:
#         return True
#     return flag


def validate_card(card):
    if not re.search(r"^[456]\d{3}(-?\d{4}){3}$", card) or re.search(
            r"(\d)\1{3}", re.sub("-", "", card)
    ):
        return False
    return True


class CreditCard(object):
    def __init__(self):
        """
        - CreditCardNumber
        - CardHolder
        - ExpirationDate
        - SecurityCode
        - Amount
        """
        self.CreditCardNumber = None
        self.CardHolder = None
        self.ExpirationDate = None
        self.SecurityCode = None
        self.Amount = None

    def validate_card_details(self, **kwargs):
        """
        - CreditCardNumber (mandatory, string, it should be a valid credit card number)
        - CardHolder: (mandatory, string)
        - ExpirationDate (mandatory, DateTime, it cannot be in the past)
        - SecurityCode (optional, string, 3 digits)
        - Amount (mandatory decimal, positive amount)

        :param kwargs:
          A kwargs that contains:
            - CreditCardNumber
            - CardHolder
            - ExpirationDate
            - SecurityCode
            - Amount
        :return: Return boolean True or False

        """
        cards_value = ["CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"]

        # Check Mandatory fields
        if set(cards_value) & kwargs.keys() != set(cards_value):
            Logger.info("Check Card values")
            return False
        elif kwargs["CreditCardNumber"] is None or not isinstance(
            kwargs["CreditCardNumber"], (str,)
        ):
            return False
        elif len(kwargs["CreditCardNumber"]) != 16:
            Logger.info("Credit Card length is not 16!")
            return False
        elif validate_card(kwargs["CreditCardNumber"]):
            Logger.info("invalid credit card number")
            return False
        elif kwargs["CardHolder"] is None or not isinstance(
            kwargs["CardHolder"], (str,)
        ):
            Logger.info("Card Holder is not String")
            return False
        elif kwargs["ExpirationDate"] is None or (
            datetime.strptime(kwargs["ExpirationDate"], "%Y/%m/%d") < datetime.now()
        ):
            Logger.info("Card has been Expired")
            return False
        elif kwargs["Amount"] is None or not isinstance(kwargs["Amount"], (float,)):
            Logger.info("Credit Card amount is not in valid format")
            return False
        elif Decimal(kwargs["Amount"]) <= 0:
            Logger.info("Credit Card amount is in negative")
            return False

        if kwargs.get("SecurityCode", None):
            if (
                not (
                    isinstance(kwargs["SecurityCode"], (str,))
                    and len(kwargs["SecurityCode"]) == 3
                )
            ):
                Logger.info("Credit Card SecurityCode is not string or "
                            "length is not 3")
                return False

        self.__map_card_data(**kwargs)
        return True

    def __map_card_data(self, **kwargs):
        """
        :param kwargs:
          A kwargs that contains:
            - CreditCardNumber
            - CardHolder
            - ExpirationDate
            - SecurityCode
            - Amount
        :return: None
        """
        self.CreditCardNumber = kwargs.get("CreditCardNumber", None)
        self.Amount = kwargs.get("Amount", None)
        self.CardHolder = kwargs.get("CardHolder", None)
        self.SecurityCode = kwargs.get("SecurityCode", None)
        self.ExpirationDate = kwargs.get("ExpirationDate", None)

        Logger.info("mapping of user input is done successfully.")

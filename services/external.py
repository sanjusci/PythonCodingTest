import enum
import importlib

from logger import Logger
from services.base import BaseService


class Enum(enum.Enum):
    @classmethod
    def to_dict(cls):
        return dict(cls.__members__)

    @classmethod
    def get_by_name(cls, name):
        module = importlib.import_module(__name__)
        return getattr(module, name, None)


class PaymentRule(Enum):

    CHEAP_PAYMENT = 20.00
    EXPENSIVE_PAYMENT = 21.00
    PREMIUM_PAYMENT = 501.00

    def __str__(self):
        return self.value


class PremiumPaymentGateway(BaseService):
    def __init__(self, repeat=3):
        super(PremiumPaymentGateway, self).__init__(repeat)
        self.gateway_type = "PremiumPaymentGatway"

    def __repr__(self):
        return f"{self.__class__.__name__}"


class ExpensivePaymentGateway(BaseService):
    def __init__(self, repeat=1):
        super(ExpensivePaymentGateway, self).__init__(repeat)
        self.gateway_type = "ExpensivePaymentGateway"

    def __repr__(self):
        return f"{self.__class__.__name__}"


class CheapPaymentGateway(BaseService):
    def __init__(self, repeat=0):
        super(CheapPaymentGateway, self).__init__(repeat)
        self.gateway_type = "CheapPaymentGateway"

    def __repr__(self):
        return f"{self.__class__.__name__}"


class ExternalService(object):
    def __init__(self, amount, card_details=None):
        self.amount = amount
        self.card_details = card_details

    def make_payment(self):
        try:
            Logger.info("Amount")
            Logger.info(self.amount)
            if self.amount <= PaymentRule.CHEAP_PAYMENT.value:
                payment_mode = CheapPaymentGateway()
            elif (
                PaymentRule.EXPENSIVE_PAYMENT.value
                <= self.amount
                < PaymentRule.PREMIUM_PAYMENT.value
            ):
                payment_mode = ExpensivePaymentGateway()
            elif self.amount >= PaymentRule.PREMIUM_PAYMENT.value:
                payment_mode = PremiumPaymentGateway()
            else:
                return False

            status = payment_mode.pay(self.amount, self.card_details)
            return status
        except Exception as e:
            Logger.exception(e)
            return False

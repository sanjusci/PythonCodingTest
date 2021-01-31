from logger import Logger


class BaseService(object):
    def __init__(self, retry=0):
        self.retry = retry
        self.gateway_type = None

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def connect(self, gateway_type=None, details=None):
        if gateway_type is not None:
            if self.authenticate(details):
                return True
        return False

    def authenticate(self, details=None):
        if details is not None:
            return True
        return False

    def pay(self, amount, user_details=None, gateway_type=None):
        if gateway_type is None:
            gateway_type = self.gateway_type
        while self.retry + 1 > 0:
            if self.connect(gateway_type, user_details):
                Logger.info(
                    "payment of {} in gateway_type {} successful".format(
                        amount, self.gateway_type
                    )
                )
                return True
            self.retry -= 1
        return False

from controller import CreditCardController, IndexController


def register_urls(api):
    api.add_resource(IndexController, "/")
    api.add_resource(CreditCardController, "/ProcessPayment")

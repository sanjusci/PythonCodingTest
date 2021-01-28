from flask import request, abort
from flask_restful import Resource

from logger import Logger
from services import CreditCard, ExternalService


class CreditCardController(Resource):
    def post(self):
        data = request.get_json(force=True)
        if not data:
            # abort(400)
            return {"status_code": 400}, 400

        card_obj = CreditCard()
        Logger.info("request data {}".format(data))
        try:
            if not card_obj.validate_card_details(**data):
                Logger.info("Card data invalid")
                # abort(400)
                return {"status_code": 400}, 400
        except Exception as e:
            Logger.exception(e)
            # abort(400)
            return {"status_code": 500}, 500
        try:
            Logger.info("Payment status started")
            payment_status = ExternalService(card_obj.Amount, card_obj)
            Logger.info("Payment process started")

            payment_successful = payment_status.make_payment()
            if payment_successful:
                return {"status_code": 200}, 200
            else:
                # abort(400)
                return {"status_code": 400}, 400
        except Exception as e:
            Logger.exception(e)
            # abort(500)
            return {"status_code": 500}, 500

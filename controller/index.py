import json

from flask_restful import Resource


class IndexController(Resource):
    def get(self):
        return json.dumps(
            {"message": "Welcome to Credit Card Testing Application:TEST-API"}
        )

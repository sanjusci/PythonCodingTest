import unittest
import requests
import json


class TestCreditCard(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        self.url = "http://{}:{}/ProcessPayment".format("localhost", 5000)
        self.headers = {"Content-Type": "application/json"}
        with open("../data/input.json") as f:
            self.data = json.load(f)
        super(TestCreditCard, self).__init__(methodName)

    def test_invalid_request_type(self):
        res = requests.get(self.url)
        self.assertEqual(res.status_code, 405, "Invalid request type")

    def test_credit_card_with_no_data(self):
        data = {}
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Credit card with no data")

    def test_check_mandatory_field(self):
        data = self.data["missing_key_credit_card"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Missing credit card key")

    def test_invalid_key_argument(self):
        data = self.data["invalid_key_credit_card"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Invalid credit card key")

    def test_invalid_value(self):
        data = self.data["invalid_value_credit_card"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Invalid credit card value")

    def test_expire_credit_card(self):
        data = self.data["expire_credit_card"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Expire credit card")

    def test_invalid_security_code(self):
        data = self.data["invalid_security_code"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Invalid security code")

    def test_security_code(self):
        data = self.data["invalid_security_code"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Invalid security code")

    def test_invalid_amount(self):
        data = self.data["invalid_amount"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Invalid credit card amount")

    def test_negative_amount(self):
        data = self.data["negative_amount"]
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(res.status_code, 400, "Negative credit card amount")

    def test_Payment_Rule(self):
        cheap_card_data = self.data["valid_credit_card_1"]
        expensive_card_data = self.data["valid_credit_card_2"]
        premium_card_data = self.data["valid_credit_card_3"]
        res1 = requests.post(
            url=self.url, data=json.dumps(cheap_card_data), headers=self.headers
        )
        res2 = requests.post(
            url=self.url, data=json.dumps(expensive_card_data), headers=self.headers
        )
        res3 = requests.post(
            url=self.url, data=json.dumps(premium_card_data), headers=self.headers
        )
        self.assertEqual(res1.status_code, 200, "Cheap credit card amount")
        self.assertEqual(res2.status_code, 200, "Expensive credit card amount")
        self.assertEqual(res3.status_code, 200, "Premium credit card amount")


if __name__ == "__main__":
    unittest.main()

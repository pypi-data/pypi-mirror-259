import json
import requests
from flask import Flask, request, jsonify

class BoxPaySDK:
    def __init__(self, merchant_id, api_key, base_url="https://apis.boxpay.tech/v0"):
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.base_url = base_url
        self.checkout_url = f"{base_url}/merchants/{self.merchant_id}/sessions"
        self.verify_url = f"{base_url}/merchants/{self.merchant_id}/transactions/inquiries"

    def create_checkout_session(self, order_id, currency, country_code, unique_reference, frontend_back_url, amount, legal_entity=None, **kwargs):
        self._validate_mandatory(order_id, "order_id")
        self._validate_mandatory(currency, "currency")
        self._validate_mandatory(country_code, "country_code")
        self._validate_mandatory(unique_reference, "unique_reference")

        payload = {
            "context": {
                "legalEntity": {
                    "code": legal_entity
                } if legal_entity else {},
                "countryCode": country_code,
                "orderId": order_id,
                **kwargs.get("context", {})
                
            },
            "paymentType": "S",
            "shopper": {
                "uniqueReference": unique_reference,
                **kwargs.get("shopper", {})
            },
            "order": {
                **kwargs.get("order", {})
            },
            "frontendReturnUrl": kwargs.get("frontendReturnUrl", ""),
            "frontendBackUrl": frontend_back_url,
            "statusNotifyUrl": kwargs.get("statusNotifyUrl", ""),
            "shopperAuthentication": {
                "threeDSAuthentication": kwargs.get("threeDSAuthentication", "Yes")
            },
            "money": {
                "amount": amount,
                "currencyCode": currency
            },
            **kwargs
        }

        headers = {
            'Authorization': f'{self.api_key}',
            'Content-Type': 'application/json'
        }

        response = requests.post(self.checkout_url, headers=headers, data=json.dumps(payload))
        return response.json()

    def verify_payment(self, token, inquiry_details):
        payload = {
            "token": token,
            "inquiryDetails": inquiry_details
        }

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        response = requests.post(self.verify_url, headers=headers, data=json.dumps(payload))
        return response.json()

    def _validate_mandatory(self, value, field_name):
        if not value or value == "":
            raise ValueError(f"{field_name} is mandatory and should not be an empty string.")

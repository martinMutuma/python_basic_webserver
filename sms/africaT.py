import africastalking
import os

username = os.environ.get("AFRICATAlKING_USERNAME", 'sandbox')
api_key = os.environ.get("AFRICATAlKING_API_KEY", "Key")
africastalking.initialize(username, api_key)


class SendSMS():
    def __init__(self, message="Hello Martin here", phone=['+254717436112']):
        self.sms = africastalking.SMS
        self.sms.send(message, phone)

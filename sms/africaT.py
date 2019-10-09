import africastalking
import os

username = os.environ.get("AFRICATAlKING_USERNAME", 'sandbox')
api_key = os.environ.get("AFRICATAlKING_API_KEY", "Key")
africastalking.initialize(username, api_key)


class SendSMS():
    def __init__(self, message="Hello Martin here", phone=['+254717436112']):
        self.sms = africastalking.SMS
        print("sending message to {}".format(phone))
        print(api_key, username)
        self.sms.send(message, phone)


def after_send(error=None, response=''):
    if error is not None:
        print(error)
    print(response)


def test(message="Hello Martin here", phone=['+254717436112']):
    sms = africastalking.SMS
    print("sending message to {}".format(phone))
    sms.send(message, phone)

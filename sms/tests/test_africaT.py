from unittest import mock
import africastalking
from sms.africaT import SendSMS


@mock.patch('africastalking.SMS', autospec=True)
def test_SendSMS_calls_africa_talkin_SMS(mocked_class):
    SendSMS()
    mocked_class.send.assert_called()
    mocked_class.send.assert_called_with(
        "Hello Martin here", ['+254717436112'])

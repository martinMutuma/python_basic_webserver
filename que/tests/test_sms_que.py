from fakeredis import FakeStrictRedis
from unittest import TestCase, mock
from ..sms_que import EnqueSMS, process_que
from sms.africaT import SendSMS

message = {'message': "This is a test message",
           'phone': ['+254717436112']}


class TestSMSQue(TestCase):
    def test_message_que(self):
        test_que = EnqueSMS(message, FakeStrictRedis())
        assert len(test_que.que.jobs) == 1


with mock.patch.object(SendSMS, '__init__', return_value=None) as mock_method:
    process_que(message)


def test_sms_processor():
    assert mock_method.called

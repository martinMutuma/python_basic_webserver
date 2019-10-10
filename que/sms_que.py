from redis import Redis
from rq import Queue
import json
from sms.africaT import SendSMS
import time
import os

url = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

redis_conn = Redis().from_url(url)


class EnqueSMS():
    def __init__(self, message='', connec=redis_conn):
        self.que = self.create_que(connec)
        self.que.enqueue(process_que, message)

    def create_que(self, conn):
        return Queue(connection=conn)


def process_que(message):
    data = message
    SendSMS(message=data['message'], phone=data['phone'])

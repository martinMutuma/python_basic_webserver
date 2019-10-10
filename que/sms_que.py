from redis import Redis
from rq import Queue
import json
from sms.africaT import SendSMS, test
import time
import os

url = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

conn = Redis().from_url(url)
que = Queue(connection=conn)


def enque(message=''):
    job = que.enqueue(process_que, message)
    time.sleep(2)
    print(job.result)


def process_que(message):
    data = message
    SendSMS(message=data['message'], phone=data['phone'])

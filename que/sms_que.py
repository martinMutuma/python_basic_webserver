from redis import Redis
from rq import Queue
import json
from sms.africaT import SendSMS, test
import time


conn = Redis()
que = Queue(connection=conn)


def enque(message=''):
    job = que.enqueue(process_que, message)
    time.sleep(2)
    print(job.result)


def process_que(message):
    data = message
    SendSMS(message=data['message'], phone=data['phone'])

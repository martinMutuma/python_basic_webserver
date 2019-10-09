import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        from dotenv import load_dotenv
        load_dotenv('./env')
        worker = Worker(map(Queue, listen))
        worker.work()


from http.server import HTTPServer
from server.basic import APIServiceHandler
import os

from dotenv import load_dotenv
load_dotenv()
port = int(os.getenv('PORT', 5000))
server = HTTPServer(('0.0.0.0', port), APIServiceHandler)
server.serve_forever()

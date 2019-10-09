
from http.server import HTTPServer
from server.basic import APIServiceHandler

from dotenv import load_dotenv
load_dotenv()

server = HTTPServer(('', 5000), APIServiceHandler)
server.serve_forever()

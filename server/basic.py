from http.server import BaseHTTPRequestHandler, HTTPStatus
from que.sms_que import EnqueSMS
import json
from urllib.parse import parse_qs
from helpers.utils import validate_data, validate_phones
import os


class APIServiceHandler(BaseHTTPRequestHandler):
    def _parse_data(self):
        length = int(self.headers['content-length'])
        field_data = self.rfile.read(length)
        try:
            data = json.loads(field_data.decode())
        except:
            self._standard_response(
                HTTPStatus.BAD_REQUEST, "Could not get data")
            data = {}
        return data

    def _standard_response(self, status_code=200, data=""):
        self.send_response(status_code)
        self.send_header("Content_type", 'application/json')
        self.end_headers()
        if type(data) != str:
            data = json.dumps(data)
        self.wfile.write(data.encode())
        self.wfile.flush()

    def do_GET(self):
        root = os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), 'static')

        filename = root + '/index.html'

        self.send_response(HTTPStatus.OK)
        self.send_header("Content_type", 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)

    def do_POST(self):
        if self.path == "/sms":
            raw_data = self._parse_data()
            errors = validate_data(raw_data)
            if len(errors) == 0:
                phones = raw_data['phone'].replace(" ", "").split(',')
                valid_phones = validate_phones(phones)
                if len(raw_data['message'].rstrip()) > 1 and len(valid_phones['phones']) > 0:
                    data = dict(
                        message=raw_data['message'], phone=valid_phones['phones'])
                    EnqueSMS(data)
                    if len(valid_phones['errors']) > 0:
                        msg = "Numbers {} will recieve your message, however {} cannot be validated".format(
                            valid_phones['phones'], valid_phones['errors'])
                    else:
                        msg = 'Success, Message Queued for Sending'
                    message = {'message': msg}
                    self._standard_response(HTTPStatus.OK, message)

            else:
                self._standard_response(HTTPStatus.BAD_REQUEST, errors)
        else:
            message = {"error": "Page not found"}
            self._standard_response(404, message)

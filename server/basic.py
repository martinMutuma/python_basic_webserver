from http.server import BaseHTTPRequestHandler, HTTPStatus
from que.sms_que import enque, process_que
import json
from urllib.parse import parse_qs
from helpers.utils import validate_data


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
        self.send_response(HTTPStatus.OK)
        self.send_header("Content_type", 'application/json')
        self.end_headers()
        data = {"data": "Well this works 3",
                "message": "Welcome to Martins Basic Python http server without any frameworks"}
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        if self.path == "/sms":
            raw_data = self._parse_data()
            errors = validate_data(raw_data)
            if len(errors) == 0:
                phones = raw_data['phone'].replace(" ", "").split(',')
                data = {'message': raw_data['message'], 'phone': phones}
                enque(data)
                message = {'message': "Success, Message Queued for Sending"}
                self._standard_response(HTTPStatus.OK, message)
            else:
                self._standard_response(HTTPStatus.BAD_REQUEST, errors)
        else:
            message = {"error": "Page not found"}
            self._standard_response(404, message)

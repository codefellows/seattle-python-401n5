from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # http://localhost:3000/api/aloha?name=Roger
        s = self.path
        print(s)
        url_components = parse.urlsplit(s)
        print(url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        print(query_string_list)
        dic = dict(query_string_list)

        name = dic.get("name")

        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stranger"

        message += f"\nGreetings from Python version {platform.python_version()}"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())


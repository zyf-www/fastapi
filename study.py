from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "username": "原神",
    "password": "nb"
}
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            body = json.dumps(profile,ensure_ascii=False)
            self.wfile.write(body.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
HTTPServer(("", 8000), MyServer).serve_forever()
#!/usr/bin/python3

import http.server
import socketserver
import os

PORT = 8000

class ExtendedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, **kwargs)

    def do_PUT(self):
        """Serve a PUT request."""
        path = self.translate_path(self.path)
        length = int(self.headers["Content-Length"])
        if False: # for future input validation
            pass
        else:
            with open(path, 'wb') as fh:
                fh.write(self.rfile.read(length))
            self.send_response(200, "OK")
            self.end_headers()

if __name__ == '__main__':
    Handler = ExtendedHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("[*] Running python http server on port", PORT)
        httpd.serve_forever()
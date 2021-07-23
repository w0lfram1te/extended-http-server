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
        print("[*] receiving PUT request")
        # filename validation - check if file exists if yes increment

        path = self.translate_path(self.path)
        f = None

        print(path)     
        # if not os.path.exists:
            # # support for file name modification will come later
            # print("[-] file path already exists")
            # self.send_error(500)
            # return

        try:
            f = open(path, 'wb')

        except OSError:
            print("[-] file opening died")
            self.send_error(500)
            return

        try:
            self.copyfile(self.rfile, f)
            print("done copying")
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            f.close()
            return
        except:
            f.close()
            return

if __name__ == '__main__':
    Handler = ExtendedHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("[*] Running python http server on port", PORT)
        httpd.serve_forever()
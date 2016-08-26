from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from lib.requests import request_handler

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parsed_path.query

        message = 'Visiting %s' % path

        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))
        return

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

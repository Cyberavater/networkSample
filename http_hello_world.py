from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Hello, World!"
        self.wfile.write(bytes(message, "utf8"))
        return


def run_http_server():
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running HTTP server...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_http_server()

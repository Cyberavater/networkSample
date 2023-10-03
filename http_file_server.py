import http.server
import socketserver
import os

ip_address = "192.168.0.8"
PORT = 8000
DIRECTORY = r"C:\Users\Cyber\test"

os.chdir(DIRECTORY)


def main():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((ip_address, PORT), Handler) as httpd:
        print(f"serving at port {PORT} from {DIRECTORY}")
        httpd.serve_forever()


if __name__ == '__main__':
    main()

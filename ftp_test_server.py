from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # Instantiate a dummy authorizer to manage 'virtual' users
    authorizer = DummyAuthorizer()

    ftp_directory = input("Paste the directory which you want to serve via FTP:")
    # Define a new user having full r/w permissions
    authorizer.add_user('user', '12345', ftp_directory, perm='elradfmwMT')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a new FTP server on the default address (0.0.0.0) and port (2121)
    server = FTPServer(('0.0.0.0', 21), handler)

    print("Use ipconfig to get the local IP where FTP is served to access it")
    # Start the FTP server
    server.serve_forever()


if __name__ == '__main__':
    main()

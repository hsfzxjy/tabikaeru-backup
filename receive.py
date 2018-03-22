#!/usr/bin/env python3

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    authorizer = DummyAuthorizer()

    target = os.path.join(os.path.dirname(__file__), 'archives')

    if not os.path.isdir(target):
        os.mkdir(target)

    authorizer.add_user('admin', '12345', target, perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "pyftpdlib based ftpd ready."

    address = ('', 2121)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()

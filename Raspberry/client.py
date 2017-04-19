#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncore
import socket
import time
from settings import *


class Client(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.msg = "Hello, I'm Client"

    def handle_connect(self):
        print "connected"

    def handle_close(self):
        print "closed"
        self.close()

    def handle_read(self):
        print(self.recv(1024))

    def handle_error(self):
        print "Server is closed..."

    def writable(self):
        return True

    def handle_write(self):
        sent = self.send(self.msg)
        time.sleep(1)


if __name__ == "__main__":
    client = Client(HOST, PORT)
    asyncore.loop()

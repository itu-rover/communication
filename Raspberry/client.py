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
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(1024))

    def writable(self):
        return True

    def handle_write(self):
        sent = self.send(self.msg)
        time.sleep(2)


if __name__ == "__main__":
    client = Client(HOST, PORT)
    asyncore.loop()

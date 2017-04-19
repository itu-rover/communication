#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncore
import socket
import time
from settings import *


class EchoHandler(asyncore.dispatcher_with_send):
    serial_data = None

    def writable(self):
        return True

    def handle_write(self):
        if self.serial_data:
            sent = self.send(self.serial_data)
            time.sleep(0.1)

    def handle_read(self):
        self.data = self.recv(1024)


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = "123"
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        print "listening"

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            self.handler = EchoHandler(sock)


if __name__ == "__main__":
    server = EchoServer(HOST, PORT)
    asyncore.loop()

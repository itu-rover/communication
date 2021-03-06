#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncore
import logging
import socket
import time
from settings import *


class Client(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info('Create client')
        self.connect((host, port))
        self.msg = "Hello, I'm Client"
        self.is_writable = True

    def handle_connect(self):
        logging.info('Client is connected')
        print "connected"

    def handle_close(self):
        logging.info('Client is disconnected')
        print "closed"
        self.close()

    def handle_read(self):
        self.data = self.recv(1024)
        print(self.data[:-1])
        logging.info('Read: "%s"', self.data[:-1])

    def handle_error(self):
        print("Server is closed...")
        logging.error('Server is closed!')

    def writable(self):
        self.is_writable = not self.is_writable
        return self.is_writable

    def handle_write(self):
        sent = self.send(self.msg)
        logging.info('Send a message: "%s"', self.msg)


if __name__ == "__main__":
    logging.basicConfig(filename='logs/client.log',
                        filemode='a',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)
    logging.info('Start')
    client = Client(HOST, PORT)
    asyncore.loop(timeout=1)
    logging.info('Finish')

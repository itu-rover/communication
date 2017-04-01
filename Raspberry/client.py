#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket()
        self.socket.connect((host, port))

    def run(self):
        while True:
            try:
                print(self.socket.recv(1024))
                self.socket.send("Selam Pi")
            except Exception:
                print("Socket closing...")
                socket.close()
                sys.exit()

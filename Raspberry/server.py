#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import atexit


class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.msg = None
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((host, port))
        self.run()

    def run(self):
        while True:
            try:
                serversocket.listen(5)
                clientsocket, addr = serversocket.accept()
                print("Got a connection from %s" % str(addr))
            while True:
                try:
                    if self.msg:
                        clientsocket.send(self.msg.encode('ascii'))
                    self.data = clientsocket.recv(1024)
                    time.sleep(.5)
                except Exception:
                    break
            except Exception:
                pass

    @atexit.register
    def exit_handler():
        clientsocket.close()
        print("Server closing")

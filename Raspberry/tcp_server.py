#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.42.0.69'
port = 1234

server.bind((host, port))
server.listen(5)

while True:
    client, addr = server.accept()
    print("Got a connection from %s" % str(addr))

    current_time = time.ctime() + "\r\n"
    client.send(current_time.encode('ascii'))

    data = client.recv(1024)
    print(data)

    client.close()

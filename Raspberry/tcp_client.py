#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = '10.42.0.69'
port = 1234

while True:
    client = socket.socket()
    client.connect((host, port))
    print(client.recv(1024))
    client.send("Selam Pi")
    client.close()

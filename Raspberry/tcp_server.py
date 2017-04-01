#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import atexit


@atexit.register
def exit_handler():
    clientsocket.close()
    print("Server closing")


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = ''

port = 1234

# bind to the port
serversocket.bind((host, port))


while True:
    try:
        serversocket.listen(5)
        clientsocket, addr = serversocket.accept()
        print("Got a connection from %s" % str(addr))
        while True:
            try:
                sensor_msg = "12,12,12,12,12,12" + "\n"
                clientsocket.send(sensor_msg.encode('ascii'))
                data = clientsocket.recv(1024)
                print(data)
                time.sleep(.5)
            except Exception:
                break
    except Exception:
        pass

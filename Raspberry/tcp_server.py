#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import atexit

def exit_handler():
   clientsocket.close()
   print("Server closing")
atexit.register(exit_handler)

# create a socket object
serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)


# serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# get local machine name
host = ''

port = 1234

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

# establish a connection
# This should be in while if more clients are available
clientsocket,addr = serversocket.accept()
print("Got a connection from %s" % str(addr))
while True:
    sensor_msg = "12,12,12,12,12,12" + "\r"
    clientsocket.send(sensor_msg.encode('ascii'))
    data = clientsocket.recv(1024)
    print(data)
    time.sleep(.5)

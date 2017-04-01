#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = '10.42.0.69'
port = 1234
s = socket.socket()
s.connect((host,port))
while True:
	try:
		print(s.recv(1024))
		s.send("Selam Pi")
	except Exception:
		print("Error, socket closing")
		s.close()	
		quit()

import socket


host = '10.42.0.69'
port = 1234
while True:
	s = socket.socket()
	s.connect((host,port))
	print(s.recv(1024))
	s.send("Selam Pi")	
	s.close()

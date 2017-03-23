import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''

port = 1234

serversocket.bind((host, port))

serversocket.listen(5)

while True:
	clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    data = clientsocket.recv(1024)
    print data
    clientsocket.close()

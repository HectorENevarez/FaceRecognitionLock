import socket

s = socket.socket()
host = socket.gethostname()
port = 6666
s.bind((host,port))

f = 

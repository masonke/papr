import socket


#connects to server
s = socket.socket()
host = '127.0.0.1'
port = 9999
s.connect((host, port))

#gets chat
while True:
    data = s.recv(1024)
    print (data[:].decode("utf-8")) 
    chat = input()
    s.send(str.encode(chat))
    
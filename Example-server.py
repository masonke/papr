import socket

def socket_create():
try:

    global host
    global port
    global s
    host = ''
    port = 9999
    s = socket.socket()

except socket.error as msg:
    print("Socket creation error" + str(msg))

#Wait for client, Connect socket and port
def socket_bind():
try:
    global host
    global port
    global s
    print("Binding socket to port: " + str(port)) 
    s.bind((host, port))
    s.listen(5)
except socket.error as msg:
    print("Socket binding error" + str(msg) + "\n" + "Retrying...")
    socket_bind

#Accept connections (Establishes connection with client) socket has to       be listining
def socket_accept():
   conn, address = s.accept()
   print("Connection is established |" + " IP:" + str(address[0]) + "|    port:" + str(address[1]))
chat_send(conn)


def chat_send(conn):
 while True:
    chat =input()
    if len(str.encode(chat)) > 0:
        conn.send(str.encode(chat))
        client_response = str(conn.recv(1024), "utf-8")
    print(client_response)
def main():
socket_create()
socket_bind()
socket_accept()

main()

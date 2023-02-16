import socket

def get_json_bytes(json_string):
    return bytes((json_string + '\n'), 'utf-8')

def json_send_recv(s, json) -> str:
    s.sendall(get_json_bytes(json))
    data = s.recv(1024)
    return data[:-4].decode('utf-8')

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print('c: Connecting to /tmp/sharkd.sock')
s.connect("/tmp/sharkd.sock")

json_string = '{"jsonrpc":"2.0","id":1,"method":"load","params":{"file":"/tmp/small.pcapng"}}'
print('s: ' + json_string)
recv_json = json_send_recv(s, json_string)
print('r: ' + recv_json)

json_string = '{"jsonrpc":"2.0","id":2,"method":"status"}'
print('s: ' + json_string)
rx_json = json_send_recv(s, json_string)
print('r: ' + rx_json)

print('c: Closing connection to /tmp/sharkd.sock')

s.close()



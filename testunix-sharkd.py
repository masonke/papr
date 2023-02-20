import socket
import sys
import os

# https://wiki.wireshark.org/sharkd-JSON-RPC-Request-Syntax
# https://stackoverflow.com/questions/20777173/add-variable-value-in-a-json-string-in-python


def get_json_bytes(json_string):
    return bytes((json_string + '\n'), 'utf-8')

def json_send_recv(s, json) -> str:
    s.sendall(get_json_bytes(json))
    data = s.recv(1024)
    return data[:-4].decode('utf-8')

uds_server_address = '/private/tmp/sharkd.sock'
pcap_name = '/tmp/small.pcapng'

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print('c: Connecting to ' + uds_server_address)
s.connect(uds_server_address)

json_string = '{"jsonrpc":"2.0","id":1,"method":"load","params":{"file":"pcap_name"}}'
print('s: ' + json_string)

recv_json = json_send_recv(s, json_string)
print('r: ' + recv_json)

json_string = '{"jsonrpc":"2.0","id":2,"method":"status"}'
print('s: ' + json_string)

rx_json = json_send_recv(s, json_string)
print('r: ' + rx_json)

print('c: Closing connection to ' + uds_server_address)

s.close()



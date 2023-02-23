import socket
import sys
import os

# https://wiki.wireshark.org/sharkd-JSON-RPC-Request-Syntax
# https://stackoverflow.com/questions/20777173/add-variable-value-in-a-json-string-in-python
#https://wiki.wireshark.org/sharkd-Info-Request-Output-Example


uds_server_address = '/private/tmp/sharkd.sock'
pcap_name = '/private/tmp/small.pcapng'

# Clear the old server socket
# if [[ -e /tmp/sharkd.sock ]] ; then
#   rm /tmp/sharkd.sock
# fi

def get_json_bytes(json_string):
    return bytes((json_string + '\n'), 'utf-8')

# Increased receive size to 32K to capture all the payload.
# If received data is cut off, increase this value.
def json_send_recv(s, json) -> str:
    s.sendall(get_json_bytes(json))
    data = s.recv(32768)
    return data[:-4].decode('utf-8')

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print('c: Connecting to ' + uds_server_address)
try:
	s.connect(uds_server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

# Load the pcap file
json_string = '{"jsonrpc":"2.0","id":1,"method":"load","params":{"file":"'+pcap_name+'"}}'
print('s: ' + json_string)

recv_json = json_send_recv(s, json_string)
print('r: ' + recv_json)

# Get the staus of the pcap
json_string = '{"jsonrpc":"2.0","id":2,"method":"status"}'
print('s: ' + json_string)

rx_json = json_send_recv(s, json_string)
print('r: ' + rx_json)

json_string = '{"jsonrpc":"2.0","id":2,"method":"analyse"}'
print('s: ' + json_string)

rx_json = json_send_recv(s, json_string)
print('r: ' + rx_json)

# https://wiki.wireshark.org/sharkd-JSON-RPC-Request-Syntax#tap
json_string = '{"jsonrpc":"2.0","id":2,"method":"tap","params":{"tap0":"expert"}}'
print('s: ' + json_string)

rx_json = json_send_recv(s, json_string)
print('r: ' + rx_json)

json_string = '{"jsonrpc":"2.0","id":2,"method":"tap","params":{"tap0":"seqa:tcp"}}'
print('s: ' + json_string)

rx_json = json_send_recv(s, json_string)
print('r: ' + rx_json)

print('c: Closing connection to ' + uds_server_address)

s.close()



import socket


HOST = 'daring.cwi.nl'
PORT = 50007

with socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM
        ) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello World')
    data = s.recv(1024)
print('Received', repr(data))

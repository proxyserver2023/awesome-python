#!/usr/bin/env python3

"""
TCP:
----
1. packets dropped in the network are detected and retransmitted by the sender.
2. data is read by your application in the order it was written by the sender.

UDP:
----
1. aren't reliable.
2. data read by receivers can be out of order from the sender's writes.

Server 
------
socket > bind > listen > accept > recv > send > recv > close

Client
-----
socket -> connect -> send -> recv -> close
"""

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

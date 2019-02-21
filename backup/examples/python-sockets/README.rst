Python Sockets
==============

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

#!/usr/bin/python

import socket
import os
s = socket.socket()                                     # Server socket, get msg from client
host = os.popen("hostname -I").read().strip()           # get server's IP
port = 11414                                            # specify getting msg socket
s.bind((host, port))                                    # bind them.
s.listen(5)                                             # listen the msg from the client and
client,client_addr = s.accept()                         # get the client's addr.
while True:
    print('get msg from: ', client_addr)
    recvmsg=client.recv(1024)                           # received message.
    client.close()
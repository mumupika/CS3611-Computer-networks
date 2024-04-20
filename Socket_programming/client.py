#!/usr/bin/python
import socket
import os
server_host="10.0.0.4"                                      # this is the server's IP, stands for h4.
server_port=11414                                           # sending port;

from_server_socket=socket.socket()
host = os.popen("hostname -I").read().strip()           # get server's IP
port = 4096                                            # specify getting msg socket
from_server_socket.bind((host,port))
from_server_socket.listen(10)                                  # listen the msg from the client.
while True:
    server=socket.socket()
    sendmsg=''
    mode=input("Input 'send' to send a msg and hear from server, input 'hear' to listen from server, input 'quit' to shut the client.\n")
    if mode=='send':
        server.connect((server_host,server_port))           # establish connection
        connected_flag=0
        sendmsg=input('Please input in the formula as: To hx:Hello\n')
        server.send(sendmsg.encode())                       # send encoded msg
        mode='hear'
    if mode=='hear':
        from_server,from_server_addr=from_server_socket.accept()
        recvmsg=from_server.recv(2048)
        recvmsg=recvmsg.decode()
        print(recvmsg)
    if mode=='quit':
        server.close()
        from_server_socket.close()
        break
    server.close()
#!/usr/bin/python

import socket
import os
server=socket.socket()
server_host="10.0.0.4"                                      # this is the server's IP, stands for h4.
server_port=11414                                           # sending port;
client_address=os.popen('hostname -I').read().strip()       # Socket cannot get the mininet ip. Try shell instead.
client=socket.socket()                                      # Client receiving socket for receive msg from server.
client_port=4096                                            # receiving socket port
client.bind((client_address,client_port))                   # Bind them together.
client.listen(5)                                            # Hear the echo from the server
connected_flag=1
while True:
    sendmsg=''
    mode=input("Input 'Send' to send a msg and hear from server and Input 'hear' to listen from server\n")
    if mode=='send':
        server.connect((server_host,server_port))           # establish connection
        connected_flag=0
        sendmsg=input('Please input in the formula as: To hx:Hello\n')
        server.send(sendmsg.encode())                       # send encoded msg
    
    '''After sending message, the client should:
    1. Judge the sending message to determine waiting for calls.
    2. Waiting for calls: Change ourself into the listener.
    '''
    
    if mode=='quit':
        server.close()                                      # close connection.
        client.close()
        connected_flag=1
    if mode=='hear':
        receive_from_server,receive_from_addr=client.accept()
        receive_msg=receive_from_server.recv(1024).decode()     # Decode the msg.
        if len(receive_msg)<0 or receive_msg[0]=='E':                                 # stands for error
            print("Message format error! Please repeat.")
            break
        else:                                                   # get the msg from the correct server.
            print(receive_msg)                                  
            print("Successfully get message. Terminate.")
            break
    print("Successfully sent. Terminate...")
    server.close()
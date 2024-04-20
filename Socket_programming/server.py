#!/usr/bin/python
import socket
import os
bind_flag=1
s = socket.socket()                                     # Server socket, get msg from client
host = os.popen("hostname -I").read().strip()           # get server's IP
port = 11414                                            # specify getting msg socket
s.bind((host,port))
s.listen(10)                                             # listen the msg from the client.

send_to_port=4096

while True:
    client,client_addr = s.accept()                         # get the client's addr.
    print('get msg from: ', client_addr)
    recvmsg=client.recv(1024)                           # received message.
    recvmsg=recvmsg.decode()                            # byte to string.
    if recvmsg=='quit':
        client.close()                                  # close connection
        break
    print(recvmsg)
    print(len(recvmsg))
    
    
    if len(recvmsg)<7:
        send_to_addr=client_addr[0]
        send_to=socket.socket()
        send_to_msg="Wrong format: Target host Undefined!"
        print("send back...")
        send_to.connect((send_to_addr,send_to_port))
        send_to.send(send_to_msg.encode())
        send_to.close()
        
    elif recvmsg[4]=='1':
        send_to_addr="10.0.0.1"
        send_to=socket.socket()
        if client_addr[0]=='10.0.0.1':
            send_to_msg=recvmsg[6:] + ' from h1'
        elif client_addr[0]=='10.0.0.2':
            send_to_msg=recvmsg[6:] + ' from h2'
        elif client_addr[0]=='10.0.0.3':
            send_to_msg=recvmsg[6:] + ' from h3'
        elif client_addr[0]=='10.0.0.4':
            send_to_msg=recvmsg[6:] + ' from h4'
        print("send to h1...")
        send_to.connect((send_to_addr,send_to_port))
        send_to.send(send_to_msg.encode())
        send_to.close()
    
    elif recvmsg[4]=='2':
        send_to_addr="10.0.0.2"
        send_to=socket.socket()
        if client_addr[0]=='10.0.0.1':
            send_to_msg=recvmsg[6:] + ' from h1'
        elif client_addr[0]=='10.0.0.2':
            send_to_msg=recvmsg[6:] + ' from h2'
        elif client_addr[0]=='10.0.0.3':
            send_to_msg=recvmsg[6:] + ' from h3'
        elif client_addr[0]=='10.0.0.4':
            send_to_msg=recvmsg[6:] + ' from h4'
        print("send to h2...")
        send_to.connect((send_to_addr,send_to_port))
        send_to.send(send_to_msg.encode())
        send_to.close()
        
    elif recvmsg[4]=='3':
        send_to_addr="10.0.0.3"
        send_to=socket.socket()
        if client_addr[0]=='10.0.0.1':
            send_to_msg=recvmsg[6:] + ' from h1'
        elif client_addr[0]=='10.0.0.2':
            send_to_msg=recvmsg[6:] + ' from h2'
        elif client_addr[0]=='10.0.0.3':
            send_to_msg=recvmsg[6:] + ' from h3'
        elif client_addr[0]=='10.0.0.4':
            send_to_msg=recvmsg[6:] + ' from h4'
        print("send to h3...")
        send_to.connect((send_to_addr,send_to_port))
        send_to.send(send_to_msg.encode())
        send_to.close()
    
    elif recvmsg[4]=='4':
        send_to_addr="10.0.0.4"
        send_to=socket.socket()
        if client_addr[0]=='10.0.0.1':
            send_to_msg=recvmsg[6:] + ' from h1'
        elif client_addr[0]=='10.0.0.2':
            send_to_msg=recvmsg[6:] + ' from h2'
        elif client_addr[0]=='10.0.0.3':
            send_to_msg=recvmsg[6:] + ' from h3'
        elif client_addr[0]=='10.0.0.4':
            send_to_msg=recvmsg[6:] + ' from h4'
        print("send to h4...")
        send_to.connect((send_to_addr,send_to_port))
        send_to.send(send_to_msg.encode())
        send_to.close()
    
    else:
        send_to_addr=client_addr[0]
        send_to=socket.socket()
        send_to_msg="Wrong format: Target host Undefined!"
        print("send back...")
        send_to.connect((send_to_addr,send_to_port))
        send_to.send(send_to_msg.encode())
        send_to.close()
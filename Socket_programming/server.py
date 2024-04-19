#!/usr/bin/python

import socket
import os
s = socket.socket()                                     # Server socket, get msg from client
host = os.popen("hostname -I").read().strip()           # get server's IP
port = 11414                                            # specify getting msg socket
s.bind((host, port))                                    # bind them.
s.listen(10)
while True:
    send_to_client=socket.socket()                          # Server send msg socket.
    #s.listen(5)                                             # listen the msg from the client and
    client,client_addr = s.accept()                         # get the client's addr.
    print('get msg from: ', client_addr)
    recvmsg=client.recv(1024)                           # received message.
    recvmsg=recvmsg.decode()                            # byte to string.
    if recvmsg=='quit':
        client.close()                                  # close connection
        break
    print(recvmsg)
    print(len(recvmsg))
    '''The sending formula is "To hx:[Contents]".
    When the formula is not correct, that is, recvmsg[4] is not 1,2,3;
    Then send error msg to client and keep connecting.
    '''
    
    if  len(recvmsg)<7:
        send_to_client.connect((client_addr[0],4096))        # connect with the receiving socket in client.
        send_to_client.send("Error! Format incorrect. No hosts founded.".encode())
        send_to_client.close()                          # close the connection.
        break

    else:
        if recvmsg[4]=='1':
            send_to_addr='10.0.0.1'
            send_to_client.connect((send_to_addr,4096))
            if client_addr[0]=='10.0.0.1':
                send_msg=recvmsg[6:]+' From h1'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.2':
                send_msg=recvmsg[6:]+' From h2'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.3':
                send_msg=recvmsg[6:]+' From h3'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.4':
                send_msg=recvmsg[6:]+' From h4'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
        
        elif recvmsg[4]=='2':
            send_to_addr='10.0.0.2'
            send_to_client.connect((send_to_addr,4096))
            if client_addr[0]=='10.0.0.1':
                send_msg=recvmsg[6:]+' From h1'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.2':
                send_msg=recvmsg[6:]+' From h2'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.3':
                send_msg=recvmsg[6:]+' From h3'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.4':
                send_msg=recvmsg[6:]+' From h4'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
        
        elif recvmsg[4]=='3':
            send_to_addr='10.0.0.3'
            send_to_client.connect((send_to_addr,4096))
            if client_addr[0]=='10.0.0.1':
                send_msg=recvmsg[6:]+' From h1'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.2':
                send_msg=recvmsg[6:]+' From h2'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.3':
                send_msg=recvmsg[6:]+' From h3'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.4':
                send_msg=recvmsg[6:]+' From h4'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
        
        elif recvmsg[4]=='4':
            send_to_addr='10.0.0.4'
            send_to_client.connect((send_to_addr,4096))
            if client_addr[0]=='10.0.0.1':
                send_msg=recvmsg[6:]+' From h1'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.2':
                send_msg=recvmsg[6:]+' From h2'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.3':
                send_msg=recvmsg[6:]+' From h3'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
            elif client_addr[0]=='10.0.0.4':
                send_msg=recvmsg[6:]+' From h4'
                send_to_client.send(send_msg.encode())
                send_to_client.close()
        else:
            #send_to_client.connect((client_addr[0],4096))        # connect with the receiving socket in client.
            send_to_client.send("Error! Format incorrect. No hosts founded.".encode())
            send_to_client.close()                          # close the connection.
            break
    print("Service over. Terminating...")
    break
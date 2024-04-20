import socket
import struct
import time

def traceroute(hostaddr):
    dest_addr = hostaddr
    port = 11414
    max_hops = 8
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.bind(("", port))
        send_socket.sendto(b"", (hostaddr, port))
        current_addr = None
        current_name = None
        try:
            # receive packet
            data, current_addr = recv_socket.recvfrom(512)
            current_addr = current_addr[0]
            try:
                current_name = socket.gethostbyaddr(current_addr)[0]
            except socket.error:
                current_name = current_addr
        except socket.error:
            pass
        finally:
            send_socket.close()
            recv_socket.close()

        if current_addr is not None:
            current_host = f"{current_name} ({current_addr})"
        else:
            current_host = "*"

        print(f"{ttl}\t{current_host}")

        ttl += 1
        if current_addr == dest_addr or ttl > max_hops:
            break

hostname=input("Please input destination host name:\n")
hostaddr=''
if hostname=='h1':
    hostaddr='10.0.0.1'
elif hostname=='h2':
    hostaddr='10.0.0.2'
elif hostname=='h3':
    hostaddr=='10.0.0.3'
elif hostname=='h4':
    hostaddr='10.0.0.4'
else:
    print("Error hostname. Terminate...")
traceroute(hostaddr)
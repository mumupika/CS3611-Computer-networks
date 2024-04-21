import socket
import struct
import time
import func_timeout
from func_timeout import func_set_timeout

@func_set_timeout(5)
def test(recv_socket):
    data, current_addr = recv_socket.recvfrom(52)
    return data,current_addr


def traceroute(hostaddr):
    dest_addr = hostaddr
    port = 53
    max_hops = 64
    icmp = socket.getprotobyname('icmp')
    udp=socket.getprotobyname('udp')
    ttl = 1
    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.bind(("", port))
        send_socket.sendto(b"", (hostaddr, port))
        current_addr = None
        current_name = None
        # receive packet
        try:
            data,current_addr=test(recv_socket)
        except func_timeout.exceptions.FunctionTimedOut:
            pass
        if current_addr!=None:
            current_addr = current_addr[0]
            try:
                current_name = socket.gethostbyaddr(current_addr)[0]
            except socket.error:
                current_name=current_addr
        else:
            current_name = current_addr
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
try:
    hostaddr=socket.gethostbyname_ex(hostname)
except socket.error:
    print("traceroute: unknown host",hostname)
    exit(0)
if len(hostaddr[2])>1:
    print("traceroute: Warning:",hostname,"has multiple addresses; using",hostaddr[2][0])
    if hostaddr[1]!=[]:
        print("traceroute to",hostaddr[1][0],f'({hostaddr[2][0]})',"64 hops max, 52 byte packets")
    else:
        print("traceroute to",hostname,f'({hostname})',"64 hops max, 52 byte packets")
    traceroute(hostaddr[2][1])
elif len(hostaddr[2])==1:
    if hostaddr[1]!=[]:
        print("traceroute to",hostaddr[1][0],f'({hostname[2][0]})',"64 hops max, 52 byte packets")
    else:
        print("traceroute to",hostname,f'({hostname[2][0]})',"64 hops max, 52 byte packets")
    traceroute(hostaddr[2][0])
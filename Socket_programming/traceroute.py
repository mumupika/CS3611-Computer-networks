import socket
import time
import sys

def test(recv_socket):
    start=time.time()
    data, current_addr = recv_socket.recvfrom(52)
    end=time.time()
    return (end-start)*1000,current_addr


def traceroute(hostaddr):
    dest_addr = hostaddr
    port = 53
    max_hops = 64
    icmp = socket.getprotobyname('icmp')
    udp=socket.getprotobyname('udp')
    ttl = 1
    while True:
        try:
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,udp)
        except PermissionError:
            print("traceroute: Permission Denied. Please run in 'sudo' mode.")
            exit(0)
        times=[]
        get_address=1
        print(ttl,end='  ')
        for i in range(3):
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            recv_socket.bind(("", port))
            recv_socket.settimeout(5) 
            send_socket.sendto(b"", (hostaddr, port))
            current_addr = None
            current_name = None
            # receive packet
            try:
                time,current_addr=test(recv_socket)
            except socket.timeout:
                time=-1
            if current_addr!=None:
                current_addr = current_addr[0]
                try:
                    current_name = socket.gethostbyaddr(current_addr)[0]
                except socket.error:
                    current_name=current_addr
            else:
                current_name = current_addr
            
            if current_addr is not None and get_address==1:
                current_host = f"{current_name} ({current_addr})"
                print(f"{current_host}",end=' ')
                print(f'{round(time,3)}ms',end=' ')
                get_address=0
            elif get_address==1 and current_addr is None:
                current_host = ""
                print('*',end=' ')
            else:
                if time==-1:
                    print('*',end=' ')
                else:
                    print(f'{round(time,3)}ms',end=' ')
        send_socket.close()
        recv_socket.close()
        print('')
        ttl += 1
        if current_addr == dest_addr or ttl > max_hops:
            break

def main():
    #hostname=input("Please input destination host name:\n")
    try:
        hostname=sys.argv[1]
    except IndexError:
        print("traceroute: Please type the hostname correctly.")
        exit(0)
    try:
        hostaddr=socket.gethostbyname_ex(hostname)
    except socket.error:
        print("traceroute: unknown host",hostname)
        exit(0)
    if len(hostaddr[2])>1:
        print("traceroute: Warning:",hostname,"has multiple addresses; using",hostaddr[2][0])
        if hostaddr[0]!='':
            print("traceroute to",hostaddr[0],f'({hostaddr[2][0]})',"64 hops max, 52 byte packets")
        else:
            print("traceroute to",hostname,f'({hostname})',"64 hops max, 52 byte packets")
        traceroute(hostaddr[2][1])
    elif len(hostaddr[2])==1:
        if hostaddr[0]!='':
            print("traceroute to",hostaddr[0],f'({hostaddr[2][0]})',"64 hops max, 52 byte packets")
        else:
            print("traceroute to",hostname,f'({hostaddr[2][0]})',"64 hops max, 52 byte packets")
        traceroute(hostaddr[2][0])

main()

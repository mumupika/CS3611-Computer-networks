Hw1: Contains the trial of playing with mininet.

Hw2: We built a network topo by mininet. The topo is: 3 switches s1,s2,s3, and 4 hosts with h4 as server, h1,h2,h3 is client.
    
We have realized one time communication between the clients with server h4. 

First, run topo_struct.py under sudo mode. Then in the command line, use 'xterm h1' to open commandline of h1. Then, Run client.py on h1,h2,h3 and server.py
on h4. For a pair(ex, (h1,h2)), type one as 'send' and one as 'hear'. Then type as: "To h2:Hello". Then you can find the echos on h2 commandline window.

Facing difficulties: 1. Binded address. When an address is binded, re-bind it will report error.

2. Bad file descriptors. This is caused after using 'socket.closed()'. It seems that close is not a simple 'close' function.

We are striving hard to fix this. If you have any good ideas, please give issues! Thankyou!

Hw1: Contains the trial of playing with mininet.

Socket_programming: We built a network topo by mininet. The topo is: 3 switches s1,s2,s3, and 4 hosts with h4 as server, h1,h2,h3 is client.
    
We have realized one time communication between the clients with server h4. 

First, run topo_struct.py under sudo mode. Then in the command line, use 'xterm h1' to open commandline of h1. Then, Run client.py on h1,h2,h3 and server.py
on h4. For a pair(ex, (h1,h2)), type one as 'send' and one as 'hear'. Then type as: "To h2:Hello". Then you can find the echos on h2 commandline window.

We have achieved the continuous chat by running the above instructions and all problems listed on 4.19.2024 has been fixed.

2024.4.22 We implemented a simple traceroute.

Todo: To add time detection for it looks closer to the traceroute now using.

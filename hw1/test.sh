#!/bin/bash
#set the mode of s1,s2,s3 all drop to offset arp.
ovs-ofctl mod-flows s1 in_port=1,arp,action=drop
ovs-ofctl mod-flows s1 in_port=2,arp,action=drop
ovs-ofctl mod-flows s1 in_port=3,arp,action=drop

ovs-ofctl mod-flows s2 in_port=1,arp,action=drop
ovs-ofctl mod-flows s2 in_port=2,arp,action=drop
ovs-ofctl mod-flows s2 in_port=3,arp,action=drop
ovs-ofctl mod-flows s2 in_port=4,arp,action=drop

ovs-ofctl mod-flows s3 in_port=1,arp,action=drop
ovs-ofctl mod-flows s3 in_port=2,arp,action=drop
ovs-ofctl mod-flows s3 in_port=3,arp,action=drop
ovs-ofctl mod-flows s3 in_port=4,arp,action=drop

sleep 30s


#del flows!!!
ovs-ofctl del-flows s1
ovs-ofctl del-flows s2
ovs-ofctl del-flows s3

sleep 30s

#set rules.
ovs-ofctl add-flow s1 in_port=3,actions=output:1,2
ovs-ofctl add-flow s1 in_port=2,actions=output:1,3
ovs-ofctl add-flow s1 in_port=1,actions=output:2,3

ovs-ofctl add-flow s2 in_port=3,actions=output:1,4
ovs-ofctl add-flow s2 in_port=4,actions=output:1,3
ovs-ofctl add-flow s2 in_port=1,actions=output:3,4


ovs-ofctl add-flow s3 in_port=3,actions=output:1,4
ovs-ofctl add-flow s3 in_port=4,actions=output:1,3
ovs-ofctl add-flow s3 in_port=1,actions=output:3,4

ovs-ofctl add-flow s2 in_port=2,actions=drop
ovs-ofctl add-flow s3 in_port=2,actions=drop


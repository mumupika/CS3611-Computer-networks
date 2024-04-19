ovs-vsctl set-fail-mode s1 standalone
ovs-vsctl set-fail-mode s2 standalone
ovs-vsctl set-fail-mode s3 standalone

ovs-ofctl add-flow s1 in_port=1,action=drop
ovs-ofctl add-flow s1 in_port=2,action=drop
ovs-ofctl add-flow s1 in_port=3,action=drop

ovs-ofctl add-flow s2 in_port=1,action=drop
ovs-ofctl add-flow s2 in_port=2,action=drop
ovs-ofctl add-flow s2 in_port=3,action=drop
ovs-ofctl add-flow s2 in_port=4,action=drop

ovs-ofctl add-flow s3 in_port=1,action=drop
ovs-ofctl add-flow s3 in_port=2,action=drop
ovs-ofctl add-flow s3 in_port=3,action=drop
ovs-ofctl add-flow s3 in_port=4,action=drop

sleep 30s

ovs-ofctl del-flows s1
ovs-ofctl del-flows s2
ovs-ofctl del-flows s3

ovs-ofctl add-flow s2 in_port=2,action=drop
ovs-ofctl add-flow s3 in_port=2,action=drop

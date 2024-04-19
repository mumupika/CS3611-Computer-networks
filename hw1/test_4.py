#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
import os

class SingleSwitchTopo(Topo):
    '''Single switch connected to n hosts.'''
    def build(self):
        s1=self.addSwitch('s1')
        s2=self.addSwitch('s2')
        s3=self.addSwitch('s3')
        h1=self.addHost('h1')
        h2=self.addHost('h2')
        h3=self.addHost('h3')
        h4=self.addHost('h4')
        h5=self.addHost('h5')
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s1,h1)
        self.addLink(s2,h2)
        self.addLink(s2,h3)
        self.addLink(s3,h4)
        self.addLink(s3,h5)

def iperf(net):
    net.iperf((net.get('h1'),net.get('h2')))
	
def simpleTest():
	'''Create and test a simple network.'''
	topo = SingleSwitchTopo() #setup topo structure
	net = Mininet(topo) #initialize net class
	net.start() #start net.
	print("Dumping host connections")
	dumpNodeConnections(net.hosts) 
	print("Testing network connectivity")
	net.pingAll()
	iperf(net)
	net.stop()

if __name__=="__main__":
	#Tell mininet to print useful information
	setLogLevel('info')
	simpleTest()
	os.system('sudo mn -c')

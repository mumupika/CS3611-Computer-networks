#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
import os

class SingleSwitchTopo(Topo):
	'''Single switch connected to n hosts.'''
	def build(self):
		#build switch: s1,s2,s3
		s=[] #switches;
		for i in range(3):
			s.append(self.addSwitch('s%s'%(i+1)))
		
		#build hosts: h1,h2,h3,h4,h5
		h=[] #hosts;
		for i in range(5):
			h.append(self.addHost('h%s'%(i+1)))
			
		#links between s1,s2,s3
		self.addLink(s[0],s[1],bw=5)
		self.addLink(s[0],s[2],bw=10)
		
		'''links between hosts and switches.
		links are (s1,h1),(s2,h2),(s2,h3),(s3,h4),(s3,h5)
		s and h are started from 0 base.'''
		self.addLink(s[0],h[0])
		self.addLink(s[1],h[1])
		self.addLink(s[1],h[2])
		self.addLink(s[2],h[3])
		self.addLink(s[2],h[4])

def getName(net):
	'''To name the node'''
	h1,h2,h3,h4,h5=net.get('h1','h2','h3','h4','h5')
	hosts=[h1,h2,h3,h4,h5];
	return hosts;

def Iperf(net,h):
	'''Run Test'''
	print("Testing bandwidth between h1 and h2")
	net.iperf( (h[0],h[1]) )
	print("Testing bandwidth between h1 and h4")
	net.iperf( (h[0],h[3]) )
	print("Testing bandwidth between h2 and h3")
	net.iperf( (h[1],h[2]) )		
	
def simpleTest():
	'''Create and test a simple network.'''
	topo = SingleSwitchTopo() #setup topo structure
	net = Mininet(topo) #initialize net class
	net.start() #start net.
	print("Dumping host connections")
	dumpNodeConnections(net.hosts) 
	print("Testing network connectivity")
	net.pingAll()
	hosts=getName(net) #To assign node to object.
	Iperf(net,hosts)
	net.stop()

if __name__=="__main__":
	#Tell mininet to print useful information
	setLogLevel('info')
	simpleTest()
	os.system('sudo mn -c')

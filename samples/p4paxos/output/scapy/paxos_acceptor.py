from scapy.all import *

##class definitions
class Paxos(Packet):
	name = 'paxos'
	fields_desc = [
		XByteField('msgtype', 0),
		XShortField('instance', 0),
		XByteField('round', 0),
		XByteField('vround', 0),
		XLongField('acceptor', 0),
		XBitField('value', 0, 512),
	]

##bindings
bind_layers(Ether, IP, type = 0x0800)
bind_layers(IP, UDP, proto = 0x11)
bind_layers(UDP, Paxos, dport = 0x8888)

##packet_list
possible_packets_ = [
	(Ether()),
	(Ether()/IP()),
	(Ether()/IP()/UDP()),
	(Ether()/IP()/UDP()/Paxos())
]

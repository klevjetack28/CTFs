from scapy.all import *

pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src="be:27:a5:d0:5f:56", type=0xffff)
response = sendp(pkt, iface="eth0")
print(response)

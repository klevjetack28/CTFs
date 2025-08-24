from scapy.all import *

pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src="da:70:0c:68:76:c5")/IP(dst="10.0.0.3", src="10.0.0.2", proto=0xff)
response = sendp(pkt, iface="eth0")
print(response)

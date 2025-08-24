from scapy.all import *
# The packet should have `TCP sport=31337, dport=31337, seq=31337, ack=31337, flags=APRSF`.
pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src="da:70:0c:68:76:c5")/IP(dst="10.0.0.3", src="10.0.0.2")/TCP(sport=31337, dport=31337, seq=31337, ack=31337, flags="APRSF")
response = sendp(pkt, iface="eth0")
print(response)

from scapy.all import *
# The initial packet should have `TCP sport=31337, dport=31337, seq=31337`.
eth = Ether(dst="ff:ff:ff:ff:ff:ff", src="3a:67:16:e6:7c:c1")
ip = IP(dst="10.0.0.3", src="10.0.0.2")
tcp = TCP(sport=31337, dport=31337, flags="S", seq=31337)
syn_pkt = eth/ip/tcp
response = srp1(syn_pkt, iface="eth0")

if response is not None:
	if response.haslayer(TCP) and response[TCP].flags == 0x12:
		tcp = TCP(sport=31337, dport=31337, flags="A", seq=response[TCP].ack, ack=response[TCP].seq + 1)
		ack_pkt = eth/ip/tcp
		response = sendp(ack_pkt, iface="eth0")
		print(response)

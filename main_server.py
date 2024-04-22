import socket
import sys

from socket_programming_example_server import socket_server_program

def main():
    # 1. Hello World example, showing server running status
    
    print("Hello World!")
    print("The server is ready for in-coming connections...")
    
    # Server side socket program function
    socket_server_program()

if __name__ == '__main__':
    main()

# socket_programming_example_server.py

import socket

def socket_server_program():
    host = socket.gethostname()
    port = 33547  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2)
    print("Listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from: {client_address}")
        message = "Connection Established... Hello, client. Thank you for connecting!"
        client_socket.send(message.encode())
        client_socket.close()

if __name__ == "__main__":
    socket_server_program()

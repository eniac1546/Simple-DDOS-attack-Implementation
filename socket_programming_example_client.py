# socket_programming_example_client.py

import socket

def socket_client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 33547  # socket server port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = client_socket.recv(1024).decode()  # receive response
    print(message)  # show in terminal

    client_socket.close()  # close the connection

if __name__ == '__main__':
    socket_client_program()

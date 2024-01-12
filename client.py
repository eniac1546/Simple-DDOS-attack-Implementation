import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

while True:
    # Send a message to the server
    message = input("You: ")
    client_socket.sendall(message.encode())

    if message.lower() == 'exit':
        break

    # Receive response from the server
    data = client_socket.recv(1024)
    print(f'Server: {data.decode()}')

# Close the socket
client_socket.close()
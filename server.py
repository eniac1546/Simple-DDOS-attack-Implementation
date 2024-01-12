import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Bind the socket to the address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

# Wait for a connection
print('Waiting for a connection...')
client_socket, client_address = server_socket.accept()
print(f'Connection from {client_address}')

while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break  # If no data is received, break the loop
    print(f'Received: {data.decode()}')

    # Send a response back to the client
    response = 'Message received!'
    client_socket.sendall(response.encode())

# Close the sockets
client_socket.close()
server_socket.close()
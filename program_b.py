# Program B - Server
# This program listens for a connection from Program A, receives a string,
# converts it to upper case, prints it, and sends it back.

import socket

# Set up connection info - must match Program A
HOST = '127.0.0.1'
PORT = 5000

# Create a socket object using IPv4 and TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (1 = max number of queued connections)
server_socket.listen(1)
print("Program B is waiting for a connection...")

# Accept a connection when Program A connects
# This returns a new socket for the connection and the client's address
connection, address = server_socket.accept()
print("Connected to:", address)

# Receive the string sent from Program A (up to 1024 bytes)
data = connection.recv(1024)

# Decode bytes into a string
received_string = data.decode()

# Convert the string to upper case
upper_string = received_string.upper()

# Print the upper case string in Program B
print("Upper case string:", upper_string)

# Send the upper case string back to Program A (must encode to bytes)
connection.send(upper_string.encode())

# Close both sockets
connection.close()
server_socket.close()

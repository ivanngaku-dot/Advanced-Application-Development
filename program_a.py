# Program A - Client
# This program asks the user for a string, sends it to Program B over a socket,
# waits for a response, and prints what it gets back.

import socket

# Set up connection info
HOST = '127.0.0.1'   # localhost - both programs run on same machine
PORT = 5000           # port number, must match Program B

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Program B
client_socket.connect((HOST, PORT))

# Ask the user for input
message = input("Enter a string to send: ")

# Send the string to Program B (must encode string to bytes)
client_socket.send(message.encode())

# Wait to receive the response from Program B (up to 1024 bytes)
response = client_socket.recv(1024)

# Decode bytes back into a string and print it
print("Received from Program B:", response.decode())

# Close the socket connection
client_socket.close()

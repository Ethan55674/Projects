
import socket

HOST = "127.0.0.1"  # Server IP address
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = input("Enter a message to send to the server: ")
client_socket.sendall(message.encode())

response = client_socket.recv(1024).decode()
print(f"Server says: {response}")

client_socket.close()

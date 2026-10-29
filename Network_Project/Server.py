import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates the TCP server

server_socket.bind((HOST, PORT)) #bind assigns both a IP address and port
server_socket.listen() # server is ready for messages

print(f"Server listening on port {PORT}")
while True:
    client_socket, client_address = server_socket.accept()

    print(f"Connected to: {client_address}")

    message = client_socket.recv(1024).decode() # number of bytes allowed
    print(f"Client says: {message}")

    client_socket.sendall("Hello from server".encode())

    client_socket.close()
    server_socket.close()

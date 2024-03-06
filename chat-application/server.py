import socket
import threading

def handle_client(client_socket, client_name):
    while True:

        message = client_socket.recv(1024).decode()
        if message == "exit":
            print(f"{client_name} exited chat")
            client_socket.close()
            break
        print(f"{client_name}: {message}")
        
        broadcast(message, client_name)

def broadcast(message, client_name):
    for client in clients:
        if client[1] != client_name:
            client[0].send(f"{client_name}: {message}".encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

server_socket.bind((host, port))

server_socket.listen(5)
print(f"Server listening on {host}:{port}")

clients = []

while True:
    client_socket, client_address = server_socket.accept()

    client_name = client_socket.recv(1024).decode()
    print(f"{client_name} connected from {client_address}")

    client_socket.send("Connection successful!".encode())

    clients.append((client_socket, client_name))

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
    client_thread.start()

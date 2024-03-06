import socket
import threading


def handle_client(client_socket, client_address, client_name):
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()
        if message == "exit":
            print(f"{client_name} exited chat")
            break
        print(f"{client_name}: {message}")
        # Broadcast the message to all clients
        broadcast(message, client_name)

    # Close client socket
    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message, client_name):
    for client in clients:
        if client[1] != client_name:  # Avoid sending the message to the sender
            client[0].send(f"{client_name}: {message}".encode())

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('blu', 8000))
server.listen(5)

print("Server is listening...")

clients = []  # List to store client sockets and names

while True:
    # Accept client connection
    client_socket, client_address = server.accept()

    # Receive client's name
    client_name = client_socket.recv(1024).decode()
    print(f"{client_name} connected from {client_address}")

    # Send connection success message to client
    client_socket.send("Connection successful!".encode())

    # Add client socket and name to the list
    clients.append((client_socket, client_name))

    # Start a new thread to handle client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_name))
    client_thread.start()

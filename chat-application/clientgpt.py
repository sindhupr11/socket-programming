import socket


# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('blu', 8000))


# Get user's name
name = input("Enter your name: ")
client.send(name.encode())

# Receive connection success message from server
print(client.recv(1024).decode())

# Start chatting
while True:
    message = input("You: ")
    client.send(message.encode())
    if message == "exit":
        break

# Close connection
client.close()




'''
import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message.startswith(name + ":"):
                # Print the message without prefixing "You:"
                print(message[len(name) + 1:])
            else:
                # Print messages from other clients with their names
                print(message)
        except Exception as e:
            print("Error:", e)
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

client.connect((host, port))

name = input("Enter your name: ")
client.send(name.encode())

print(client.recv(1024).decode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("You: ")
    client.send(message.encode())
    if message == "exit":
        break

client.close()
'''

import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except Exception as e:
            print("Error:", e)
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

client.connect((host, port))

name = input("Enter your name: ")
client.send(name.encode())

print(client.recv(1024).decode())

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("You: ")
    print("You:", message)  # Print "You:" before sending the message
    client.send(message.encode())
    if message == "exit":
        break

# Close connection
client.close()

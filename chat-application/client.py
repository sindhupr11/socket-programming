import socket
import threading

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

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("You: ")
    client.send(message.encode())
    if message == "exit":
        break

client.close()

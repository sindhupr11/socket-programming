import socket

def main():
    host = 'blu'
    port = 8000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(client_socket.recv(1024).decode())


    while True:
        print(client_socket.recv(1024).decode())

        option = input(client_socket.recv(1024).decode())
        client_socket.send(option.encode())

if __name__ == "__main__":
    main()

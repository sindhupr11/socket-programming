import socket

def main():
    host = 'blu'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening on port", port)

    max_clients = int(input("Enter the maximum number of clients for the poll: "))
    clients_count = 0
    clients = []

    candidates = []
    votes = {}

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print("Client connected from", addr)
        clients_count += 1

        if clients_count == max_clients:
            print("Max clients reached. You can now add candidates.")
            for client in clients:
                client.send("Connected successfully!\n".encode())
            while True:
                option = input("Enter 1 to add a candidate, 2 to remove a candidate, 3 to publish poll: ")
                if option == '1':
                    candidate_name = input("Enter the candidate name: ")
                    candidates.append(candidate_name)
                    print(f"{candidate_name} added to the list.")
                elif option == '2':
                    candidate_name = input("Enter the candidate name to remove: ")
                    if candidate_name in candidates:
                        candidates.remove(candidate_name)
                        print(f"{candidate_name} removed from the list.")
                    else:
                        print(f"{candidate_name} not found in the list.")
                elif option == '3':
                    if len(candidates) == 0:
                        print("No candidates available to publish poll.")
                    else:
                        print("Candidates available for the poll:")
                        for i, candidate in enumerate(candidates):
                            print(f"{i + 1}. {candidate}")

                        for client in clients:
                            client.send("Candidates available for the poll:\n".encode())
                            for i, candidate in enumerate(candidates):
                                client.send(f"{i + 1}. {candidate}\n".encode())

                            client.send("Enter the number corresponding to your choice: ".encode())
                            response = client.recv(1024).decode()
                            vote = candidates[int(response) - 1]
                            if vote in votes:
                                votes[vote] += 1
                            else:
                                votes[vote] = 1
                            print(f"Client from {addr} voted for {vote}")
                        break

            print("Poll result:")
            for candidate, vote_count in votes.items():
                print(f"{candidate}: {vote_count} votes")

            for client in clients:
                client.send("\nPoll result:\n".encode())
                for candidate, vote_count in votes.items():
                    client.send(f"{candidate}: {vote_count} votes\n".encode())

            break

    server_socket.close()

if __name__ == "__main__":
    main()

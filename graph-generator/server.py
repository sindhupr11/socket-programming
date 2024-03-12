import socket,time,sys,json
from pyvis.network import Network

net = Network(directed=True)

def create_graph(json_str,filename="graph.html"):
    

    json_data = json.loads(json_str)

    """
    json structure

    {
        "nodes":[
            {id:1, label:"Node 1"},
            {id:2, label:"Node 2"},
            {id:3, label:"Node 3"}
        ],
        "edges":[
            {from:1, to:2},
            {from:2, to:3},
            {from:3, to:1}
        ]
    }
    """

    for node in json_data['nodes']:
        net.add_node(node['id'], label=node['label'])
    for edge in json_data['edges']:
        net.add_edge(edge['from'], edge['to'])

    net.toggle_stabilization(True)
    net.toggle_physics(True)
    net.save_graph(f"{filename}")
    return filename


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = int(input("port? :"))



server_socket.bind((host, port))

server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")

    client_socket.send(b"Thank you for connecting")

    json_str = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {json_str}")

    graph_name = create_graph(json_str)

    file = open(graph_name, 'rb')
    line = file.read(1024)
    c = 1
    while(line):
        client_socket.send(line)
        sys.stdout.write(f"[{'*'*c}]")
        sys.stdout.flush()
        line = file.read(1024)
        c+=1

    file.close()
    print("done sending")
    
    client_socket.close()

"""
    - send 
    - receive

"""
import socket, os, webbrowser, json

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

def get_elements():
    no_nodes = int(input("no of nodes;"))
    no_edges = int(input("no of edges;"))

    json_dict = {}
    nodes_list = []
    edges_list = []
    for n in range(1, no_nodes+1):
        node_dict = {}
        node_dict['id'] = int(input(f"node {n} id:"))
        node_dict['label'] = input(f"node {n} label:")
        nodes_list.append(node_dict)
    for n in range(1, no_edges+1):
        edge_dict = {}
        edge_dict['from'] = int(input(f"from {n} id:"))
        edge_dict['to'] = int(input(f"to {n} id:"))
        edges_list.append(edge_dict)
    
    json_dict['nodes'] = nodes_list
    json_dict['edges'] = edges_list

    json_str = json.dumps(json_dict)

    return json_str

        



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = int(input("port? :"))

client_socket.connect((host, port))

data = client_socket.recv(1024)
print(data.decode('utf-8'))


json_str = get_elements()
client_socket.send(json_str.encode('utf-8'))


file = open('graph.html', 'wb')

line = client_socket.recv(1024)

while(line):
    file.write(line)
    line = client_socket.recv(1024)

print('File has been received successfully.')

file.close()

client_socket.close()

webbrowser.open('graph.html')

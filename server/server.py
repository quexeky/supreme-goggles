import socket
import sys
import threading

port = 8090
host = "0.0.0.0"

clients = list()
client_counter = 0
"""

def handle_client(player):
    global client_counter

    player.send(client_counter.to_bytes(16, byteorder="little"))
    client_counter += 1

    while True:
        global clients
        data = player.recvfrom(17)

        if not data:
            print("Client disconnected")
            player.close()
            clients.remove(player)
            break
        threading.Thread(target=send_received_data, args=(data, player)).start()


def send_received_data(data, player):
    print(data)
    for client in clients:
        if client != player:
            client.sendto(data)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    print("Socket successfully created")
except socket.error as msg:
    print("Socket creation failed")
    print(msg)
    sys.exit()

try:
    print(host, port)
    s.bind((host, port))
    print("Socket bind successful")
except socket.error as msg:
    print("Bind failed")
    print(msg)
    sys.exit()

s.listen(3)

while True:
    print("Waiting for connection")
    (payload, addr) = s.recvfrom(17)
    print(payload)
    clients.append(addr)
    print("Connected by", addr)
    threading.Thread(target=handle_client, args=(addr,)).start()
"""

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket successfully created")
except socket.error as msg:
    print("Socket creation failed")
    print(msg)
    sys.exit()

try:
    s.bind((host, port))
    print("Socket bind successful")
except socket.error as msg:
    print("Bind failed")
    print(msg)
    sys.exit()

while True:
    print("Waiting for connection")
    payload, addr = s.recvfrom(17)
    if not clients.__contains__(addr):
        if payload == b"Create Client!1!!":
            s.sendto(int.to_bytes(client_counter, 17, "little"), addr)
            clients.append(addr)
    else:
        print(payload)
        for client in clients:
            if client != addr:
                s.sendto(payload, client)



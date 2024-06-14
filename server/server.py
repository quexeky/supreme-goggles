import socket
import sys
import threading

port = 8090
host = "127.0.0.1"

clients = []
client_counter = 0


def handle_client(player):
    global client_counter

    player.send(client_counter.to_bytes(16, byteorder="little"))
    client_counter += 1

    while True:
        global clients
        data = player.recv(17)
        if not data:
            print("Client disconnected")
            clients.remove(player)
            player.close()
        threading.Thread(target=send_received_data, args=(data, player)).start()


def send_received_data(data, player):
    print(data)
    for client in clients:
        if client != player:
            client.send(data)


try:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
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

s.listen(3)

while True:
    print("Waiting for connection")
    (conn, addr) = s.accept()
    clients.append(conn)
    print("Connected by", addr)
    threading.Thread(target=handle_client, args=(conn,)).start()

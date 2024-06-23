import socket
import sys

port = 8090
host = "0.0.0.0"

clients = {}
client_counter = 0

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
    # print("Waiting for connection")
    payload, addr = s.recvfrom(22)
    # print(payload)
    if not clients.__contains__(addr):
        if payload == b"Create Client!1!!!!":
            s.sendto(int.to_bytes(client_counter, 1, "little"), addr)
            clients.update({addr: client_counter})
            client_counter += 1
    else:
        # print(payload)
        sender_id = clients[addr]

        for client in clients.items():
            if client[0] != addr:
                print("Sending update from {} to {}".format(sender_id, client))
                id_payload = sender_id.to_bytes(1, 'little', signed=False) + payload
                s.sendto(id_payload, client[0])


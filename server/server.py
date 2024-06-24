import socket
import sys
import threading


def manage_client(payload, addr):
    try:
        global client_counter
        if not clients.__contains__(addr):
            print(addr)
            if payload == b"Create Client!1!!!!":
                s.sendto(int.to_bytes(client_counter, 1, "little"), addr)
                clients.update({addr: client_counter})
                # Giving each user their ID. Isn't shown to the user. This is just to slightly stop Declan's DDOS,
                # but also because I thought it would fix a bug (it didn't), but it still works slightly better this
                # way because it's a bit less bandwidth being transferred
                client_counter += 1
        else:
            sender_id = clients[addr]

            for client in clients.items():
                if client[0] != addr:
                    id_payload = sender_id.to_bytes(1, "little", signed=False) + payload
                    s.sendto(id_payload, client[0])
    except Exception as e:
        print("Server Error:", e)


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
    payload, addr = s.recvfrom(25)
    # Multithreading it just for that little bit of extra safety if something dies while it's happening
    threading.Thread(target=manage_client, args=(payload, addr), daemon=True).start()

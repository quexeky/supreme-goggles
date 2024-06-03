import asyncio
import socket
import threading


def handle_client(client):
    request = None
    while request != b'quit' and request != b'quit\n':
        request = client.recv(1024)
        response = request.upper()
        print(request)
        client.send(response)
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen(8)

try:
    while True:
        client, _ = server.accept()
        threading.Thread(target=handle_client, args=(client,)).start()
except KeyboardInterrupt:
    server.close()

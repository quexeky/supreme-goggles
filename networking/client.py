import json
import socket
import threading
from asyncio import sleep

import data
import playerData
import settings
from GameObjects.displayPlayer import DisplayPlayer


def server_connect(game):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b"Create Client!1!!!!", (settings.host, settings.PORT))
    print(len(b"Create Client!1!!!!"))

    self_id = int.from_bytes(sock.recv(1), "little")
    data.player_self = playerData.PlayerData(
        self_id, data.player_pos.x, data.player_pos.y,
        (0, 1, False)
    )
    threading.Thread(target=manage_input, args=(sock, game), daemon=True).start()
    threading.Thread(target=manage_output, args=(sock, game), daemon=True).start()


def manage_input(conn, game):
    while True:
        if game.done:
            break
        # conn.sendto(b"Create Client!1!!", (settings.host, settings.PORT))
        recv_data = conn.recvfrom(22)
        if not recv_data:
            break

        try:
            # length = int.from_bytes(recv_data[:1], 'little')
            # d = recv_data[1:length]
            # print(d)

            # block = json.loads(d)

            player = playerData.deserialise_player_data(recv_data[0])
            # print((player.x, player.y))
            # print("Received UID:", player.user_id)

            # print(data.others)
            if data.others.get(str(player.user_id)):
                data.others[str(player.user_id)] = player

                print("Updated old user", str(player.user_id))
            else:
                data.others[str(player.user_id)] = player
                game.addGameObject(DisplayPlayer(player.user_id, player.direction))

                print("Created new user", str(player.user_id))

            # print("Users: ", len(data.others))

        except json.JSONDecodeError:
            print("Invalid client data recieved")


def manage_output(conn, game):
    while True:
        if game.done:
            break
        if data.player_pos_updated:
            data.player_pos_updated = False
            position_data = data.player_self.serialise()
            # block = (len(position_data) + 1).to_bytes(1, byteorder='little') + position_data
            conn.sendto(position_data, (settings.host, settings.PORT))
            # sleep(0.01)

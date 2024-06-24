import json
import socket
import threading
import time
from time import sleep

import data
import playerData
import settings
from GameObjects.displayPlayer import DisplayPlayer


def server_connect(game):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Had to create some sort of client connection value just to process. If someone accidentally triggers it in game it
    # shouldn't be much of an issue though
    sock.sendto(b"Create Client!1!!!!", (settings.host, settings.PORT))

    self_id = int.from_bytes(sock.recv(1), "little")
    data.player_self = playerData.PlayerData(
        self_id, data.player_pos.x, data.player_pos.y, (0, 1, False), (0, 0, 0)
    )
    threading.Thread(target=manage_input, args=(sock, game), daemon=True).start()
    threading.Thread(target=manage_output, args=(sock, game), daemon=True).start()


def manage_input(conn, game):
    while True:
        if game.done:
            break
        # conn.sendto(b"Create Client!1!!", (settings.host, settings.PORT))
        recv_data = conn.recvfrom(settings.PACKET_SIZE)
        if not recv_data:
            break

        # run_client(game, recv_data)
        threading.Thread(target=run_client, args=(game, recv_data), daemon=True).start()


def run_client(game, recv_data):
    try:
        player = playerData.deserialise_player_data(recv_data[0])
        if (player.age - data.current_time) > settings.MAX_DATA_AGE:
            return

        if data.others.get(str(player.user_id)):
            data.others[str(player.user_id)] = player

        else:
            data.others[str(player.user_id)] = player
            game.addGameObject(DisplayPlayer(player.user_id, player.direction))

    except json.JSONDecodeError:
        print("Invalid client data recieved")


def manage_output(conn, game):
    while True:
        timeSinceLastUpdate = time.time()
        if game.done:
            break
        if (
            data.player_pos_updated
            or (time.time() - timeSinceLastUpdate) > settings.PASSIVE_UPDATE_FREQUENCY
        ):
            timeSinceLastUpdate = time.time()
            data.player_pos_updated = False
            position_data = data.player_self.serialise()

            conn.sendto(position_data, (settings.host, settings.PORT))
        sleep(settings.CLIENT_SLEEP_TIME)

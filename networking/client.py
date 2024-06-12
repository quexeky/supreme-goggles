import json
import pickle
import socket
import threading
from time import sleep

import jsonpickle

import data
import playerData
import settings
from GameObjects.displayPlayer import DisplayPlayer
from playerData import PlayerData


def server_connect(game):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((settings.host, settings.PORT))
    self_id = int.from_bytes(sock.recv(16), 'little')
    data.player_self = playerData.PlayerData(self_id, data.player_pos.x, data.player_pos.y, True)
    threading.Thread(target=manage_input, args=(sock, game)).start()
    threading.Thread(target=manage_output, args=(sock,)).start()


def manage_input(conn, game):
    while True:
        recv_data = conn.recv(1024)
        if not recv_data:
            break

        tmp_data = json.loads(recv_data.decode())
        print(tmp_data)
        player = PlayerData(**tmp_data)
        print((player.x, player.y))
        if player.user_id not in data.others:
            data.others.update({player.user_id: player})
            game.addGameObject(DisplayPlayer(player.user_id))
        else:
            data.others.update({player.user_id: player})


def manage_output(conn):
    while True:
        sleep(0.01)
        conn.send(jsonpickle.dumps(data.player_self, unpicklable=False).encode())


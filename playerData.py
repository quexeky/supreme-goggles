import json

import pygame

import data


class PlayerData(object):

    def __init__(self, user_id, x, y):
        self.user_id = user_id
        self.x = x
        self.y = y

    def update_pos(self, pos):
        if not (self.x == int(pos.x) and self.y == int(pos.y)):
            self.x = int(pos.x)
            self.y = int(pos.y)
            data.player_pos_updated = True

    def serialise(self):
        uid = int(self.user_id).to_bytes(1, byteorder='little', signed=False)
        x = int(self.x).to_bytes(8, byteorder='little', signed=True)
        y = int(self.y).to_bytes(8, byteorder='little', signed=True)
        print(len(uid + x + y))

        return uid + x + y


def deserialise_player_data(serialised):
    print(serialised)
    uid = int.from_bytes((serialised[0], ), byteorder='little', signed=False)
    x = int.from_bytes(serialised[1:8], byteorder='little', signed=True)
    y = int.from_bytes(serialised[9:16], byteorder='little', signed = True)

    return PlayerData(uid, x, y)

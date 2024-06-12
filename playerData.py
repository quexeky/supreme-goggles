import json

import pygame


class PlayerData(object):

    def __init__(self, user_id, x, y, visible):
        self.user_id = user_id
        self.x = x
        self.y = y
        self.visible = visible

    def update_pos(self, pos):
        self.x = int(pos.x)
        self.y = int(pos.y)
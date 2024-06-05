import pygame

import data
import settings
from GameObjects import gameObject


class Player(gameObject.GameObject):
    def __init__(self, x, y, w, h, scale):
        super().__init__(x, y, settings.playerImage(w, h), scale)
        self.rect = self.img.get_rect(center=(x, y))

    def update(self, dt):
        for key in settings.DIRECT_DICT:
            if data.keys[key]:
                self.pos.x += settings.DIRECT_DICT[key][0] * settings.PLAYER_SPEED * dt
                self.pos.y += settings.DIRECT_DICT[key][1] * settings.PLAYER_SPEED * dt
        (self.rect.x, self.rect.y) = (self.pos.x, self.pos.y)
        (data.camera_position.x, data.camera_position.y) = (self.x - settings.SCREEN_SIZE.x / 2,
                                                            self.y - settings.SCREEN_SIZE.y / 2)
        self.clamp(data.screen_rect)

    def clamp(self, screen_rect):
        """
        Clamp the rect to the screen if needed and reset true_pos to the
        rect position so they don't lose sync.
        """
        if not screen_rect.contains(self.rect):
            self.rect.clamp_ip(screen_rect)
            (self.x, self.y) = self.rect_pos()

    def rect_pos(self):
        return self.rect.x, self.rect.y
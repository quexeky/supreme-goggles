import pygame.transform

import data
import settings
from GameObjects import gameObject
from Sprites.sprites import SpriteCharacter


class Player(gameObject.GameObject):
    def __init__(self, x, y, w, h, scale, z=1):
        self.movement_composition = (0, 0)
        self.direction = (0, -1, False)
        self.sprite = SpriteCharacter(3, self.direction)
        self.rect = self.sprite.img.get_rect(center=(x, y))

        super().__init__(x, y, self.sprite.img, scale, True, z)
        # print(self.rect.center)

    def update(self, dt, events):
        posUpdateX = 0
        posUpdateY = 0
        for key in settings.DIRECT_DICT:
            if data.keys[key]:
                posUpdateX += settings.DIRECT_DICT[key][0]
                posUpdateY += settings.DIRECT_DICT[key][1]
        if abs(posUpdateX) == 1 and abs(posUpdateY) == 1:
            (posUpdateX, posUpdateY) = (posUpdateX * 1.412 / 2, posUpdateY * 1.412 / 2)

        self.pos += pygame.Vector2(
            (
                posUpdateX * settings.PLAYER_SPEED * dt,
                posUpdateY * settings.PLAYER_SPEED * dt,
            )
        )
        # print(posUpdateX, posUpdateY)

        (self.rect.x, self.rect.y) = (self.pos.x, self.pos.y)
        (data.camera_position.x, data.camera_position.y) = (
            self.rect.center[0] - settings.SCREEN_SIZE.x / 2,
            self.rect.center[1] - settings.SCREEN_SIZE.y / 2,
        )
        self.clamp(data.screen_rect)
        data.player_self.update_pos(self.pos, self.direction, self.sprite.styleIndexes)
        # print(self.direction)
        self.sprite.update(events)
        self.sprite.tick(dt)
        self.direction = self.sprite.direction

        self.img = self.sprite.img
        self.rect = self.img.get_rect(center=(self.pos.x, self.pos.y))
        # print(self.sprite.img)

    def clamp(self, screen_rect):
        if not screen_rect.contains(self.rect):
            self.rect.clamp_ip(screen_rect)
            (self.x, self.y) = self.rect_pos()

    def rect_pos(self):
        return self.rect.x, self.rect.y

import pygame.transform

import data
import settings
from GameObjects import gameObject
from Sprites.sprites import SpriteCharacter


class Player(gameObject.GameObject):
    def __init__(self, x, y, w, h, scale, z=1):
        s = pygame.transform.scale(settings.playerImage(w, h), (w * scale, w * scale))
        super().__init__(x, y, s, scale, True, z)
        self.rect = self.img.get_rect(center=(x, y))
        self.movement_composition = (0, 0)
        self.direction = (0, -1, False)
        self.sprite = SpriteCharacter(3, self.direction)
        #print(self.rect.center)

    def update(self, dt, events):
        for key in settings.DIRECT_DICT:
            if data.keys[key]:
                self.pos.x += settings.DIRECT_DICT[key][0] * settings.PLAYER_SPEED * dt
                self.pos.y += settings.DIRECT_DICT[key][1] * settings.PLAYER_SPEED * dt
        (self.rect.x, self.rect.y) = (self.pos.x, self.pos.y)
        (data.camera_position.x, data.camera_position.y) = (
            self.rect.center[0] - settings.SCREEN_SIZE.x / 2,
            self.rect.center[1] - settings.SCREEN_SIZE.y / 2,
        )
        self.clamp(data.screen_rect)
        data.player_self.update_pos(self.pos, self.direction)
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

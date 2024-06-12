import pygame

from data import camera_position


class GameObject(object):
    def __init__(self, x, y, img, scale, enabled=True, z=0):
        self.pos = pygame.math.Vector2(x, y)
        self.img = img
        self.scale = scale
        self.enabled = enabled
        self.z = z

    def update(self, dt):
        return

    def draw(self):
        if self.enabled:
            return self.img, (self.pos.x - camera_position.x, self.pos.y - camera_position.y)


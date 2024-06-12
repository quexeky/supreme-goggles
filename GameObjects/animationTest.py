import pygame

import GameObjects.gameObject


class AnimationTest(GameObjects.gameObject.GameObject):
    def __init__(self, x, y, w, h):
        s = pygame.Surface((w, h))
        s.fill((255, 255, 255))

        super().__init__()

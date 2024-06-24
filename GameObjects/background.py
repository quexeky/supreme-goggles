import pygame.image

import settings
from GameObjects.gameObject import GameObject
from Sprites.animatedSprite import AnimatedSprite
from Sprites.spriteSheets import parseSprites


# A sample to show how easy it is to add an animated object into the game, given a spritesheet
class Background(GameObject):
    def __init__(self, x, y, z):
        self.sprite = pygame.image.load("media/background.PNG").convert_alpha()
        s = pygame.transform.scale(self.sprite, (5000, 5000))

        super().__init__(x, y, s, 1, z=z)

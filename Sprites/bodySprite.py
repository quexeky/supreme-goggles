import pygame

import settings
from Sprites.conditionalAnimatedSprite import ConditionalAnimatedSprite
from Sprites.animatedSprite import animationConstructor
from Sprites.spriteSheets import parseSprites


def getSprite(spriteSheet, x, y, w, h):
    sprite = pygame.Surface((w, h), pygame.SRCALPHA)
    sprite.blit(spriteSheet, (0, 0), (x, y, w, h))
    return sprite


class BodySprite(pygame.sprite.Sprite):
    def __init__(self, name, spritesDir="media/"):
        super().__init__()
        sprites = parseSprites(
            name,
            8,
            3,
            24,
            settings.SPRITE_WIDTH,
            settings.SPRITE_HEIGHT,
            spritesDir=spritesDir,
            padding=0,
        )
        # Custom dictionary for quickly looking up all the sprites. Could probably be done in a function, but that
        # would be a bit slower and it's harder to get your head around to change. Hence this is the best option
        animations = {
            (0, -1, False): [sprites[8]],  # N
            (1, -1, False): [sprites[9]],  # NE
            (1, 0, False): [sprites[10]],  # E
            (1, 1, False): [sprites[11]],  # SE
            (0, 1, False): [sprites[12]],  # S
            (-1, 1, False): [sprites[13]],  # SW
            (-1, 0, False): [sprites[14]],  # W
            (-1, -1, False): [sprites[15]],  # NW
            (0, -1, True): animationConstructor(sprites, [0, 8, 16, 8]),  # N Walk
            (1, -1, True): animationConstructor(sprites, [1, 9, 17, 9]),  # NE Walk
            (1, 0, True): animationConstructor(sprites, [2, 10, 18, 10]),  # E Walk
            (1, 1, True): animationConstructor(sprites, [3, 11, 19, 11]),  # SE Walk
            (0, 1, True): animationConstructor(sprites, [4, 12, 20, 12]),  # S Walk
            (-1, 1, True): animationConstructor(sprites, [5, 13, 21, 13]),  # SW Walk
            (-1, 0, True): animationConstructor(sprites, [6, 14, 22, 14]),  # W Walk
            (-1, -1, True): animationConstructor(sprites, [7, 15, 23, 15]),  # NW Walk
        }

        # Think of it as a 2D array. The active animated sprite is the x, the actual frame is the y. Put in both
        # and then you get your desired sprite in a way that can be easily moved around
        self.styles = ConditionalAnimatedSprite(animations, index=(0, -1, True))

        self.image = self.styles.image
        self.rect = self.image.get_rect()

    def update(self, speed):
        self.styles.update(speed)
        self.image = self.styles.image

    def changeAnim(self, index):
        self.styles.index = index
        self.styles.changeAnim(index)

import pygame


# Inherited sprite class to create a sprite with multiple conditional animations. Ideal for player movement
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animation):
        super().__init__()

        self.currentSprite = 0                              # 0 is the base sprite, not in an animation
        print("Created Sprite")
        self.animation = animation                          #

        self.image = self.animation[self.currentSprite]
        self.rect = self.image.get_rect()

    def update(self, speed):
        self.currentSprite += speed
        # print(self.currentSprite)
        if int(self.currentSprite) >= len(self.animation):
            self.currentSprite = 0
        self.image = self.animation[
            int(self.currentSprite)
        ]  # rounds to nearest int so speed works
        # print("Updated animated sprite")


def spriteArrConstructor(sprites, indexes):
    arr = []
    for i in indexes:
        arr.append(sprites[i])
    return arr

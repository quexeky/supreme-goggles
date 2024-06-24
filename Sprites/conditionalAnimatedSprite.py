import pygame

from Sprites.animatedSprite import AnimatedSprite


# Inherited sprite class to create a sprite with multiple conditional animations. Ideal for player movement
class ConditionalAnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animations, index):
        super().__init__()

        self.index = index                                          # The ID of the animation to be in use
        self.animations = animations                                # Array of possible animations
        self.activeAnim = AnimatedSprite(self.animations[index])    # Currently active AnimatedSprite object

        self.image = self.activeAnim.image
        self.rect = self.image.get_rect()

    def update(self, speed):
        self.activeAnim.update(speed)
        self.image = self.activeAnim.image

    def changeAnim(self, index):
        self.index = index
        self.activeAnim = AnimatedSprite(self.animations[index])
        print("Changed Anim")


def conditionalAnimationConstructor(sprites, indexes):
    arr = []
    for i in indexes:
        arr.append(sprites[i])
    return arr

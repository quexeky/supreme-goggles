import pygame

from Sprites.animatedSprite import AnimatedSprite


# Inherited sprite class to create a sprite with multiple conditional animations. Ideal for player movement
class ConditionalAnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animations, index):
        super().__init__()

        # The ID of the animation to be in use
        self.index = index
        # Array of possible animations
        self.animations = animations
        # Currently active AnimatedSprite object
        self.activeAnim = AnimatedSprite(self.animations[index], 0)

        self.image = self.activeAnim.image
        self.rect = self.image.get_rect()

    # Branching down image generation to the most basic class
    def update(self, speed):
        self.activeAnim.update(speed)
        self.image = self.activeAnim.image

    # Branching down animation changing to the most basic class
    def changeAnim(self, index):
        self.index = index
        self.activeAnim = AnimatedSprite(
            self.animations[index], self.activeAnim.currentSprite
        )

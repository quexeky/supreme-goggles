import pygame


# Sprite class for simple sequential animations. Easy to use and implement
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animation, currentSprite=0):
        super().__init__()

        # 0 is the base sprite, not in an animation
        self.currentSprite = currentSprite

        # The array of sprites used to make up the animation
        self.animation = animation

        # The currently active image / animation frame
        self.image = self.animation[int(self.currentSprite % len(animation))]

        self.rect = self.image.get_rect()

    def update(self, speed):
        self.currentSprite += speed
        if int(self.currentSprite) >= len(self.animation):
            self.currentSprite = 0
        self.image = self.animation[
            int(self.currentSprite)
        ]  # rounds to nearest int so speed works


# Helper function for initialising Animations in a custom order
def animationConstructor(sprites, indexes):
    arr = []
    for i in indexes:
        arr.append(sprites[i])
    return arr

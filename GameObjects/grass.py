import settings
from GameObjects.gameObject import GameObject
from Sprites.animatedSprite import AnimatedSprite
from Sprites.spriteSheets import parseSprites


# A sample to show how easy it is to add an animated object into the game, given a sprite sheet
class Grass(GameObject):
    def __init__(self, x, y, z):
        self.sprite = AnimatedSprite(parseSprites("Grass", 5, 1, 5, 20, 14))
        super().__init__(x, y, self.sprite.image, 1, z=z)

    def update(self, dt, events):
        self.sprite.update(dt * settings.ANIMATION_RATE)
        self.img = self.sprite.image

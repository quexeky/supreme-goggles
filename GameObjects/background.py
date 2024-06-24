import pygame.image

from GameObjects.gameObject import GameObject


# Example background object. Done very basically, but hey, it works. And the simpler, the better, right?
class Background(GameObject):
    def __init__(self, x, y, z):
        self.sprite = pygame.image.load("media/background.PNG").convert_alpha()
        s = pygame.transform.scale(self.sprite, (4000, 2448))

        super().__init__(x, y, s, 1, z=z)

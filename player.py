import pygame

import settings
from settings import DIRECT_DICT


class Player(object):
    """This class will represent our user controlled character."""

    SIZE = (100, 100)

    def __init__(self, pos, speed):
        """
        Aside from setting up our image and rect as seen previously,
        in this example we create a new variable called true_pos.
        Rects can only hold integers, so in order to preserve fractional
        changes we need this new variable to hold the exact float position.
        Without it, a body that moved slower than 1 pixel per frame would
        never move.
        """
        self.image = draw_player()
        self.rect = self.image.get_rect(center=pos)
        self.true_pos = list(self.rect.center)  # Exact float position.
        self.speed = speed  # Speed in pixels per second.

    def update(self, keys, screen_rect, dt):
        """
        Update must accept a new argument dt (time delta between frames).
        Adjustments to position must be multiplied by this delta.
        Set the rect to true_pos once adjusted (automatically converts to int).
        """
        for key in DIRECT_DICT:
            if keys[key]:
                self.true_pos[0] += DIRECT_DICT[key][0] * self.speed * dt
                self.true_pos[1] += DIRECT_DICT[key][1] * self.speed * dt
        self.rect.center = self.true_pos
        self.clamp(screen_rect)

    def clamp(self, screen_rect):
        """
        Clamp the rect to the screen if needed and reset true_pos to the
        rect position so they don't lose sync.
        """
        if not screen_rect.contains(self.rect):
            self.rect.clamp_ip(screen_rect)
            self.true_pos = list(self.rect.center)

    def draw(self, surface):
        """
        Basic draw function.
        """
        surface.blit(self.image, self.rect)


def draw_player():
    """
    Create player image. No differences from previous.
    """
    image = pygame.Surface(Player.SIZE).convert_alpha()
    image.fill(settings.TRANSPARENT)
    rect = image.get_rect()
    pygame.draw.ellipse(image, pygame.Color("black"), rect)
    pygame.draw.ellipse(image, pygame.Color("tomato"), rect.inflate(-50, -50))
    return image

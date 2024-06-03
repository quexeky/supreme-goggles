import pygame

import settings
from player import Player


class App(object):
    """
    Class responsible for program control flow.
    """

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.player = Player(self.screen_rect.center, 300)

    def event_loop(self):
        """
        Basic event loop.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                self.keys = pygame.key.get_pressed()

    def update(self, dt):
        """
        Update must acccept and pass dt to all elements that need to update.
        """
        self.player.update(self.keys, self.screen_rect, dt)

    def render(self):
        """
        Render all needed elements and update the display.
        """
        self.screen.fill(settings.BACKGROUND_COLOR)
        self.player.draw(self.screen)
        pygame.display.update()

    def main_loop(self):
        """
        We now use the return value of the call to self.clock.tick to
        get the time delta between frames.
        """
        dt = 0
        self.clock.tick(self.fps)
        while not self.done:
            self.event_loop()
            self.update(dt)
            self.render()
            dt = self.clock.tick(self.fps) / 1000.0

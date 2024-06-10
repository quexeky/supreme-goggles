import pygame

import data
import settings


class App(object):
    """
    Class responsible for program control flow.
    """

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.gameObjects = []
        data.screen_rect = self.screen.get_rect()
        data.keys = pygame.key.get_pressed()

    def event_loop(self):
        """
        Basic event loop.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                data.keys = pygame.key.get_pressed()
            if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                settings.SCREEN_SIZE = (event.w, event.h)
                self.screen = pygame.display.set_mode(
                    settings.SCREEN_SIZE, pygame.RESIZABLE
                )
                data.screen_rect = self.screen.get_rect()

    def update(self, dt):
        """
        Update must acccept and pass dt to all elements that need to update.
        """
        for gameObject in self.gameObjects:
            gameObject.update(dt)

    def render(self):
        """
        Render all needed elements and update the display.
        """
        self.screen.fill(settings.BACKGROUND_COLOR)
        for gameObject in self.gameObjects:
            gameObject.draw(self.screen)

        pygame.display.update()

    def addGameObject(self, gameObject):
        self.gameObjects.append(gameObject)

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

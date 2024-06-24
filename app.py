import pygame

import data
import settings
from playerData import calculate_age


# Class responsible for maintaining the application flow
class App(object):
    def __init__(self):
        self.events = None
        self.screen = pygame.display.get_surface()
        data.clock = pygame.time.Clock()
        self.fps = 10000
        self.done = False
        self.gameObjects = []
        data.screen_rect = self.screen.get_rect()
        data.keys = pygame.key.get_pressed()

    def event_loop(self):
        # Basic game event loop. Nothing special
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                data.keys = pygame.key.get_pressed()
            if event.type == pygame.VIDEORESIZE:
                # Allows resizing of the window, but could definitely be done better
                settings.SCREEN_SIZE = pygame.Vector2(event.w, event.h)
                self.screen = pygame.display.set_mode(
                    settings.SCREEN_SIZE, pygame.RESIZABLE
                )
                data.screen_rect = self.screen.get_rect()

    def update(self, dt):
        # Calculate age in this loop because the actual client code is in a separate (read-only) thread
        data.current_time = calculate_age()
        for gameObject in self.gameObjects:
            gameObject.update(dt, self.events)

    def render(self):
        # Render all elements to the display with the background as the base
        self.screen.fill(settings.BACKGROUND_COLOR)
        to_draw = []
        for gameObject in self.gameObjects:
            to_draw.append(gameObject.draw())

        # Draw everything in a single GPU call. Much more efficient
        self.screen.blits(to_draw)
        pygame.display.update()

    # Quick way of ensuring a z positioning. Very useful for draw priority
    def addGameObject(self, gameObject):
        self.gameObjects.append(gameObject)

        self.gameObjects.sort(key=lambda x: x.z)

    def main_loop(self):
        dt = 0
        data.clock.tick(self.fps)
        while not self.done:
            self.event_loop()
            self.update(dt)
            self.render()
            dt = data.clock.tick(self.fps) / 1000.0

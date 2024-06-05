import app
import os
import sys
import pygame

import data
import settings
from GameObjects.displayPlayer import DisplayPlayer
# import networking.server
from GameObjects.widgets.button import Button
from GameObjects.player import Player


def main():
    """
    Initialize; create an App; and start the main loop.
    """
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption(settings.CAPTION)
    pygame.display.set_mode(settings.SCREEN_SIZE, pygame.RESIZABLE)
    pygame.font.init()
    data.keys = pygame.key.get_pressed()
    data.screen_rect = pygame.display.get_surface().get_rect()
    game = app.App()
    game.addGameObject(Button(100, 100, 150, 150, text="Hi hooman", textSize=30))
    game.addGameObject(Button(500, 50, 100, 100, text="Hello, Jess", textSize=15))
    game.addGameObject(Player(300, 300, 50, 50, 1))
    game.addGameObject(DisplayPlayer(300, 300, 50, 50, 1))
    game.main_loop()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

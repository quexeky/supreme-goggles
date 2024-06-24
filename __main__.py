import os
import sys
import threading

import pygame

import app
import data
import settings
from GameObjects.player import Player

# import networking.server
from GameObjects.widgets.button import Button
from GameObjects.widgets.fps_counter import FPS
from networking.client import server_connect


def main():
    """
    Initialize; create an App; and start the main loop.
    """
    settings.host = input("Host IP:")
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption(settings.CAPTION)
    pygame.display.set_mode(settings.SCREEN_SIZE, pygame.RESIZABLE)
    pygame.font.init()
    data.keys = pygame.key.get_pressed()
    data.screen_rect = pygame.display.get_surface().get_rect()
    game = app.App()
    game.addGameObject(Button(100, 100, 150, 150, text="Hi hooman", textSize=30))
    game.addGameObject(Button(500, 50, 100, 100, text="Hello, Jess", textSize=15))
    game.addGameObject(Player(300, 300, 50, 50, 3, 10))
    game.addGameObject(FPS(0, 0, z=100))
    threading.Thread(target=server_connect, args=(game,), daemon=True).start()
    game.main_loop()
    pygame.quit()
    sys.exit()


def background(game):
    game.addGameObject(
        Button(100, 500, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        Button(100, 600, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        Button(100, 750, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        Button(100, 800, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        Button(100, 850, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        Button(100, 1000, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )


if __name__ == "__main__":
    main()

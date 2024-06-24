import os
import sys
import threading

import pygame

import app
import data
import settings
from GameObjects.grass import Grass
from GameObjects.background import Background
from GameObjects.player import Player

# import networking.server
from GameObjects.widgets.textbox import TextBox
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
    game.addGameObject(Background(-2000, -1000, -10))
    game.addGameObject(TextBox(-3500, 0, 200, 100, text="Hello, human", textSize=30, textColour="white", colour="black"))
    game.addGameObject(TextBox(-6000, 0, 250, 100, text="Why are you here?", textSize=30, textColour="white", colour="black"))
    game.addGameObject(TextBox(-10000, 0, 500, 100, text="There's nothing out here, you know", textSize=30, textColour="white", colour="black"))
    game.addGameObject(TextBox(-15000, 0, 300, 100, text="I mean it", textSize=30, textColour="white", colour="black"))
    game.addGameObject(TextBox(-50000, 0, 300, 100, text="You idiot", textSize=30, textColour="white", colour="black"))
    game.addGameObject(Player(300, 300, 50, 50, 3, 10))
    game.addGameObject(Grass(350, 350, 1000))
    game.addGameObject(FPS(0, 0, z=100))
    threading.Thread(target=server_connect, args=(game,), daemon=True).start()
    game.main_loop()
    pygame.quit()
    sys.exit()


def background(game):
    game.addGameObject(
        TextBox(100, 500, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        TextBox(100, 600, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        TextBox(100, 750, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        TextBox(100, 800, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        TextBox(100, 850, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )
    game.addGameObject(
        TextBox(100, 1000, 150, 150, text="WEEEEEEEEEEEEEEEEEEE", textSize=30)
    )


if __name__ == "__main__":
    main()

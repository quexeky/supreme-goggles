import app
import os
import sys
import pygame

import settings
# import networking.server
from widgets.button import Button


def main():
    """
    Initialize; create an App; and start the main loop.
    """
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption(settings.CAPTION)
    pygame.display.set_mode(settings.SCREEN_SIZE, pygame.RESIZABLE)
    pygame.font.init()
    game = app.App()
    game.addWidget(Button(100, 100, 70, 70, text="Hello, World", textSize=10))
    game.addWidget(Button(500, 50, 100, 100, text="Hello, Jess", textSize=30))
    game.main_loop()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

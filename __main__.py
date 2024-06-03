import app
import os
import sys
import pygame

import settings
import networking.server


def main():
    networking.server.Server()
    """
    Initialize; create an App; and start the main loop.
    """
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption(settings.CAPTION)
    pygame.display.set_mode(settings.SCREEN_SIZE)
    app.App().main_loop()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

import pygame

MAPSIZE = pygame.math.Vector2(0, 0)
CAPTION = "Supreme Goggles"
SCREEN_SIZE = (500, 500)
TRANSPARENT = (0, 0, 0, 0)
BACKGROUND_COLOR = pygame.Color("darkslategrey")
DIRECT_DICT = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1)
}

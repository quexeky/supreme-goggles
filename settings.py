import pygame

MAPSIZE = pygame.math.Vector2(0, 0)
CAPTION = "Supreme Goggles"
SCREEN_SIZE = pygame.Vector2(500, 500)
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
    pygame.K_s: (0, 1),
}
PLAYER_COLOUR = "tomato"
PLAYER_SPEED = 300

host = "127.0.0.1"
PORT = 8090

playerDimensions = (50, 50)


def playerImage(w, h):
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.circle(s, PLAYER_COLOUR, s.get_rect().center, w / 2)
    s = s.convert_alpha()
    return s

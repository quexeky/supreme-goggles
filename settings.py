import pygame

MAPSIZE = pygame.math.Vector2(0, 0)
CAPTION = "Supreme Goggles"
SCREEN_SIZE = pygame.math.Vector2(1000, 1000)
BACKGROUND_COLOR = pygame.Color("black")
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

PLAYER_SPEED = 300
ANIMATION_RATE = 4

host = "0.0.0.0"
PORT = 8090

SPRITE_WIDTH = 18
SPRITE_HEIGHT = 23

PACKET_SIZE = 26

PASSIVE_UPDATE_FREQUENCY = 0.1


max_data_age = 200000

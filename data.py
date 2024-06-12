import pygame

from playerData import PlayerData

camera_position = pygame.math.Vector2(0, 0)
keys = 0
screen_rect = 0
player_self = PlayerData(0, 0, 0, True)
player_pos = pygame.Vector2((0, 0))
others = {}

import pygame

from playerData import PlayerData

camera_position = pygame.math.Vector2(0, 0)
keys = 0
screen_rect = 0
player_self = PlayerData(int(0), int(0), int(0), (0, 1, False), (0, 0, 0))
player_pos = pygame.Vector2((0, 0))
others = {}
player_pos_updated = True
clock = None

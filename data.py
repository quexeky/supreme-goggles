import pygame

from playerData import PlayerData, calculate_age

# Variables that are too far passed down the chain to be worth including. These variables must never be written to
# twice at once though. That's how you get a segfault or some other major error

camera_position = pygame.math.Vector2(0, 0)
keys = 0
screen_rect = 0
player_self = PlayerData(int(0), int(0), int(0), (0, 1, False), (0, 0, 0))
player_pos = pygame.Vector2((0, 0))
others = {}
player_pos_updated = True
clock = None
current_time = calculate_age()

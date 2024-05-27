import pygame
import settings


class Character:
    __name = "UNDEFINED"
    __id = 0
    __position = pygame.math.Vector2(0, 0)
    __features = (0, 0, 0)

    def __init__(self, name, characterId, features):
        self.id = characterId
        self.__name = name
        self.__features = features

    def move(self, posDelta):
        self.__position += posDelta

        if self.__position.x > settings.mapSize.x:
            self.__position = settings.mapSize.x
        elif self.__position.x < 0:
            self.__position = 0

        if self.__position.y > settings.mapSize.y:
            self.__position = settings.mapSize.y
        elif self.__position.y < 0:
            self.__position = 0


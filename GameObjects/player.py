import pygame.transform

import data
import settings
from GameObjects import gameObject
from Sprites.sprites import CharacterSprite


class Player(gameObject.GameObject):
    def __init__(self, x, y, w, h, scale, z=1):
        self.moving = False
        self.direction = (0, -1, False)
        self.sprite = CharacterSprite(3, self.direction)
        self.rect = self.sprite.img.get_rect(center=(x, y))

        super().__init__(x, y, self.sprite.img, scale, True, z)

    def update(self, dt, events):
        self.updatePlayerPos(dt)

        self.updateCharacterSprite(events)

        self.sprite.spriteUpdate(dt)

        self.img = self.sprite.img
        self.rect = self.img.get_rect(center=(self.pos.x, self.pos.y))

    def updatePlayerPos(self, dt):
        # Just getting position vectors as individual values because python hates tuple addition for some reason
        posUpdateX = 0
        posUpdateY = 0
        for key in settings.DIRECT_DICT:
            if data.keys[key]:
                posUpdateX += settings.DIRECT_DICT[key][0]
                posUpdateY += settings.DIRECT_DICT[key][1]

        # Using this as a dirty way to update direction. It works the exact same as normal, just in a different spot
        # I don't like it because it looks ugly, but it works well
        self.moving = (posUpdateX, posUpdateY) != (0, 0)

        self.direction = (posUpdateX, posUpdateY, self.moving)
        self.sprite.direction = self.direction

        # Normalise the movement value if both values are either 1 or -1 to stop the play from moving too fast
        if abs(posUpdateX) == 1 and abs(posUpdateY) == 1:
            # Multiply by ~sqrt(2) because Pythagoras
            (posUpdateX, posUpdateY) = (posUpdateX * 1.412 / 2, posUpdateY * 1.412 / 2)

        # Update player position
        self.pos += pygame.Vector2(
            (
                posUpdateX * settings.PLAYER_SPEED * dt,
                posUpdateY * settings.PLAYER_SPEED * dt,
            )
        )
        (self.rect.x, self.rect.y) = (self.pos.x, self.pos.y)

        # Set the camera position relative to the player
        (data.camera_position.x, data.camera_position.y) = (
            self.rect.center[0] - settings.SCREEN_SIZE.x / 2,
            self.rect.center[1] - settings.SCREEN_SIZE.y / 2,
        )

        data.player_self.update_pos(self.pos, self.direction, self.sprite.styleIndexes)

    # Changing the player sprites. Might be able to put it into a dictonary like the DATA_DICT, but to be frank it's
    # a massive amount of trouble optimising something that doesn't need to be optimised. And it would probably be
    # slower anyways. So we get this
    def updateCharacterSprite(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_i:
                        self.sprite.replace_animation(self.sprite.Head, -1)
                    case pygame.K_p:
                        self.sprite.replace_animation(self.sprite.Head, 1)
                    case pygame.K_j:
                        self.sprite.replace_animation(self.sprite.Torso, -1)
                    case pygame.K_l:
                        self.sprite.replace_animation(self.sprite.Torso, 1)
                    case pygame.K_n:
                        self.sprite.replace_animation(self.sprite.Legs, -1)
                    case pygame.K_COMMA:
                        self.sprite.replace_animation(self.sprite.Legs, 1)
                self.sprite.styleIndexes = (
                    self.sprite.Head.styleIndex,
                    self.sprite.Torso.styleIndex,
                    self.sprite.Legs.styleIndex,
                )
                self.sprite.changeFullAnimation(self.direction)
            if event.type == pygame.KEYUP:
                self.sprite.changeFullAnimation(self.direction)

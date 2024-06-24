import pygame

import data
import settings
from Sprites.bodySprite import BodySprite
from Sprites.bodyType import BodyType


class SpriteCharacter(object):
    def __init__(self, scale, direction):
        self.img = pygame.Surface((0, 0))
        self.num = 0
        self.Head = BodyType([BodySprite("head1"), BodySprite("head2"), BodySprite("head3"), BodySprite("head4"), BodySprite("head5")], animation=direction)
        self.Torso = BodyType([BodySprite("torso1"), BodySprite("torso2"), BodySprite("torso3"), BodySprite("torso4"), BodySprite("torso5")], animation=direction)
        self.Legs = BodyType([BodySprite("legs1"), BodySprite("legs2"), BodySprite("legs3"), BodySprite("legs4"), BodySprite("legs5")], animation=direction)
        self.movement_composition = (0, 0)
        self.direction = direction
        self.styleIndexes = (0, 0, 0)

        # Creating the sprites and groups
        moving_sprites = pygame.sprite.Group()
        moving_sprites.add(self.Head.style)
        moving_sprites.add(self.Torso.style)
        moving_sprites.add(self.Legs.style)

        self.moving_sprites = moving_sprites

        self.scale = scale

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_i:
                        self.moving_sprites.remove(self.Head.style)
                        self.moving_sprites.add(self.Head.changeStyle(-1))
                    case pygame.K_p:
                        self.moving_sprites.remove(self.Head.style)
                        self.moving_sprites.add(self.Head.changeStyle(1))
                    case pygame.K_j:
                        self.moving_sprites.remove(self.Torso.style)
                        self.moving_sprites.add(self.Torso.changeStyle(-1))
                    case pygame.K_l:
                        self.moving_sprites.remove(self.Torso.style)
                        self.moving_sprites.add(self.Torso.changeStyle(1))
                    case pygame.K_n:
                        self.moving_sprites.remove(self.Legs.style)
                        self.moving_sprites.add(self.Legs.changeStyle(-1))
                    case pygame.K_COMMA:
                        self.moving_sprites.remove(self.Legs.style)
                        self.moving_sprites.add(self.Legs.changeStyle(1))
                self.styleIndexes = (self.Head.styleIndex, self.Torso.styleIndex, self.Legs.styleIndex)
                self.update_walk()
                self.changeFullAnimation(self.direction)
            if event.type == pygame.KEYUP:
                self.update_walk()
                self.changeFullAnimation(self.direction)

    def tick(self, dt):
        self.moving_sprites.update(dt * settings.ANIMATION_RATE)

        screen = pygame.Surface((settings.spriteWidth, settings.spriteHeight), pygame.SRCALPHA)
        self.moving_sprites.draw(screen)
        # print(self.moving_sprites.sprites())
        # print("Reassigned self.img")
        pygame.transform.flip(screen, False, True)
        self.img = pygame.transform.scale(screen,
                                          (settings.spriteWidth * self.scale, settings.spriteHeight * self.scale))

    def changeFullAnimation(self, direction):
        # print(direction)
        self.Head.changeAnim(direction)
        self.Torso.changeAnim(direction)
        self.Legs.changeAnim(direction)
        # print("Changed to go", direction)

    def update_walk(self):
        x = 0
        y = 0
        for key in settings.DIRECT_DICT:
            if data.keys[key]:
                x += settings.DIRECT_DICT[key][0]
                y += settings.DIRECT_DICT[key][1]
        self.movement_composition = (x, y)

        print(self.movement_composition != (0, 0))

        moving = self.movement_composition != (0, 0)

        self.direction = (x, y, moving)

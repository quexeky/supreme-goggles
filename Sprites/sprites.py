import pygame

import data
import settings
from Sprites.bodyType import BodyType, createStyleArr


class SpriteCharacter(object):
    def __init__(self, scale, direction):
        self.img = pygame.Surface((0, 0))
        self.num = 0
        self.Head = BodyType(
            createStyleArr(["head1", "head2", "head3", "head4", "head5"], settings.SPRITE_HEIGHT, settings.SPRITE_WIDTH),
            animation=direction,
        )
        self.Torso = BodyType(
            createStyleArr(["torso1", "torso2", "torso3", "torso4", "torso5"], settings.SPRITE_HEIGHT, settings.SPRITE_WIDTH),
            animation=direction,
        )
        self.Legs = BodyType(
            createStyleArr(["legs1", "legs2", "legs3", "legs4", "legs5"], settings.SPRITE_HEIGHT, settings.SPRITE_WIDTH),
            animation=direction,
        )
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
                        self.replace_animation(self.Head, -1)
                    case pygame.K_p:
                        self.replace_animation(self.Head, 1)
                    case pygame.K_j:
                        self.replace_animation(self.Torso, -1)
                    case pygame.K_l:
                        self.replace_animation(self.Torso, 1)
                    case pygame.K_n:
                        self.replace_animation(self.Legs, -1)
                    case pygame.K_COMMA:
                        self.replace_animation(self.Torso, 1)
                self.styleIndexes = (
                    self.Head.styleIndex,
                    self.Torso.styleIndex,
                    self.Legs.styleIndex,
                )
                self.updateWalk()
                self.changeFullAnimation(self.direction)
                self.Head.changeAnim(self.direction)
                self.Torso.changeAnim(self.direction)
                self.Legs.changeAnim(self.direction)
            if event.type == pygame.KEYUP:
                self.updateWalk()
                self.changeFullAnimation(self.direction)

    def tick(self, dt):
        self.moving_sprites.update(dt * settings.ANIMATION_RATE)

        screen = pygame.Surface(
            (settings.SPRITE_WIDTH, settings.SPRITE_HEIGHT), pygame.SRCALPHA
        )
        self.moving_sprites.draw(screen)
        pygame.transform.flip(screen, False, True)
        self.img = pygame.transform.scale(
            screen,
            (settings.SPRITE_WIDTH * self.scale, settings.SPRITE_HEIGHT * self.scale),
        )

    def changeFullAnimation(self, direction):
        self.Head.changeAnim(direction)
        self.Torso.changeAnim(direction)
        self.Legs.changeAnim(direction)

    def updateWalk(self):
        x = 0
        y = 0
        for key in settings.DIRECT_DICT:
            if data.keys[key]:
                x += settings.DIRECT_DICT[key][0]
                y += settings.DIRECT_DICT[key][1]

        self.movement_composition = (x, y)
        moving = self.movement_composition != (0, 0)

        self.direction = (x, y, moving)

    def replace_animation(self, animation, style):
        self.moving_sprites.remove(animation.style)
        self.moving_sprites.add(animation.changeStyle(style))
        return

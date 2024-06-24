import pygame

import settings
from Sprites.bodyType import BodyType, createBodySpriteArr


# Custom implemented class for our own Sprite behaviours
class CharacterSprite(object):
    def __init__(self, scale, direction):
        self.img = pygame.Surface((0, 0))
        self.num = 0
        self.Head = BodyType(
            createBodySpriteArr(["head1", "head2", "head3", "head4", "head5"]),
            animation=direction,
        )
        self.Torso = BodyType(
            createBodySpriteArr(["torso1", "torso2", "torso3", "torso4", "torso5"]),
            animation=direction,
        )
        self.Legs = BodyType(
            createBodySpriteArr(["legs1", "legs2", "legs3", "legs4", "legs5"]),
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

    def update(self, events):  # TODO: Clean up
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
                self.changeFullAnimation(self.direction)
            if event.type == pygame.KEYUP:
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

    def replace_animation(self, animation, style):
        self.moving_sprites.remove(animation.style)
        self.moving_sprites.add(animation.changeStyle(style))
        return

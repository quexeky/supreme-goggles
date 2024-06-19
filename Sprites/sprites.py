import pygame

from GameObjects import gameObject
from Sprites.bodySprite import BodySprite
from Sprites.bodyType import BodyType


class SpriteCharacter(gameObject.GameObject):
    def __init__(self, x, y, z):
        self.num = 0
        self.Head = BodyType([BodySprite("Head"), BodySprite("Head2")])
        self.Torso = BodyType([BodySprite("Torso"), BodySprite("Torso2")])
        self.Legs = BodyType([BodySprite("Legs"), BodySprite("Legs2")])

        # Creating the sprites and groups
        moving_sprites = pygame.sprite.Group()
        moving_sprites.add(self.Head.style)
        moving_sprites.add(self.Torso.style)
        moving_sprites.add(self.Legs.style)

        self.moving_sprites = moving_sprites

        s = pygame.Surface((500, 500), pygame.SRCALPHA)
        super().__init__(x, y, s, 1, z)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.Head.changeAnim("N_walk")
                self.Torso.changeAnim("N_walk")
                self.Legs.changeAnim("N_walk")
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        print("Pressed Q")
                        self.moving_sprites.remove(self.Head.style)
                        self.moving_sprites.add(self.Head.selectStyle(-1))
                    case pygame.K_e:
                        self.moving_sprites.remove(self.Head.style)
                        self.moving_sprites.add(self.Head.selectStyle(1))
                    case pygame.K_a:
                        self.moving_sprites.remove(self.Torso.style)
                        self.moving_sprites.add(self.Torso.selectStyle(-1))
                    case pygame.K_d:
                        self.moving_sprites.remove(self.Torso.style)
                        self.moving_sprites.add(self.Torso.selectStyle(1))
                    case pygame.K_z:
                        self.moving_sprites.remove(self.Legs.style)
                        self.moving_sprites.add(self.Legs.selectStyle(-1))
                    case pygame.K_c:
                        self.moving_sprites.remove(self.Legs.style)
                        self.moving_sprites.add(self.Legs.selectStyle(1))

        screen = pygame.Surface((500, 500), pygame.SRCALPHA)
        self.moving_sprites.draw(screen)
        self.moving_sprites.update(0.25)
        # print(self.moving_sprites.sprites())
        pygame.transform.flip(screen, False, True)

        self.img = screen


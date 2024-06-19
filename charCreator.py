import pygame
import sys


class BodyType:
    def __init__(self, styles, styleIndex=0, animation="N"):
        self.style = None
        self.styles = styles
        self.styleIndex = styleIndex
        self.animation = animation

        self.selectStyle(0)

    def selectStyle(self, num):
        self.styleIndex += num
        self.style = self.styles[self.styleIndex % len(self.styles)]
        self.changeAnim(self.animation)
        return self.style

    def changeAnim(self, key):
        self.style.activeAnim = self.style.animations[key]
        self.animation = key
        return self.style.activeAnim


spritesDir = "media/"


class BodySprite(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()

        self.spriteSheet = None
        self.sprites = []
        self.parseSprites(name, 8, 3, 24, 12, 18, 6)

        self.animations = {
            "N": [self.sprites[8]],
            "NE": [self.sprites[9]],
            "E": [self.sprites[10]],
            "SE": [self.sprites[11]],
            "S": [self.sprites[12]],
            "SW": [self.sprites[13]],
            "W": [self.sprites[14]],
            "NW": [self.sprites[15]],
            "N_walk": [self.sprites[0], self.sprites[8], self.sprites[16]],
            "NE_walk": [self.sprites[1], self.sprites[9], self.sprites[17]],
            "E_walk": [self.sprites[2], self.sprites[10], self.sprites[18]],
            "SE_walk": [self.sprites[3], self.sprites[11], self.sprites[19]],
            "S_walk": [self.sprites[4], self.sprites[12], self.sprites[20]],
            "SW_walk": [self.sprites[5], self.sprites[13], self.sprites[21]],
            "W_walk": [self.sprites[6], self.sprites[14], self.sprites[22]],
            "NW_walk": [self.sprites[7], self.sprites[15], self.sprites[23]],
        }
        self.currentSprite = 0  #0 is the base sprite, not in an animation
        self.activeAnim = self.animations["S"]

        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [250, 250]

    def getSprite(self, spriteSheet, x, y, w, h):
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(spriteSheet, (0, 0), (x, y, w, h))
        return sprite

    def parseSprites(self, name, rows, columns, length, width, height, padding=0):
        self.spriteSheet = pygame.image.load(f'{spritesDir}{name}.png')

        count = 0
        for y in range(columns):
            for x in range(rows):
                count += 1
                if count > length:
                    break
                self.sprites.append(
                    self.getSprite(self.spriteSheet, x * width + x * padding, y * height + y * padding, width, height))

    def update(self, speed):
        self.currentSprite += speed
        if int(self.currentSprite) >= len(self.activeAnim):
            self.currentSprite = 0
        self.image = self.activeAnim[int(self.currentSprite)]  #rounds to nearest int so speed works


Head = BodyType([BodySprite("Head"), BodySprite("Head2")])
Torso = BodyType([BodySprite("Torso"), BodySprite("Torso2")])
Legs = BodyType([BodySprite("Legs"), BodySprite("Legs2")])

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Customization demo")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
moving_sprites.add(Head.style)
moving_sprites.add(Torso.style)
moving_sprites.add(Legs.style)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Head.changeAnim("N_walk")
            Torso.changeAnim("N_walk")
            Legs.changeAnim("N_walk")
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    moving_sprites.remove(Head.style)
                    moving_sprites.add(Head.selectStyle(-1))
                case pygame.K_e:
                    moving_sprites.remove(Head.style)
                    moving_sprites.add(Head.selectStyle(1))
                case pygame.K_a:
                    moving_sprites.remove(Torso.style)
                    moving_sprites.add(Torso.selectStyle(-1))
                case pygame.K_d:
                    moving_sprites.remove(Torso.style)
                    moving_sprites.add(Torso.selectStyle(1))
                case pygame.K_z:
                    moving_sprites.remove(Legs.style)
                    moving_sprites.add(Legs.selectStyle(-1))
                case pygame.K_c:
                    moving_sprites.remove(Legs.style)
                    moving_sprites.add(Legs.selectStyle(1))

    # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)

import pygame


def getSprite(spriteSheet, x, y, w, h):
    sprite = pygame.Surface((w, h), pygame.SRCALPHA)
    sprite.blit(spriteSheet, (0, 0), (x, y, w, h))
    return sprite


class BodySprite(pygame.sprite.Sprite):
    def __init__(self, name, direction=(0, -1, False)):
        super().__init__()

        self.spriteSheet = None
        self.spritesDir = "media/"

        self.sprites = []
        self.parseSprites(name, 8, 3, 24, 18, 24, 0)

        self.animations = {
            (0, -1, False): [self.sprites[8]],                                                           # N
            (1, -1, False): [self.sprites[9]],                                                           # NE
            (1, 0, False): [self.sprites[10]],                                                          # E
            (1, 1, False): [self.sprites[11]],                                                         # SE
            (0, 1, False): [self.sprites[12]],                                                         # S
            (-1, 1, False): [self.sprites[13]],                                                        # SW
            (-1, 0, False): [self.sprites[14]],                                                         # W
            (-1, -1, False): [self.sprites[15]],                                                         # NW
            (0, -1, True): [self.sprites[0], self.sprites[8], self.sprites[16], self.sprites[8]],        # N Walk
            (1, -1, True): [self.sprites[1], self.sprites[9], self.sprites[17], self.sprites[9]],        # NE Walk
            (1, 0, True): [self.sprites[2], self.sprites[10], self.sprites[18], self.sprites[10]],      # E Walk
            (1, 1, True): [self.sprites[3], self.sprites[11], self.sprites[19], self.sprites[11]],     # SE Walk
            (0, 1, True): [self.sprites[4], self.sprites[12], self.sprites[20], self.sprites[12]],     # S Walk
            (-1, 1, True): [self.sprites[5], self.sprites[13], self.sprites[21], self.sprites[13]],    # SW Walk
            (-1, 0, True): [self.sprites[6], self.sprites[14], self.sprites[22], self.sprites[14]],     # W Walk
            (-1, -1, True): [self.sprites[7], self.sprites[15], self.sprites[23], self.sprites[15]],     # NW Walk
        }
        self.currentSprite = 0  # 0 is the base sprite, not in an animation
        self.activeAnim = self.animations[direction]

        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()

    def parseSprites(self, name, rows, columns, length, width, height, padding=0):
        self.spriteSheet = pygame.image.load(f"{self.spritesDir}{name}.PNG")

        count = 0
        for y in range(columns):
            for x in range(rows):
                count += 1
                if count > length:
                    break
                self.sprites.append(
                    getSprite(
                        self.spriteSheet,
                        x * width + x * padding + 2,
                        y * height + y * padding + 2,
                        width,
                        height,
                    )
                )
        # print(count)

    def update(self, speed):
        self.currentSprite += speed
        # print(speed)
        if int(self.currentSprite) >= len(self.activeAnim):
            self.currentSprite = 0
        self.image = self.activeAnim[
            int(self.currentSprite)
        ]  # rounds to nearest int so speed works

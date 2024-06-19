import pygame


class BodySprite(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()

        self.spriteSheet = None
        self.spritesDir = "media/"

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
        self.currentSprite = 0  # 0 is the base sprite, not in an animation
        self.activeAnim = self.animations["S"]

        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [250, 250]

    def getSprite(self, spriteSheet, x, y, w, h):
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(spriteSheet, (0, 0), (x, y, w, h))
        return sprite

    def parseSprites(self, name, rows, columns, length, width, height, padding=0):
        self.spriteSheet = pygame.image.load(f"{self.spritesDir}{name}.png")

        count = 0
        for y in range(columns):
            for x in range(rows):
                count += 1
                if count > length:
                    break
                self.sprites.append(
                    self.getSprite(
                        self.spriteSheet,
                        x * width + x * padding,
                        y * height + y * padding,
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

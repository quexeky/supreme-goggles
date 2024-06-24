import pygame


def getSprite(spriteSheet, x, y, w, h):
    sprite = pygame.Surface((w, h), pygame.SRCALPHA)
    sprite.blit(spriteSheet, (0, 0), (x, y, w, h))
    return sprite


def parseSprites(name, rows, columns, length, width, height, spritesDir="media/", padding=0):
    spriteSheet = pygame.image.load(f"{spritesDir}{name}.PNG")

    sprites = []

    count = 0
    for y in range(columns):
        for x in range(rows):
            count += 1
            if count > length:
                break
            sprites.append(
                getSprite(
                    spriteSheet,
                    x * width + x * padding,
                    y * height + y * padding,
                    width,
                    height,
                )
            )
    # print(count)
    return sprites

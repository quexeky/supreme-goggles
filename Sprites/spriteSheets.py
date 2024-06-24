import pygame


# Helper function to get a single sprite from a sprite sheet
def getSprite(spriteSheet, x, y, w, h):
    sprite = pygame.Surface((w, h), pygame.SRCALPHA)
    sprite.blit(spriteSheet, (0, 0), (x, y, w, h))
    return sprite


# Helper function to convert a sprite sheet into an array of sprites
def parseSprites(
    name, rowWidth, columnHeight, length, width, height, spritesDir="media/", padding=0
):
    spriteSheet = pygame.image.load(f"{spritesDir}{name}.PNG")

    sprites = []

    count = 0
    for y in range(columnHeight):
        for x in range(rowWidth):
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

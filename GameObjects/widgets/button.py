import pygame
import pygame.freetype

from GameObjects.widgets import widget


class Button(widget.Widget):
    def __init__(self, x, y, w, h, text="", textSize=20, textColour="black", colour="white"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        s = pygame.Surface((w, h))
        pygame.draw.rect(s, colour, pygame.Rect(0, 0, w, h))
        if text != "":
            font = pygame.font.SysFont('Arial', textSize)
            text = font.render(text, True, textColour)
            textRect = text.get_rect()
            textRect.center = s.get_rect().center
            print(textRect.center)
            # s.blit(text, textRect)
            s.blit(text, textRect)

        super().__init__(x, y, w, h, s, text, textSize, textColour, colour)

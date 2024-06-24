import pygame
import pygame.freetype

from GameObjects.widgets import widget


# Was supposed to be a button class, but that kind of fell through. Pre-render the textbox so that you don't have to
# keep rendering it (thank you GameObject)
class TextBox(widget.Widget):
    def __init__(
        self, x, y, w, h, text="", textSize=20, textColour="black", colour="white", z=0
    ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.textColour = textColour
        s = pygame.Surface((w, h))
        pygame.draw.rect(s, colour, pygame.Rect(0, 0, w, h))
        if text != "":
            font = pygame.font.SysFont("Arial", textSize)
            text = font.render(text, True, self.textColour)
            textRect = text.get_rect()
            textRect.center = s.get_rect().center
            s.blit(text, textRect)

        super().__init__(x, y, w, h, s, text, textSize, textColour, colour, z)

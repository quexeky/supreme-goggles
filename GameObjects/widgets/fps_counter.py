import pygame
import pygame.freetype

import data
from GameObjects.widgets import widget


class FPS(widget.Widget):
    def __init__(self, x, y, textSize=20, textColour="black", colour="white", z=0):
        self.x = x
        self.y = y
        self.textSize = textSize
        self.last_updated = 0
        self.font = pygame.font.SysFont("Arial", textSize)
        text = self.font.render("0", True, textColour)
        # print(textRect.center)
        # s.blit(text, textRect)
        super().__init__(x, y, 0, 0, text, 1, "0")

    def update(self, dt, events):
        self.last_updated += dt
        if self.last_updated >= 0.1:
            self.img = self.font.render(
                str(int(data.clock.get_fps())), True, self.textColour
            )
            self.last_updated = 0

    def draw(self):
        return self.img, (self.pos.x, self.pos.y)

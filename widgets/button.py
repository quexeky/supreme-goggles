import pygame

from widgets import widget


class Button(widget.Widget):
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, self.w, self.h))
        if self.text != "":
            font = pygame.font.SysFont('Arial', self.textSize)
            text = font.render(self.text, True, self.textColour)
            screen.blit(text, self.centre())



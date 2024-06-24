import pygame
import pygame.freetype

import data
from GameObjects.widgets import widget


# A good example of a UI element. Updating every so often, and it shows useful data.
class FPS(widget.Widget):
    def __init__(self, x, y, textSize=20, textColour="black", colour="white", z=0):
        self.x = x
        self.y = y
        self.textSize = textSize
        self.last_updated = 0

        # Pre-render the font so that we don't have to do it every single time
        self.font = pygame.font.SysFont("Arial", textSize)
        text = self.font.render("0", True, textColour)

        super().__init__(x, y, 0, 0, text, 1, "0")

    def update(self, dt, events):
        # Only update every 0.1 seconds
        self.last_updated += dt
        if self.last_updated >= 0.1:
            self.img = self.font.render(
                # Pygame clock has a get_fps() function which comes in useful here
                str(int(data.clock.get_fps())),
                True,
                self.textColour,
            )
            self.last_updated = 0

    def draw(self):
        return self.img, (self.pos.x, self.pos.y)

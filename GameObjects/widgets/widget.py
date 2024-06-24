from GameObjects.gameObject import GameObject


class Widget(GameObject):
    def __init__(
        self,
        x,
        y,
        w,
        h,
        img,
        scale,
        text="",
        textSize=20,
        textColour="black",
        colour="white",
        enabled=True,
        z=0,
    ):
        super().__init__(x, y, img, scale, enabled, z)
        self.w = w
        self.h = h
        self.text = text
        self.textSize = textSize
        self.textColour = textColour
        self.colour = colour


"""
    def draw(self):
        if self.enabled:
            return self.img, (self.pos.x, self.pos.y)
"""

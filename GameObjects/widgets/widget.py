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
    ):
        super().__init__(x, y, img, scale)
        self.w = w
        self.h = h
        self.text = text
        self.textSize = textSize
        self.textColour = textColour
        self.colour = colour

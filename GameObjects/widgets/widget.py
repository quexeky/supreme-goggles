from GameObjects.gameObject import GameObject


# Basic Widget class. Any "Thing" is called a widget for a reason. This class does nothing without inheriting from it
# except create a new GameObject. It doesn't even render anything
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

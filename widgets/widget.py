class Widget(object):
    def __init__(self, x, y, w, h, text="", textSize=20, textColour="black", colour="white"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.textSize = textSize
        self.textColour = textColour
        self.colour = colour

    def draw(self, screen):
        return self

    def centre(self):
        return self.x + self.w / 2, self.y + self.h / 2

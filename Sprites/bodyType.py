from Sprites.bodySprite import BodySprite


class BodyType:
    def __init__(self, styles, styleIndex=0, animation=(0, -1, False)):
        self.style = None                       # The active BodySprite
        self.styles = styles                    # The array of Styles
        self.styleIndex = styleIndex            # The ID of the style currently in use
        self.animation = animation              # The Animation ID

        self.changeStyle(0)

    def changeStyle(self, num):
        self.styleIndex += num                  #
        return self.setStyle(self.styleIndex)

    def setStyle(self, index):
        self.styleIndex = index
        self.styleIndex %= len(self.styles)
        self.style = self.styles[self.styleIndex]
        self.changeAnim(self.animation)
        return self.style

    def changeAnim(self, key):
        if key != (0, 0, False) and key != (0, 0, True):
            self.style.changeAnim(key)
            self.animation = key
        else:
            key = (self.animation[0], self.animation[1], False)
            if key == (0, 0, False) or key == (0, 0, True):
                key = (0, -1, False)
            self.style.changeAnim(key)
            self.animation = key

        return self.style.styles.index

    def update(self, speed):
        self.style.update(speed)


def createStyleArr(names, height, width):
    arr = []
    for name in names:
        arr.append(BodySprite(name))
    return arr

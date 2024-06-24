from Sprites.bodySprite import BodySprite


class BodyType:
    def __init__(self, styles, styleIndex=0, animation=(0, -1, False)):
        self.style = None
        self.styles = styles
        self.styleIndex = styleIndex
        self.animation = animation

        self.changeStyle(0)

    def changeStyle(self, num):
        self.styleIndex += num
        return self.setStyle(self.styleIndex)

    def setStyle(self, index):
        self.styleIndex = index
        self.styleIndex %= len(self.styles)
        self.style = self.styles[self.styleIndex]
        self.changeAnim(self.animation)
        return self.style

    def changeAnim(self, key):
        if key != (0, 0, False) and key != (0, 0, True):
            self.style.activeAnim = self.style.animations[key]
            self.animation = key
        else:
            key = (self.animation[0], self.animation[1], False)
            if key == (0, 0, False) or key == (0, 0, True):
                key = (0, -1, False)
            self.style.activeAnim = self.style.animations[key]
            self.animation = key

        return self.style.activeAnim


def createBodyTypeArr(names, height, width):
    arr = []
    for name in names:
        arr.append(BodySprite(name))
    return arr

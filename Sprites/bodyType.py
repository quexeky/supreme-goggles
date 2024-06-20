class BodyType:
    def __init__(self, styles, styleIndex=0, animation="N"):
        self.style = None
        self.styles = styles
        self.styleIndex = styleIndex
        self.animation = animation

        self.selectStyle(0)

    def selectStyle(self, num):
        self.styleIndex += num
        self.styleIndex %= len(self.styles)
        self.style = self.styles[self.styleIndex]
        self.changeAnim(self.animation)
        return self.style

    def changeAnim(self, key):
        self.style.activeAnim = self.style.animations[key]
        self.animation = key
        return self.style.activeAnim

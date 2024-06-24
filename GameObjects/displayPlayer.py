import data
from GameObjects import gameObject
from Sprites.sprites import SpriteCharacter


class DisplayPlayer(gameObject.GameObject):
    def __init__(self, uid, direction, styleIndexes):
        self.styleIndexes = styleIndexes
        self.sprite = SpriteCharacter(3, direction)
        super().__init__(
            0,
            0,
            self.sprite.img,
            1,
            20,
        )

        self.uid = uid

    def update(self, dt, events):
        other = data.others.get(str(self.uid))
        self.pos.x = other.x
        self.pos.y = other.y
        self.updateBody(other)
        if other.direction != self.sprite.direction:
            self.sprite.changeFullAnimation(other.direction)
        self.sprite.tick(dt)
        self.img = self.sprite.img
        # print(self.sprite.direction)

    def updateBody(self, other):
        otherStyleIndexes = other.styleIndexes
        if otherStyleIndexes[0] != self.styleIndexes[0]:
            self.sprite.moving_sprites.remove(self.sprite.Head.style)
            self.sprite.moving_sprites.add(
                self.sprite.Head.setStyle(otherStyleIndexes[0])
            )
            self.styleIndexes = otherStyleIndexes
            print("Changed Head")
        if otherStyleIndexes[1] != self.styleIndexes[1]:
            self.sprite.replace_animation(self.sprite.Torso, otherStyleIndexes[1])
            self.styleIndexes = otherStyleIndexes
            print("Changed Torso")
        if otherStyleIndexes[2] != self.styleIndexes[2]:
            self.sprite.replace_animation(self.sprite.Legs, otherStyleIndexes[2])
            self.styleIndexes = otherStyleIndexes
            print("Changed Legs")

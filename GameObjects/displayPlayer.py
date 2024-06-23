import data
import settings
from GameObjects import gameObject
from Sprites.sprites import SpriteCharacter


class DisplayPlayer(gameObject.GameObject):
    def __init__(self, uid, direction):
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
        for sprite in (self.sprite.Head, self.sprite.Torso, self.sprite.Legs):
            if sprite.styleIndex !=
        if other.direction != self.sprite.direction:
            self.sprite.changeFullAnimation(other.direction)
        self.sprite.tick(dt)
        self.img = self.sprite.img
        # print(self.sprite.direction)

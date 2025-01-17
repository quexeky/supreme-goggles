import data
from GameObjects import gameObject
from Sprites.sprites import CharacterSprite


# A player class with only rendering code. Made explicitly for networking, although it could theoretically be
# extended to be a generic NPC class in future
class DisplayPlayer(gameObject.GameObject):
    def __init__(self, uid, direction):
        self.styleIndexes = (0, 0, 0)
        self.sprite = CharacterSprite(3, direction)  # The entire player assembly
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
            self.sprite.direction = other.direction
        self.sprite.spriteUpdate(dt)

        self.img = self.sprite.img

    def updateBody(self, other):
        otherStyleIndexes = other.styleIndexes
        if otherStyleIndexes[0] != self.styleIndexes[0]:
            self.sprite.moving_sprites.remove(self.sprite.Head.style)
            self.sprite.moving_sprites.add(
                self.sprite.Head.setStyle(otherStyleIndexes[0])
            )
            self.styleIndexes = otherStyleIndexes
        if otherStyleIndexes[1] != self.styleIndexes[1]:
            self.sprite.moving_sprites.remove(self.sprite.Torso.style)
            self.sprite.moving_sprites.add(
                self.sprite.Torso.setStyle(otherStyleIndexes[1])
            )
            self.styleIndexes = otherStyleIndexes
        if otherStyleIndexes[2] != self.styleIndexes[2]:
            self.sprite.moving_sprites.remove(self.sprite.Legs.style)
            self.sprite.moving_sprites.add(
                self.sprite.Legs.setStyle(otherStyleIndexes[2])
            )
            self.styleIndexes = otherStyleIndexes

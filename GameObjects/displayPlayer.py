import data
import settings
from GameObjects import gameObject


class DisplayPlayer(gameObject.GameObject):
    def __init__(self, uid):

        super().__init__(0, 0, settings.playerImage(settings.playerDimensions[0], settings.playerDimensions[1]), 1, 20)

        self.uid = uid

    def update(self, dt):
        other = data.others.get(self.uid)
        self.pos.x = other.x
        self.pos.y = other.y


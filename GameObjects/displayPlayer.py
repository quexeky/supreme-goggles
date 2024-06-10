import settings
from GameObjects import gameObject


class DisplayPlayer(gameObject.GameObject):
    def __init__(self, x, y, w, h, scale):
        super().__init__(x, y, settings.playerImage(w, h), scale)


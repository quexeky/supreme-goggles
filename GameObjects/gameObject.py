import pygame

from data import camera_position


# The base GameObject class. Nothing here would exist without it. Take from it what you will.
# The "Scale" feature has not been added, although space has been left for it in case of future development.
# It's just too inefficient to do in the most obvious manner of just "scale it and pray" because to account for
# everything, because you'd have to call it every frame, thus removing the benefits of optimising for static images.
class GameObject(object):
    def __init__(self, x, y, img, scale, enabled=True, z=0):
        self.pos = pygame.math.Vector2(x, y)
        self.img = img
        self.scale = scale
        self.enabled = enabled
        self.z = z

    def update(self, dt, events):
        return

    # Draw function by default draws objects in absolute space (removing the camera transform from the position).
    # Most objects in the actual game are also drawn in absolute space, so this is useful. If you want to change it,
    # it's as simple as removing the "-camera_position.*" in the return statement
    def draw(self):
        if self.enabled:
            # Return is structured like this for the app.py main loop
            return self.img, (
                self.pos.x - camera_position.x,
                self.pos.y - camera_position.y,
            )

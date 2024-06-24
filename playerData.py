from datetime import datetime

import data


def calculate_age():
    now = datetime.now()
    seconds_since_midnight = (
        now - now.replace(hour=0, minute=0, second=0, microsecond=0)
    ).microseconds
    return seconds_since_midnight


# The data class for passing raw bytes through the proxy server. Made custom instead of JSON because JSON was far too
# Inefficient (used up at least twice as much bandwidth)
class PlayerData(object):
    def __init__(self, user_id, x, y, direction, styleIndexes, age=0):
        self.user_id = user_id
        self.x = x
        self.y = y
        self.direction = direction
        self.styleIndexes = styleIndexes
        self.age = age

    def update_pos(self, pos, direction, styleIndexes):
        if not (self.x == int(pos.x) and self.y == int(pos.y)):
            self.x = int(pos.x)
            self.y = int(pos.y)
            data.player_pos_updated = True
        if not (self.styleIndexes == styleIndexes):
            self.styleIndexes = styleIndexes
            data.player_pos_updated = True
        if not (self.direction == direction):
            self.direction = direction
            data.player_pos_updated = True
            print(self.direction)

    # Custom byte structure. UID is added by the server, so it shouldn't be added here
    def serialise(self):
        x = int(self.x).to_bytes(8, byteorder="little", signed=True)
        y = int(self.y).to_bytes(8, byteorder="little", signed=True)
        directionX = int(self.direction[0]).to_bytes(1, byteorder="little", signed=True)
        directionY = int(self.direction[1]).to_bytes(1, byteorder="little", signed=True)
        walking = bool(self.direction[2]).to_bytes(1, byteorder="little", signed=True)
        head = int(self.styleIndexes[0]).to_bytes(1, byteorder="little", signed=True)
        torso = int(self.styleIndexes[1]).to_bytes(1, byteorder="little", signed=True)
        legs = int(self.styleIndexes[2]).to_bytes(1, byteorder="little", signed=True)

        # Calculate the age of the data so to remove a major part of the delay
        age = int(calculate_age()).to_bytes(3, byteorder="little", signed=True)

        # print(len(uid + x + y))

        return x + y + directionX + directionY + walking + head + torso + legs + age


# Removed from the class itself because python wouldn't let me call class functions without initialising a class
def deserialise_player_data(serialised):
    # print(len(serialised))
    uid = int.from_bytes((serialised[0],), byteorder="little", signed=False)
    x = int.from_bytes(serialised[1:8], byteorder="little", signed=True)
    y = int.from_bytes(serialised[9:16], byteorder="little", signed=True)
    directionX = int.from_bytes((serialised[17],), byteorder="little", signed=True)
    directionY = int.from_bytes((serialised[18],), byteorder="little", signed=True)
    walking = bool.from_bytes((serialised[19],), byteorder="little", signed=True)
    head = int.from_bytes((serialised[20],), byteorder="little", signed=True)
    torso = int.from_bytes((serialised[21],), byteorder="little", signed=True)
    legs = int.from_bytes((serialised[22],), byteorder="little", signed=True)
    age = int.from_bytes((serialised[23:26]), byteorder="little", signed=False)

    return PlayerData(
        uid, x, y, (directionX, directionY, walking), (head, torso, legs), age
    )

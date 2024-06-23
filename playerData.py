import data


class PlayerData(object):
    def __init__(self, user_id, x, y, direction, styleIndexes):
        self.user_id = user_id
        self.x = x
        self.y = y
        self.direction = direction
        self.styleIndexes = styleIndexes

    def update_pos(self, pos, direction, styleIndexes):
        if not (self.x == int(pos.x) and self.y == int(pos.y)):
            self.x = int(pos.x)
            self.y = int(pos.y)
            self.direction = direction
            data.player_pos_updated = True
        if not (self.styleIndexes == styleIndexes):
            self.styleIndexes = styleIndexes
            data.player_pos_updated = True

    def serialise(self):
        # uid = int(self.user_id).to_bytes(1, byteorder="little", signed=False)
        x = int(self.x).to_bytes(8, byteorder="little", signed=True)
        y = int(self.y).to_bytes(8, byteorder="little", signed=True)
        directionX = int(self.direction[0]).to_bytes(1, byteorder="little", signed=True)
        directionY = int(self.direction[1]).to_bytes(1, byteorder="little", signed=True)
        walking = bool(self.direction[2]).to_bytes(1, byteorder="little", signed=True)
        head = int(self.styleIndexes[0]).to_bytes(1, byteorder="little", signed=True)
        torso = int(self.styleIndexes[1]).to_bytes(1, byteorder="little", signed=True)
        legs = int(self.styleIndexes[2]).to_bytes(1, byteorder="little", signed=True)

        # print(len(uid + x + y))

        return x + y + directionX + directionY + walking + head + torso + legs


def deserialise_player_data(serialised):
    print(len(serialised))
    uid = int.from_bytes((serialised[0],), byteorder="little", signed=False)
    x = int.from_bytes(serialised[1:8], byteorder="little", signed=True)
    y = int.from_bytes(serialised[9:16], byteorder="little", signed=True)
    directionX = int.from_bytes((serialised[17],), byteorder="little", signed=True)
    directionY = int.from_bytes((serialised[18],), byteorder="little", signed=True)
    walking = bool.from_bytes((serialised[19],), byteorder="little", signed=True)
    head = int.from_bytes((serialised[20],), byteorder="little", signed=True)
    torso = int.from_bytes((serialised[21],), byteorder="little", signed=True)
    legs = int.from_bytes((serialised[22],), byteorder="little", signed=True)

    return PlayerData(uid, x, y, (directionX, directionY, walking), (head, torso, legs))

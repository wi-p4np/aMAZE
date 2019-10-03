import arcade


class MapObject(arcade.Sprite):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale)

        self.left = x
        self.bottom = y
        self.properties = properties

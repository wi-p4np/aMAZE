from game.items.map_object import MapObject


class Star(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        print("I've found a star")
        super().on_hit()
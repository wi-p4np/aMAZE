import arcade
from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager


class DestroyableWall(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.health = 3

    def on_hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.remove_from_sprite_lists()
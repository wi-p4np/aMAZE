import arcade
from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager

MAX_TIMER = 0.5


class DestroyableWall(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.health = 3
        self.timer = 0

    def on_hit(self):
        if self.timer == 0:
            self.timer = MAX_TIMER
            if self.health > 0:
                self.health -= 1
            else:
                self.remove_from_sprite_lists()

    def update(self, delta_time):
        self.timer = max(self.timer - delta_time, 0)

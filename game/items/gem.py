from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from math import sin
from game.managers.sounds_manager import SoundsManager

class Gem(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.timer = 0

    def on_hit(self):
        ScoreManager.gem_score += 1
        super().on_hit()
        SoundsManager.play('gems')

    def update(self, delta_time):
        self.timer += delta_time
        self.center_y = self.center_y + sin(self.timer * 5) * 0.150

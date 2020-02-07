from game.managers.score_manager import ScoreManager
from game.items.map_object import MapObject


class Score(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        ScoreManager.score +=1
        super().on_hit()
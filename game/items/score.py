from game.managers.score_manager import ScoreManager
from game.items.map_object import MapObject
from game.managers.sounds_manager import SoundsManager


class Score(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        ScoreManager.score +=1
        SoundsManager.play_sound('coins')
        super().on_hit()

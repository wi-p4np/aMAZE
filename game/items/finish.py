from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from game.managers.sounds_manager import SoundsManager


class Finish(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        ScoreManager.gameIsActive = False
        SoundsManager.play_sound("win")
        print("I've finished the level")
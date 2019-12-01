from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from game.gui.pause_window import PauseWindow


class Finish(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        ScoreManager.gameIsActive = False
        pause_window = PauseWindow()
        pause_window.setup()
        print("I've finished the level")
from game.items.map_object import MapObject
from game.managers.sounds_manager import SoundsManager


class Enemy(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

        self.speed = 1.0

    def update(self, delta_time):
        pass

    def on_hit(self):
        self.kill()
        SoundsManager.play_sound("losing")

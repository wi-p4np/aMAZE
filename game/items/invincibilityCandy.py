from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from game.consts import MAX_INVINCIBILITY_TIMER
from game.managers.sounds_manager import SoundsManager


class InvincibilityCandy(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        ScoreManager.invincibility_timer = MAX_INVINCIBILITY_TIMER
        ScoreManager.is_invincible = True
        SoundsManager.play_sound("invincible")
        super().on_hit()


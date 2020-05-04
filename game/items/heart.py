from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from game.managers.score_manager import MAX_HEALTH
from game.managers.sounds_manager import SoundsManager


class Heart(MapObject):
	def __init__(self, asset_path, scale, x, y, properties):
		super().__init__(asset_path, scale, x, y, properties)

	def on_hit(self):
		if ScoreManager.health < MAX_HEALTH:
			ScoreManager.health += 1
			SoundsManager.play_sound("hearts")
		super().on_hit()


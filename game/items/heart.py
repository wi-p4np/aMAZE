from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from game.managers.score_manager import MAX_HEALTH


class Heart(MapObject):
	def __init__(self, asset_path, scale, x, y, properties):
		super().__init__(asset_path, scale, x, y, properties)

	def on_hit(self):
		if ScoreManager.health < MAX_HEALTH:
			ScoreManager.health += 1
		super().on_hit()
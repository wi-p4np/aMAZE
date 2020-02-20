from game.gui.components.score import ScoreLabel
from game.managers.score_manager import ScoreManager



class CoinsLabel(ScoreLabel):
	def __init__(self, icon_type, center_x, center_y):
		super().__init__(icon_type, center_x, center_y)


	def update(self):
		self.set_text(ScoreManager.score)





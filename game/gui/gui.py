from game.gui.components.health_bar import HealthBar
from game.gui.components.score import ScoreLabel
from game.managers.score_manager import ScoreManager
from game.gui.components.coins_label import CoinsLabel
from game.gui.components.score import Score


class MyGui:
    def __init__(self):
        self.health_bar = HealthBar()
        self.gem_score = ScoreLabel('gem', 50, 600)
        self.coins_score = ScoreLabel('coin', 150, 600)
        self.score_label = CoinsLabel('coin2', 250, 600)

    def draw(self):
        self.coins_score.set_text(ScoreManager.score)
        self.health_bar.draw()
        self.gem_score.draw()
        self.coins_score.draw()
        self.score_label.draw()

    def update(self):
        self.score_label.update()
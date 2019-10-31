from game.gui.components.health_bar import HealthBar
from game.gui.components.score import ScoreLabel
from game.managers.score_manager import ScoreManager


class MyGui:
    def __init__(self):
        self.health_bar = HealthBar()
        self.gem_score = ScoreLabel('gem',50,600)
        self.coins_score = ScoreLabel('coin',150,600)

    def draw(self):
        self.coins_score.set_text(ScoreManager.score)
        self.health_bar.draw()
        self.gem_score.draw()
        self.coins_score.draw()


    def update():
        pass

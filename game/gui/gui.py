from game.gui.components.health_bar import HealthBar
from game.gui.components.score import ScoreLabel
from game.managers.score_manager import ScoreManager
from game.gui.components.invincibilityCandy_bar import InvincibilityCandyBar
from game.gui.components.coins_label import CoinsLabel
from game.gui.components.score import Score
from game.gui.pause_window import PauseWindow
from game.gui.pause_window import ShowPauseButton
from game.gui.themes import gui_theme



class MyGui:
    def __init__(self):
        self.health_bar = HealthBar()
        self.gem_score = ScoreLabel('gem', 50, 600)
        self.coins_score = ScoreLabel('coin', 150, 600)
        self.invincibility_candy_bar = InvincibilityCandyBar()
        self.score_label = CoinsLabel('coin', 150, 600)
        self.pause_view = PauseWindow()

        self.show_pause_button = ShowPauseButton(self.pause_view, 555, 25, theme=gui_theme)
        self.pause_view.active = False

    def draw(self):
        self.health_bar.draw()
        self.gem_score.draw()
        self.show_pause_button.draw()
        self.coins_score.draw()
        self.invincibility_candy_bar.draw()
        self.pause_view.draw()
        self.score_label.draw()
        
    def update(self, delta_time):
        self.invincibility_candy_bar.update(delta_time)
        self.pause_view.on_update(delta_time)
        self.score_label.update()
        self.health_bar.update()

    def on_mouse_press(self, x, y, button, modifiers):
        self.pause_view.on_mouse_press(x, y, button, modifiers)
        self.show_pause_button.check_mouse_press(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.pause_view.on_mouse_release(x, y, button, modifiers)
        self.show_pause_button.check_mouse_release(x, y)

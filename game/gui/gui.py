from game.gui.components.gems_label import GemsLabel
from game.gui.components.health_bar import HealthBar
from game.gui.components.score_label import ScoreLabel
from game.managers.score_manager import ScoreManager
from game.gui.components.invincibilityCandy_bar import InvincibilityCandyBar
from game.gui.components.coins_label import CoinsLabel
from game.gui.components.gems_label import GemsLabel
#from game.gui.components.score_label import Score
from game.gui.pause_window import PauseWindow
from game.gui.pause_window import ShowPauseButton
from game.gui.themes import gui_theme
from game.gui.panel import GUIPanel



class MyGui:
    def __init__(self):
        self.health_bar = HealthBar()
        self.invincibility_candy_bar = InvincibilityCandyBar()
        self.pause_view = PauseWindow()

        self.show_pause_button = ShowPauseButton(self.pause_view, 555, 25, theme=gui_theme)
        self.pause_view.active = False
        self.top_panel = GUIPanel()
        self.top_panel.add_component(GemsLabel('gem', 50, 50))
        self.top_panel.add_component(CoinsLabel('coin', 150, 50))

    def draw(self):
        self.health_bar.draw()
        self.top_panel.draw()
        self.show_pause_button.draw()
        self.invincibility_candy_bar.draw()
        self.pause_view.draw()
        
    def update(self, delta_time):
        self.invincibility_candy_bar.update(delta_time)
        self.top_panel.update()
        self.pause_view.on_update(delta_time)
        self.health_bar.update()

    def on_mouse_press(self, x, y, button, modifiers):
        self.pause_view.on_mouse_press(x, y, button, modifiers)
        self.show_pause_button.check_mouse_press(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.pause_view.on_mouse_release(x, y, button, modifiers)
        self.show_pause_button.check_mouse_release(x, y)

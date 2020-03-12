from game.gui.components.invincibilityCandy_bar import InvincibilityCandyBar
from game.gui.components.coins_label import CoinsLabel
from game.gui.components.gems_label import GemsLabel
from game.gui.panel import GUIPanel
from game.gui.components.health_bar import HealthBar
from game.gui.components.pause_button import PauseButton
from game.gui.components.pause_button import PausePanel
from game.gui.components.resume_button import ResumeButton
from game.gui.components.quit_button import QuitButton
from game.managers.score_manager import ScoreManager


class MyGui:
    def __init__(self):
        self.invincibility_candy_bar = InvincibilityCandyBar()
        self.pause_view = PausePanel()
        self.pause_view.visible = False
        self.top_panel = GUIPanel()
        self.top_panel.add_component(GemsLabel('gem', 50, 50))
        self.top_panel.add_component(CoinsLabel('coin', 150, 50))
        self.top_panel.add_component(HealthBar(850, 50))
        self.top_panel.add_component(PauseButton(self.pause_view, 910, 600))
        self.pause_view.add_component(ResumeButton(self.pause_view, 350, 200))
        self.pause_view.add_component(QuitButton(self.pause_view, 700, 200))

    def draw(self):
        self.top_panel.draw()
        self.invincibility_candy_bar.draw()
        self.pause_view.draw()

    def update(self, delta_time):
        self.invincibility_candy_bar.update(delta_time)
        self.top_panel.update()
        self.pause_view.update()
        self.on_update(delta_time)

    def on_update(self, delta_time):
        if ScoreManager.pauseWindowIsActive:
            ScoreManager.gameIsActive = False
        else:
            ScoreManager.gameIsActive = True

    def on_mouse_press(self, x, y, button, modifiers):
        self.pause_view.on_mouse_press(x, y, button, modifiers)
        self.top_panel.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.pause_view.on_mouse_release(x, y, button, modifiers)
        self.top_panel.on_mouse_release(x, y, button, modifiers)

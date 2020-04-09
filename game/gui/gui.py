from game.gui.components.invincibilityCandy_bar import InvincibilityCandyBar
from game.gui.components.coins_label import CoinsLabel
from game.gui.components.gems_label import GemsLabel
from game.gui.panel import GUIPanel
from game.gui.components.health_bar import HealthBar
from game.gui.components.pause_button import PauseButton
from game.gui.components.pause_button import PausePanel
from game.gui.components.you_died_panel import YouDiedPanel
from game.gui.components.resume_button import ResumeButton
from game.gui.components.quit_button import QuitButton
from game.managers.score_manager import ScoreManager
from game.gui.components.pause_background import PauseBackground
from game.consts import SCREEN_WIDTH

class MyGui:
    def __init__(self):
        self.invincibility_candy_bar = InvincibilityCandyBar()
        self.pause_view = PausePanel()
        self.you_died_panel = YouDiedPanel()
        self.top_panel = GUIPanel()
        self.top_panel.add_component(GemsLabel('gem', 50, 50))
        self.top_panel.add_component(CoinsLabel('coin', 150, 50))
        self.top_panel.add_component(HealthBar(850, 50))
        self.pause_view.add_component(PauseBackground())
        self.top_panel.add_component(PauseButton(self.pause_view, 910, 600))
        self.pause_view.add_component(ResumeButton(self.pause_view, SCREEN_WIDTH/2, 250))
        self.pause_view.add_component(QuitButton(SCREEN_WIDTH/2, 320))
        self.you_died_panel.add_component(PauseBackground())
        self.you_died_panel.add_component(QuitButton(SCREEN_WIDTH/2, 340))


    def draw(self):
        self.top_panel.draw()
        self.invincibility_candy_bar.draw()
        self.pause_view.draw()
        self.you_died_panel.draw()


    def update(self, delta_time):
        self.invincibility_candy_bar.update(delta_time)
        self.top_panel.update()
        self.pause_view.update()
        self.you_died_panel.update()
        self.on_update(delta_time)

    def on_update(self, delta_time):
        if ScoreManager.pauseWindowIsActive:
            ScoreManager.gameIsActive = False
        else:
            ScoreManager.gameIsActive = True
        if ScoreManager.health <= 0:
           ScoreManager.gameIsActive = False


    def on_mouse_press(self, x, y, button, modifiers):
        self.pause_view.on_mouse_press(x, y, button, modifiers)
        self.you_died_panel.on_mouse_press(x, y, button, modifiers)
        self.top_panel.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.pause_view.on_mouse_release(x, y, button, modifiers)
        self.top_panel.on_mouse_release(x, y, button, modifiers)
        self.you_died_panel.on_mouse_release(x, y, button, modifiers)

import arcade
from game.managers.score_manager import ScoreManager
from game.gui.panel import GUIPanel


class YouDiedPanel(GUIPanel):
    def __init__(self):
        super().__init__()

        self.visible = False
        self.components = []
        self.text = 'YOU DIED!'
        self.x = 0
        self.y = 0
        self.text_settings = {'x': 350, 'y': 300, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 50}

    def update(self):
        if ScoreManager.death_window_is_active:
            self.visible = True
            for component in self.components:
                component.update()

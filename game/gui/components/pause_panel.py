import arcade
from game.gui.panel import GUIPanel


class PausePanel(GUIPanel):
    def __init__(self):
        super().__init__()

        self.visible = False
        self.components = []
        self.text = 'OPTIONS'
        self.x = 0
        self.y = 0
        self.text_settings = {'x': 410, 'y': 130, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 35}

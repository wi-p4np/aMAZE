import arcade
from game.gui.panel import GUIPanel


class LevelsPanel(GUIPanel):
    def __init__(self):
        super().__init__()

        self.visible = False
        self.components = []
        self.text = 'SELECT LEVEL'
        self.x = 0
        self.y = 0
        self.text_settings = {'x': 350, 'y': 130, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 35}



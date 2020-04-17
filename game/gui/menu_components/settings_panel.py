import arcade
from game.gui.panel import GUIPanel


class SettingsPanel(GUIPanel):
    def __init__(self):
        super().__init__()
        
        self.visible = False
        self.components = []
        self.text = 'SETTINGS'
        self.text_settings = {'x': 370, 'y': 130, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 35}
        self.x = 0
        self.y = 0


import arcade
from game.gui.panel import GUIPanel
from os import listdir
from game.consts import SCREEN_WIDTH
from game.gui.menu_components.selection_button import SelectionButton

LEVELS_MENU = 'maps/'


class LevelsPanel(GUIPanel):
    def __init__(self):
        super().__init__()

        self.visible = False
        self.components = []
        self.text = 'SELECT LEVEL'
        self.x = 0
        self.y = 0
        self.text_settings = {'x': 350, 'y': 130, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 35}
        self.level_list = [f for f in listdir(LEVELS_MENU) if f.endswith(".tmx")]

    def add_levels_buttons(self):
        center_x = SCREEN_WIDTH/2
        center_y = 200
        for f in self.level_list:
            center_y += 50
            text = f.split('.')[0]
            self.add_component(SelectionButton(self, center_x, center_y, text))



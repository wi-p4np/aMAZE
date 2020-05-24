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
        self.level_list = sorted([f for f in listdir(LEVELS_MENU) if f.endswith(".tmx")])
        self.size = 3
        self.offset = 0
        self.visible_buttons = []

    def add_levels_buttons(self):
        center_x = SCREEN_WIDTH/2
        center_y = 200
        self.visible_buttons = []
        for f in self.level_list[self.offset:self.offset+self.size]:
            center_y += 50
            text = f.split('.')[0]
            button = SelectionButton(self, center_x, center_y, text)
            self.visible_buttons.append(button)

    def update(self):
        if self.visible:
            self.components += self.visible_buttons
            for component in self.components:
                component.update()

    def draw(self):
        if self.visible:
            viewport_left, viewport_right, viewport_bottom, viewport_top = arcade.get_viewport()
            for component in self.components:
                component.center_x = viewport_left + self.x + component.initial_x
                component.center_y = viewport_top + self.y - component.initial_y
                component.draw()
            if self.text:
                arcade.draw_text(self.text, viewport_left + self.text_settings['x'],
                                 viewport_top - self.text_settings['y'], self.text_settings['color'],
                                 self.text_settings['font_size'])


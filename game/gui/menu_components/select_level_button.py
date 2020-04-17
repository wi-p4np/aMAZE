import arcade
from game.gui.components.button import Button

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class SelectLevelButton(Button):
    def __init__(self, levels_window, parent_window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.levels_window = levels_window
        self.parent_window = parent_window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'LEVELS'
        self.text_settings = {'x': 40, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        if not self.levels_window.visible:
            self.pressed = True
            self.parent_window.visible = False
            self.levels_window.visible = True


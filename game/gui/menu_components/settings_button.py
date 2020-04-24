import arcade
from game.gui.components.button import Button


BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class SettingsButton(Button):
    def __init__(self, window, parent_window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.window = window
        self.parent_window = parent_window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'SETTINGS'
        self.text_settings = {'x': 60, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        if not self.window.visible:
            self.pressed = True
            self.parent_window.visible = False
            self.window.visible = True

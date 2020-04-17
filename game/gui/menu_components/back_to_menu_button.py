import arcade
from game.gui.components.button import Button

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class BackToMenu(Button):
    def __init__(self, window, previous_window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.window = window
        self.previous_window = previous_window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'BACK'
        self.text_settings = {'x': 35, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        if self.window.visible:
            self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.window.visible = False
            self.previous_window.visible = True

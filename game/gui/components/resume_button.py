import arcade
from game.gui.components.button import Button

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 1


class ResumeButton(Button):
    def __init__(self, window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.window = window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'RESUME'
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False
        self.text_settings = {'x': 50, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}

    def on_press(self):
        if self.window.visible:
            self.pressed = True
            self.window.visible = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.window.visible = False

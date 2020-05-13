import arcade
from game.gui.components.button import Button
from game.managers.score_manager import ScoreManager


BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class PauseButton(Button):
    def __init__(self, window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.window = window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'PAUSE'
        self.text_settings = {'x': 40, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        if not self.window.visible:
            self.pressed = True
            ScoreManager.pause_window_is_active = True
            self.window.visible = True



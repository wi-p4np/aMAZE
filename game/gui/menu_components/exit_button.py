import arcade
from game.gui.components.button import Button
from game.managers.score_manager import ScoreManager


BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class ExitButton(Button):
    def __init__(self, parent_window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.parent_window = parent_window
        self.text = 'EXIT'
        self.text_settings = {'x': 30, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        self.pressed = True
        self.parent_window.visible = False
        ScoreManager.gameIsActive = False
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        print('game closed')


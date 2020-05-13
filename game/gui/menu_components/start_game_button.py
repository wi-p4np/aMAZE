import arcade
from game.gui.components.button import Button
from game.managers.scene_manager import SceneManager
from game.managers.score_manager import ScoreManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.8


class StartButton(Button):
    def __init__(self, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'START'
        self.text_settings = {'x': 35, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        self.pressed = True
        ScoreManager.pause_window_is_active = False
        ScoreManager.score = 0
        ScoreManager.gem_score = 0
        ScoreManager.health = 3
        SceneManager.change_scene('game')

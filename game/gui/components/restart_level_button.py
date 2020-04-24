import arcade
from game.gui.components.button import Button
from game.managers.scene_manager import SceneManager
from game.managers.score_manager import ScoreManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 1
MAX_HEALTH = 3


class RestartButton(Button):
    def __init__(self, window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.window = window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'RESTART LEVEL'
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False
        self.text_settings = {'x': 85, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 18}

    def on_press(self):
        if self.window.visible:
            self.pressed = True
            self.window.visible = True
            ScoreManager.score = 0
            ScoreManager.gem_score = 0
            ScoreManager.health = 3

    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.window.visible = False
            ScoreManager.pauseWindowIsActive = False
            SceneManager.restart(SceneManager.game)

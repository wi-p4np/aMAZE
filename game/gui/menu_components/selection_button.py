import arcade
from game.gui.components.button import Button
from game.managers.scene_manager import SceneManager
from game.managers.score_manager import ScoreManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class SelectionButton(Button):
    def __init__(self, window, center_x, center_y, text):
        super().__init__(center_x, center_y)

        self.window = window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = text
        self.map = "./maps/" + text + '.tmx'
        self.text_settings = {'x': 50, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 15}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        self.pressed = True
        SceneManager.map = self.map
        #SceneManager.change_scene('game')
        #SceneManager.restart(SceneManager.game)

    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.window.visible = False
            ScoreManager.pause_window_is_active = False
            SceneManager.restart(SceneManager.game)
import arcade
from game.gui.components.button import Button
from game.managers.score_manager import ScoreManager

BUTTON_SPRITE = '/home/elena/aMAZE/assets/sprites/UI/grey_button01.png'
SCALING = 0.80

class PauseButton(Button):
    def __init__(self, pause_window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.pause_window = pause_window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'SHOW'
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        print("LOL")
        print(self.pause_window)
        if not self.pause_window.active:
            print("PLEEASSEEEE")
            self.pressed = True
            ScoreManager.pauseWindowIsActive = True
            self.pause_window.active = True

    def on_release(self):
        if self.pressed:
            self.pressed = False

    def draw(self):
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()

        arcade.draw_text(self.text,
                         self.icon.center_x - 30, self.icon.center_y - 4, arcade.csscolor.BLACK, 20)
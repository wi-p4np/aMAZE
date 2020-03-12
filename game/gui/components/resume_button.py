import arcade
from game.gui.components.button import Button
from game.managers.score_manager import ScoreManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 1


class ResumeButton(Button):
    def __init__(self, pause_window, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.pause_window = pause_window
        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'RESUME'
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.check_mouse_press(x, y):
            self.on_press()

    def on_mouse_release(self, x, y, button, modifiers):
        if self.pressed:
            self.on_release()

    def on_press(self):
        if self.pause_window.visible:
            self.pressed = True
            #ScoreManager.pauseWindowIsActive = True
            self.pause_window.visible = True


    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.pause_window.visible = False
            arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
            ScoreManager.pauseWindowIsActive = False

    def draw(self):
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()

        arcade.draw_text(self.text,
                         self.icon.center_x - 40, self.icon.center_y - 6, arcade.csscolor.BLACK, 20)
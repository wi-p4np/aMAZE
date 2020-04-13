import arcade
from game.gui.components.button import Button
from game.managers.scene_manager import SceneManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.8


class StartButton(Button):
    def __init__(self, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'START'
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
        self.pressed = True
        SceneManager.change_scene('game')

    def on_release(self):
        if self.pressed:
            self.pressed = False

    def draw(self):
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()

        arcade.draw_text(self.text,
                         self.icon.center_x - 35, self.icon.center_y - 6, arcade.csscolor.BLACK, 20)
import arcade
from game.gui.components.button import Button
from game.managers.scene_manager import SceneManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 1


class MenuButton(Button):
    def __init__(self, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'MENU'
        self.text_settings = {'x': 35, 'y': 6, 'color': arcade.csscolor.BLACK, 'font_size': 20}
        self.window = None
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def on_press(self):
        self.pressed = True

    def update(self):
        if self.pressed:
            SceneManager.change_scene('menu')

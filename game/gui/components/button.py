import arcade
from game.gui.components.component import GUIComponent

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class Button(GUIComponent):
    def __init__(self, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = None
        self.text_settings = {'x': 0, 'y': 0, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 0}
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False

    def set_text(self, text):
        self.text = str(text)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.check_mouse_press(x, y):
            self.on_press()

    def on_mouse_release(self, x, y, button, modifiers):
        if self.pressed:
            self.on_release()

    def on_press(self):
        pass

    def on_release(self):
        if self.pressed:
            self.pressed = False

    def check_mouse_press(self, x, y):
        if x > self.center_x + self.icon.width / 2:
            return False
        if x < self.center_x - self.icon.width / 2:
            return False
        if y > self.center_y + self.icon.height / 2:
            return False
        if y < self.center_y - self.icon.height / 2:
            return False
        return True

    def draw(self):
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()

        arcade.draw_text(self.text,
                         self.icon.center_x - self.text_settings['x'], self.icon.center_y - self.text_settings['y'],
                         self.text_settings['color'], self.text_settings['font_size'])

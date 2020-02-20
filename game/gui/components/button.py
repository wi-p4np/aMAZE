import arcade
from game.gui.components.component import GUIComponent

BUTTON_SPRITE = '/home/elena/aMAZE/assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class Button(GUIComponent):
    def __init__(self, center_x, center_y,):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
        self.text = 'SHOW'
        self.center_x = center_x
        self.center_y = center_y

    def set_text(self, text):
        self.text = str(text)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.check_mouse_press(x, y):
            self.on_press()

    def on_mouse_release(self, x, y, button, modifiers):
        if self.pressed:
            self.on_release()

    def check_mouse_press(self, x, y):

        print("lol checking")
        print(self.center_x, self.center_y, self.icon.width, self.icon.height, x, y)

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
        pass
        #self.icon.center_x = self.center_x
        #self.icon.center_y = self.center_y
        #self.icon.draw()

        #arcade.draw_text(self.text,
                         #self.icon.center_x - 30, self.icon.center_y - 4, arcade.csscolor.BLACK, 20)
import arcade


class DialogueBox:
    def __init__(self, x, y, width, height, color=None, texture=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.active = False
        self.button_list = []
        self.text_list = []
        self.texture = texture

    def on_draw(self):
        if self.active:
            if self.texture:
                arcade.draw_texture_rectangle(self.x, self.y, self.width, self.height, self.texture)
            else:
                arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
            for button in self.button_list:
                button.draw()
            for text in self.text_list:
                text.draw()

    def on_mouse_press(self, x, y, _button, _modifiers):
        for button in self.button_list:
            button.check_mouse_press(x, y)

    def on_mouse_release(self, x, y, _button, _modifiers):
        for button in self.button_list:
            button.check_mouse_release(x, y)

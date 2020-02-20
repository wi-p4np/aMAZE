class GUIComponent:
    def __init__(self, center_x, center_y):
        self.initial_x = center_x
        self.initial_y = center_y

    def draw(self):
        pass

    def update(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass
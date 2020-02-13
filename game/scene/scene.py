
class Scene:

    def __init__(self, game):
        self.game = game

    def setup(self):
        pass

    def draw(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def update(self, delta_time):
        pass

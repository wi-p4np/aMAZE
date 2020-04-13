import arcade
from game.gui.menu_gui import MenuGui
from game.scene.scene import Scene
from game.managers.scene_manager import SceneManager


class GameMenu(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.gui = None

    def setup(self):
        self.gui = MenuGui()

    def draw(self):
        self.gui.draw()

    def update(self, delta_time):
        self.gui.update(delta_time)

    def on_mouse_press(self, x, y, button, modifiers):
        self.gui.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.gui.on_mouse_release(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        pass



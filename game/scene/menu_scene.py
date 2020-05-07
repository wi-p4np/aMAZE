import arcade

from game.managers.sounds_manager import SoundsManager
from game.scene.scene import Scene


class GameMenu(Scene):

    def __init__(self, game):
        super().__init__(game)

    def setup(self):
        SoundsManager.load_settings()

    def draw(self):
        pass

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.game.change_scene('game')


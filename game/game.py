import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SCALE, PLAYER_SCALE
from game.gui.gui import MyGui
from game.managers.score_manager import ScoreManager
from game.scene.game_scene import GameScene
from game.scene.menu_scene import GameMenu


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.current = None
        self.scenes = {
            "game": GameScene(self),
            "menu": GameMenu(self)
        }

        self.current = self.scenes['menu']

    def setup(self):
        self.current.setup()

    def on_mouse_press(self, x, y, button, modifiers):
        self.current.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.current.on_mouse_release(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        self.current.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.current.on_key_release(key, modifiers)

    def change_scene(self, scene_name):
        self.current = self.scenes[scene_name]
        self.current.setup()

    def on_draw(self):
        arcade.start_render()
        self.current.draw()

    def update(self, delta_time):
        self.current.update(delta_time)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

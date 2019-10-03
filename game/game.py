"""
Platformer Game
"""
import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SCALE
from game.map.map import Map
from game.player.player import Player


class MyGame(arcade.Window):
    """
    """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.map = None
        self.player = None
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player = Player("assets/sprites/enemies/bee.png", TILE_SCALE, 128, 128)

        self.map = Map.load("./maps/template.tmx")
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.map.walls_layer, 0)

    def on_draw(self):
        arcade.start_render()
        self.map.walls_layer.draw()
        self.map.objects_layer.draw()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)

    def update(self, delta_time):
        self.physics_engine.update()
        self.player.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

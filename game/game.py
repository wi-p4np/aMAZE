"""
Platformer Game
"""
import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SCALE
from game.map.map import Map
from game.player.player import Player
from game.gui.gui import MyGui


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
        self.gui = MyGui()

    def on_draw(self):
        arcade.start_render()
        self.map.draw()
        self.player.draw()
        self.gui.draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)

    def update(self, delta_time):
        self.physics_engine.update()
        self.player.update()
        self.gui.update(delta_time)

        hit_list = arcade.check_for_collision_with_list(self.player, self.map.objects_layer)
        for hit in hit_list:
            hit.on_hit()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SCALE
from game.map.map import Map
from game.player.player import Player
from game.enemies.enemies import Enemy


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.map = None
        self.player = None
        self.physics_engine = None
        self.enemy_list = arcade.SpriteList()

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player = Player("assets/sprites/enemies/bee.png", TILE_SCALE, 128, 128)
        enemy = Enemy("assets/sprites/enemies/fishBlue.png", TILE_SCALE, 280, 280, None)
        self.enemy_list.append(enemy)

        self.map = Map.load("./maps/template.tmx")
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.map.walls_layer, 0)

    def on_draw(self):
        arcade.start_render()
        self.map.draw()
        self.player.draw()
        self.enemy_list.draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)

    def update(self, delta_time):
        self.physics_engine.update()
        self.player.update()
        self.enemy_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        if len(hit_list) > 0:
            self.player.center_x = 128
            self.player.center_y = 128

            for enemy in hit_list:
                enemy.on_hit()
            
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
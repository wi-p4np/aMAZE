import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SCALE
from game.gui.gui import MyGui
from game.managers.score_manager import ScoreManager
from game.map.map import Map
from game.physics import PhysicsEngineSimple
from game.player.player import Player


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.map = None
        self.player = None
        self.animated_player = None
        self.animated_player_list = None
        self.physics_engine = None
        self.objects_physics_engine = None
        self.gui = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player = Player("assets/sprites/enemies/bee.png", TILE_SCALE, 128, 128)
        self.map = Map.load("./maps/template.tmx")
        self.physics_engine = PhysicsEngineSimple(self.player, self.map.walls_layer)
        self.objects_physics_engine = PhysicsEngineSimple(self.player, self.map.collidable_objects_layer)
        self.gui = MyGui()


        #self.animated_player.animations


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
        if not ScoreManager.gameIsActive:
            return

        self.player.update()
        self.gui.update(delta_time)
        self.map.update(delta_time)

        # handle collision with walls
        hit_list = self.physics_engine.update()
        for hit in hit_list:
            pass

        destroyable_hit_list = self.objects_physics_engine.update()
        for hit in destroyable_hit_list:
            hit.on_hit()

        enemy_hit_list = arcade.check_for_collision_with_list(self.player, self.map.enemies_layer)
        if len(enemy_hit_list) > 0:
            self.player.on_hit()
            for enemy in enemy_hit_list:
                enemy.on_hit()

        hit_list = arcade.check_for_collision_with_list(self.player, self.map.objects_layer)
        for hit in hit_list:
            hit.on_hit()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

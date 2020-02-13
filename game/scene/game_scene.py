import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SCALE, PLAYER_SCALE
from game.gui.gui import MyGui
from game.managers.score_manager import ScoreManager
from game.map.map import Map
from game.physics import PhysicsEngineSimple
from game.player.player import Player
from game.enemies.enemies import FollowingEnemy
from game.camera.camera import Camera
from game.scene.scene import Scene


class GameScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.map = None
        self.player = None
        self.animated_player = None
        self.animated_player_list = None
        self.player_physics_engine = None
        self.gui = None
        self.following_enemy = None
        self.following_enemy_physics_engine = None
        self.players_list = None
        self.camera = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.players_list = arcade.SpriteList()
        self.player = Player(PLAYER_SCALE, 98, 128)
        self.players_list.append(self.player)
        self.map = Map.load("./maps/second_map.tmx")
        self.player_physics_engine = PhysicsEngineSimple(self.player)
        self.following_enemy = FollowingEnemy("assets/sprites/enemies/fly.png", TILE_SCALE, 400, 400, None)
        self.following_enemy_physics_engine = PhysicsEngineSimple(self.following_enemy)
        self.gui = MyGui()
        self.camera = Camera(self.player)

    def draw(self):
        self.map.draw()
        self.player.draw()
        self.gui.draw()
        self.following_enemy.draw()

    def update(self, delta_time):
        self.gui.update(delta_time)

        if not ScoreManager.gameIsActive:
            return

        self.player.update()
        self.player_physics_engine.update()
        self.map.update(delta_time)
        self.following_enemy.update(delta_time)
        self.following_enemy_physics_engine.update()
        self.camera.update(delta_time)

        # handle collision with walls
        self.player_physics_engine.check(self.map.walls_layer)

        destroyable_hit_list = self.player_physics_engine.check(self.map.collidable_objects_layer)
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

        players_list = arcade.check_for_collision_with_list(self.following_enemy, self.players_list)
        if len(players_list) > 0:
            for player in players_list:
                player.on_hit()

        self.player_physics_engine.resolve()

    def on_mouse_press(self, x, y, button, modifiers):
        self.gui.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.gui.on_mouse_release(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)


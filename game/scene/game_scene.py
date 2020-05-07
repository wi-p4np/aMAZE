import arcade

from game.consts import TILE_SCALE, PLAYER_SCALE
from game.gui.gui import MyGui
from game.managers.score_manager import ScoreManager
from game.map.map import Map
from game.physics import PhysicsEngineSimple
from game.player.player import Player
from game.enemies.following_enemy import FollowingEnemy
from game.enemies.bullet_controller import BulletController
from game.enemies.shooting_enemy import ShootingEnemy
from game.camera.camera import Camera
from game.scene.scene import Scene
from game.managers.sounds_manager import SoundsManager


class GameScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.map = None
        self.animated_player = None
        self.animated_player_list = None
        self.player_physics_engine = None
        self.player = None
        self.gui = None
        self.following_enemy = None
        self.players_list = None
        self.camera = None
        self.shooting_enemy = None
        self.players_list = None
        self.bullet_controller = None
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.bullet_controller = BulletController(self)
        self.map = Map.load(self, "./maps/template.tmx")
        self.players_list = arcade.SpriteList()
        self.players_list.append(self.player)
        self.player_physics_engine = PhysicsEngineSimple(self.player)
        self.following_enemy = FollowingEnemy(self, "assets/sprites/enemies/fly.png", TILE_SCALE, 400, 400, None)
        self.shooting_enemy = ShootingEnemy(self, "assets/sprites/enemies/frog_move.png",
                                            TILE_SCALE, -100, 00, None, self.bullet_controller)
        self.gui = MyGui()
        self.camera = Camera(self.player)

        SoundsManager.register_sound("coins", "./assets/sounds/coins.wav"),
        SoundsManager.register_sound("hearts", "./assets/sounds/hearts.wav"),
        SoundsManager.register_sound("gems", "./assets/sounds/gems.wav"),
        SoundsManager.register_sound("stars", "./assets/sounds/stars.wav")
        SoundsManager.register_sound("losing", "./assets/sounds/losing_sound.wav"),
        SoundsManager.register_sound("shooting", "./assets/sounds/shooting_enemy.wav"),
        SoundsManager.register_sound("win", "./assets/sounds/finish_level.wav"),
        SoundsManager.register_sound("invincible", "./assets/sounds/invincibility.wav"),
        SoundsManager.register_sound("door", "./assets/sounds/door_key.wav"),
        SoundsManager.register_sound("destroy", "./assets/sounds/destroy_wall.wav")

    def draw(self):
        self.map.draw()
        self.player.draw()
        self.following_enemy.draw()
        self.bullet_controller.draw()
        self.shooting_enemy.draw()
        self.gui.draw()

    def update(self, delta_time):

        self.gui.update(delta_time)

        self.player.update()
        self.player_physics_engine.update()
        self.map.update(delta_time)
        self.following_enemy.update(delta_time)
        self.camera.update(delta_time)
        self.bullet_controller.update(delta_time)
        self.shooting_enemy.update(delta_time)

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
                SoundsManager.play('losing')

        self.player_physics_engine.resolve()


    def on_mouse_press(self, x, y, button, modifiers):
        self.gui.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.gui.on_mouse_release(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)


import arcade
import math

from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager

ENEMY_MOVEMENT_SPEED = 5
MIN_DISTANCE = 250


class Enemy(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

        self.speed = 1.0

    def update(self, delta_time):
        pass

    def on_hit(self):
        self.kill()


class FollowingEnemy(Enemy):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def update (self, delta_time):
        _x = ScoreManager.playerX - self.center_x
        _y = ScoreManager.playerY - self.center_y

        d = math.sqrt(_x**2 + _y**2)
        if d <= MIN_DISTANCE:
            self.change_x = _x * self.speed / d
            self.change_y = _y * self.speed / d
        else:
            self.change_x = 0
            self.change_y = 0

import math
from game.managers.score_manager import ScoreManager
from game.enemies.enemies import Enemy
from game.consts import SHORT_DISTANCE_MIN
from game.physics import PhysicsEngineSimple


class FollowingEnemy(Enemy):
    def __init__(self, map, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.physics_engine = PhysicsEngineSimple(self)
        self.map = map

    def update(self, delta_time):
        _x = ScoreManager.playerX - self.center_x
        _y = ScoreManager.playerY - self.center_y

        d = math.sqrt(_x**2 + _y**2)
        if d <= SHORT_DISTANCE_MIN:
            self.change_x = _x * self.speed / d
            self.change_y = _y * self.speed / d
        else:
            self.change_x = 0
            self.change_y = 0

        self.physics_engine.check(self.map.walls_layer)

        self.physics_engine.resolve()
        self.physics_engine.update()

import math
from game.enemies.following_enemy import FollowingEnemy
from game.managers.score_manager import ScoreManager
from game.consts import SHORT_DISTANCE_MIN
from game.consts import SHOOTING_DISTANCE_MIN
from game.consts import SHOOTING_DISTANCE_MAX
from game.physics import PhysicsEngineSimple


class ShootingEnemy(FollowingEnemy):
    def __init__(self, map, asset_path, scale, x, y, properties, bullet_controller):
        super().__init__(map, asset_path, scale, x, y, properties)

        self.shooting_timer = 0
        self.bullet_controller = bullet_controller
        self.map = map

    def update(self, delta_time):
        _x = ScoreManager.playerX - self.center_x
        _y = ScoreManager.playerY - self.center_y
        d = math.sqrt(_x ** 2 + _y ** 2)

        self.shooting_timer -= delta_time
        self.change_x = 0
        self.change_y = 0

        if d <= SHORT_DISTANCE_MIN:
            if d <= SHOOTING_DISTANCE_MAX:
                if self.shooting_timer <= 0:
                    self.bullet_controller.shoot_bullet(self.center_x, self.center_y, _x / d, _y / d, 3)
                    self.shooting_timer = 2

            if d <= SHOOTING_DISTANCE_MIN:
                self.change_x = _x * self.speed / d
                self.change_y = _y * self.speed / d

        self.physics_engine.check(self.map.walls_layer)

        self.physics_engine.resolve()
        self.physics_engine.update()

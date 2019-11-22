import arcade

from game.managers.score_manager import ScoreManager

PLAYER_MOVEMENT_SPEED = 5


class Player(arcade.Sprite):
    def __init__(self, asset_path, scale, x, y):
        super().__init__(asset_path, scale)

        self.center_x = x
        self.center_y = y

    def on_key_press(self, key):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = -PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = 0

    def on_hit(self):
        if not ScoreManager.isInvincible:
            self.center_x = 128
            self.center_y = 128
            ScoreManager.health -= 1;

    def update(self):
        pass

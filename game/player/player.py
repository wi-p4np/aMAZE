import arcade

from game.managers.score_manager import ScoreManager

PLAYER_MOVEMENT_SPEED = 5


class Player(arcade.AnimatedTimeSprite):
    def __init__(self, asset_path, scale, x, y):
        super().__init__(asset_path, scale)

        self.center_x = x
        self.center_y = y

        self.animations = {
            "right": [
                arcade.load_texture("assets/sprites/other/player_17.png"),
                arcade.load_texture("assets/sprites/other/player_18.png"),
                arcade.load_texture("assets/sprites/other/player_19.png")
            ],
            "left": [
                arcade.load_texture("assets/sprites/other/player_20.png"),
                arcade.load_texture("assets/sprites/other/player_21.png"),
                arcade.load_texture("assets/sprites/other/player_22.png")
            ],
            "up": [
                arcade.load_texture("assets/sprites/other/player_08.png"),
                arcade.load_texture("assets/sprites/other/player_09.png"),
                arcade.load_texture("assets/sprites/other/player_10.png")
            ],
            "down": [
                arcade.load_texture("assets/sprites/other/player_05.png"),
                arcade.load_texture("assets/sprites/other/player_06.png"),
                arcade.load_texture("assets/sprites/other/player_07.png")
            ],
            "idle_right": [
                arcade.load_texture("assets/sprites/other/player_17.png"),
            ],
            "idle_left": [
                arcade.load_texture("assets/sprites/other/player_20.png"),
            ],
            "idle_up": [
                arcade.load_texture("assets/sprites/other/player_08.png"),
            ],
            "idle_down": [
                arcade.load_texture("assets/sprites/other/player_05.png"),
            ]
        }
        self.play_animation("idle_down")

    def play_animation(self, animation_name):
        self.textures = self.animations[animation_name]

    def on_key_press(self, key):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -PLAYER_MOVEMENT_SPEED
            self.play_animation("left")
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = PLAYER_MOVEMENT_SPEED
            self.play_animation("right")
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_y = PLAYER_MOVEMENT_SPEED
            self.play_animation("up")
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = -PLAYER_MOVEMENT_SPEED
            self.play_animation("down")

    def on_key_release(self, key):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
            self.play_animation("idle_left")
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0
            self.play_animation("idle_right")
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_y = 0
            self.play_animation("idle_up")
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = 0
            self.play_animation("idle_down")

    def on_hit(self):
        if not ScoreManager.isInvincible:
            self.center_x = 128
            self.center_y = 128
            ScoreManager.health -= 1

    def update(self):
        self.update_animation()

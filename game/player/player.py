import arcade

from game.managers.score_manager import ScoreManager

PLAYER_MOVEMENT_SPEED = 5


class Player(arcade.AnimatedTimeSprite):
    def __init__(self, scale, x, y):
        super().__init__("assets/sprites/other/player_05.png", scale)

        self.center_x = x
        self.center_y = y

        self.animations = {
            "right": [
                arcade.load_texture("assets/sprites/other/player_17.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_18.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_19.png", scale=scale)
            ],
            "left": [
                arcade.load_texture("assets/sprites/other/player_20.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_21.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_22.png", scale=scale)
            ],
            "up": [
                arcade.load_texture("assets/sprites/other/player_08.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_09.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_10.png", scale=scale)
            ],
            "down": [
                arcade.load_texture("assets/sprites/other/player_05.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_06.png", scale=scale),
                arcade.load_texture("assets/sprites/other/player_07.png", scale=scale)
            ],
            "idle_right": [
                arcade.load_texture("assets/sprites/other/player_17.png", scale=scale),
            ],
            "idle_left": [
                arcade.load_texture("assets/sprites/other/player_20.png", scale=scale),
            ],
            "idle_up": [
                arcade.load_texture("assets/sprites/other/player_08.png", scale=scale),
            ],
            "idle_down": [
                arcade.load_texture("assets/sprites/other/player_05.png", scale=scale),
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
        ScoreManager.playerX = self.center_x
        ScoreManager.playerY = self.center_y

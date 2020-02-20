import arcade

from game.consts import SCREEN_WIDTH, SCREEN_HEIGHT


class Camera():
    def __init__(self, player):
        self.player = player
        self.left = self.player.center_x - SCREEN_WIDTH / 2
        self.bottom = self.player.center_y - SCREEN_HEIGHT / 2

    def update(self, delta_time):
        target_left = self.player.center_x - SCREEN_WIDTH / 2
        target_bottom = self.player.center_y - SCREEN_HEIGHT / 2

        self.left = arcade.lerp(self.left, target_left, delta_time*2)

        self.bottom = arcade.lerp(self.bottom, target_bottom, delta_time*2)

        arcade.set_viewport(self.left,
                            SCREEN_WIDTH + self.left,
                            self.bottom,
                            SCREEN_HEIGHT + self.bottom)

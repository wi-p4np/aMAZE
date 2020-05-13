import arcade
from game.managers.score_manager import ScoreManager


SPRITE = 'assets/sprites/items/lollipopGreen.png'
CANDY_SCALING = 1.0


class InvincibilityCandyBar():
    def __init__(self):

        self.candy_sprite = arcade.Sprite(SPRITE, CANDY_SCALING)
        self.candy_sprite.center_x = 600
        self.candy_sprite.center_y = 600

    def update(self, deltaTime):
        if ScoreManager.invincibility_timer > 0:
            ScoreManager.invincibility_timer = ScoreManager.invincibility_timer - deltaTime
            if ScoreManager.invincibility_timer <= 0:
                ScoreManager.is_invincible = False

    def draw(self):
        if ScoreManager.is_invincible:
            self.candy_sprite.draw()

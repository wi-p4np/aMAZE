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
        if ScoreManager.invincibilityTimer > 0:
            ScoreManager.invincibilityTimer = ScoreManager.invincibilityTimer - deltaTime
            if ScoreManager.invincibilityTimer <= 0:
                ScoreManager.isInvincible = False

    def draw(self):
        if ScoreManager.isInvincible:
            self.candy_sprite.draw()

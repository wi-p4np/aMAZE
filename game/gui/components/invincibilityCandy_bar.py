import arcade
from game.items.invincibilityCandy import InvincibilityCandy


SPRITE = 'assets/sprites/other/lollipopGreen.png'
CANDY_SCALING = 1.0


class InvincibilityCandyBar():
    def __init__(self):

        self.candy_sprite = arcade.Sprite(SPRITE, CANDY_SCALING)
        self.candy_sprite.center_x = 600
        self.candy_sprite.center_y = 600

        self.update_candy()

    def update_candy(self, deltaTime):
        if InvincibilityCandy.invincibilityTimer > 0:
            InvincibilityCandy.invincibilityTimer = InvincibilityCandy.invincibilityTimer - deltaTime
            if InvincibilityCandy.invincibilityTimer <= 0:
                InvincibilityCandy.isInvincible = False

    def draw(self):
        self.candy_list.draw()
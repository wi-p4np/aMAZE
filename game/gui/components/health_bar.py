import arcade

from game.gui.components.component import GUIComponent
from game.managers.score_manager import ScoreManager
from game.managers.score_manager import MAX_HEALTH


HEARTS_SCALING = 1.0

SPRITES = {
    'full': 'assets/sprites/items/full_heart.png',
    'half': 'assets/sprites/items/half_heart.png',
    'empty': 'assets/sprites/items/empty_heart.png',
}

TEXTURE_FULL = 0
TEXTURE_HALF = 1
TEXTURE_EMPTY = 2


class HealthBar(GUIComponent):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y)

        textures = [
            arcade.load_texture(SPRITES['half']),
            arcade.load_texture(SPRITES['empty'])
        ]

        self.hearts_list = arcade.SpriteList()

        for x in range(MAX_HEALTH):
            heart = arcade.Sprite(SPRITES['full'], HEARTS_SCALING)
            for texture in textures:
                heart.append_texture(texture)
            self.hearts_list.append(heart)
        self.update()

    def draw(self):
        for x in range(MAX_HEALTH):
            heart = self.hearts_list.sprite_list[x]
            heart.center_x = x * 50 + self.center_x
            heart.center_y = self.center_y

        self.hearts_list.draw()

    def update(self):
        for x in range(MAX_HEALTH):
            sprite = self.hearts_list.sprite_list[x]

            if x + 1 <= ScoreManager.health:
                sprite.set_texture(TEXTURE_FULL)
            else:
                sprite.set_texture(TEXTURE_EMPTY)

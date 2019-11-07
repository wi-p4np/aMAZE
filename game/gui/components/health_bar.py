import arcade


MAX_HEALTH = 3
HEARTS_SCALING = 1.0

SPRITES = {
    'full': 'assets/sprites/items/full_heart.png',
    'half': 'assets/sprites/items/half_heart.png',
    'empty': 'assets/sprites/items/empty_heart.png',
}

TEXTURE_FULL = 0
TEXTURE_HALF = 1
TEXTURE_EMPTY = 2


class HealthBar():
    def __init__(self):

        textures = [
            arcade.load_texture(SPRITES['half'], scale=HEARTS_SCALING),
            arcade.load_texture(SPRITES['empty'], scale=HEARTS_SCALING)
        ]

        self.hearts_list = arcade.SpriteList()
        self.health = 2

        for x in range(MAX_HEALTH):
            heart = arcade.Sprite(SPRITES['full'], HEARTS_SCALING)
            for texture in textures:
                heart.append_texture(texture)
            heart.center_x = x * 50 + 850
            heart.center_y = 600
            self.hearts_list.append(heart)

        self.update_hearts()

    def update_hearts(self):
        for x in range(MAX_HEALTH):
            sprite = self.hearts_list.sprite_list[x]

            if x + 1 <= self.health:
                sprite.set_texture(TEXTURE_FULL)
            else:
                sprite.set_texture(TEXTURE_EMPTY)

    def draw(self):

        # self.hearts_list.sprite_list[0]
        #object.__dict__ - returns an object in form of a dict

        self.hearts_list.draw()

    def update(self):
        pass

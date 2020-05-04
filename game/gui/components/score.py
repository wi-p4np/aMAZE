import arcade
from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager
from game.managers.sounds_manager import SoundsManager

SPRITES = {
    'gem': 'assets/sprites/items/gemBlue.png',
    'coin': 'assets/sprites/items/coinGold.png',
    'coin2': 'assets/sprites/items/gold_1.png',
    'coin3': 'assets/sprites/items/coinBronze.png'
}

SCORE_SCALING = 0.40

# I want to create a super class for my gemscore and my coin score
# class Score():
    # def __init__(self):


class Score(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        ScoreManager.score +=1
        SoundsManager.play_sound("coins")
        super().on_hit()


class ScoreLabel(Score):
    def __init__(self, icon_type, center_x, center_y):
        #super().__init__(asset_path, scale, x, y, properties)

        self.icon_sprite_list = arcade.SpriteList()
        self.icon = arcade.Sprite(SPRITES[icon_type], SCORE_SCALING)
        self.icon.center_x = center_x
        self.icon.center_y = center_y
        self.icon_sprite_list.append(self.icon)
        self.icon_score = 0
        self.set_text(self.icon_score)

    def set_text(self, text):
        self.text = str(text)

    def draw(self):
        self.icon_sprite_list.draw()
        arcade.draw_text(self.text,
            self.icon.center_x + 20, self.icon.center_y - 5, arcade.csscolor.WHITE, 15)
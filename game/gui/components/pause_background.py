from game.gui.components.component import GUIComponent
from game.consts import SCREEN_WIDTH
from game.consts import SCREEN_HEIGHT
import arcade

PAUSE_BACKGROUND = 'assets/sprites/UI/black_square.png'


class PauseBackground(GUIComponent):
    def __init__(self, center_x=SCREEN_WIDTH/2, center_y=SCREEN_HEIGHT/2):
        super().__init__(center_x, center_y)

        self.icon = arcade.Sprite(PAUSE_BACKGROUND)
        self.icon.height = SCREEN_HEIGHT
        self.icon.width = SCREEN_WIDTH
        self.icon.alpha = 400
        self.icon.center_y = center_y
        self.icon.center_x = center_x

    def draw(self):
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()
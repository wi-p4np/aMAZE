import arcade
from game.items.map_object import MapObject
from game.managers.score_manager import ScoreManager

MAX_TIMER = 0.5


class DestroyableWall(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.health = 3
        self.timer = 0
        #self.color = None

    def on_hit(self):
        if self.timer == 0:
            self.timer = MAX_TIMER
            if self.health > 0:
                self.health -= 1
            else:
                self.remove_from_sprite_lists()
        self.update_colour()


    def update_colour(self):
        if self.health == 2:
            self.color: RGB = (20, 50, 50) #dark orange
        elif self.health == 1:
            self.color: RGB = (50, 200, 200) #yellow green



    def update(self, delta_time):
        self.timer = max(self.timer - delta_time, 0)
        #self.update_colour()

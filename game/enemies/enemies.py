import arcade

from game.items.map_object import MapObject

ENEMY_MOVEMENT_SPEED = 5


class Enemy(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)   

    def update(self):
        pass

    def on_hit(self):
        self.kill()

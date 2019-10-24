from game.items.map_object import MapObject


class Gem(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)

    def on_hit(self):
        print("I've found a gem")
        super().on_hit()







"""


class Animal:
    def __init__(self, size, health, name):
        self.size = size
        self.health = health
        self.name = name



class SmallLion(Animal):
    def __init__(self, name):
        super().__init___("small", 10, name)

lion = Lion("Sylwia")
"""
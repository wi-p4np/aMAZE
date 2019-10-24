import arcade

from game.consts import TILE_SCALE
from game.map.parser.parser import MapParser
from game.items.map_object import MapObject
from game.items.gem import Gem


class Map:
    def __init__(self):
        self.walls_layer = arcade.SpriteList()
        self.objects_layer = arcade.SpriteList()

    def draw(self):
        self.walls_layer.draw()
        self.objects_layer.draw()

    @staticmethod
    def load(file_path):
        config = MapParser.read(file_path)

        _map = Map()
        for row in config.layers['Walls'].tiles:
            for tile in row:
                if not tile:
                    continue

                sprite = arcade.Sprite(tile.image, TILE_SCALE)
                sprite.left = tile.x * TILE_SCALE
                sprite.bottom = tile.y * TILE_SCALE

                _map.walls_layer.append(sprite)

        for tile in config.object_layers['Items'].objects:
            if tile.type == "Gem":
                gem = Gem(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y, tile.properties)
                _map.objects_layer.append(gem)
            else:
                sprite = MapObject(tile.image, TILE_SCALE,
                    tile.x * TILE_SCALE, tile.y * TILE_SCALE,
                    tile.properties)

                _map.objects_layer.append(sprite)
        return _map

"""
class Dog:
    def __init__(self):
        print("hał hał")

dog1 = Dog()


class NamedDog(Dog):
    def __init__(self, name):
        super().__init__()
        self.name = name

dog2 = NamedDog("Burek")
"""



import arcade

from game.consts import TILE_SCALE
from game.map.parser.parser import MapParser
from game.items.map_object import MapObject
from game.items.gem import Gem
from game.items.star import Star
from game.items.heart import Heart


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
            elif tile.type == "Star":
                star = Star(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y, tile.properties)
                _map.objects_layer.append(star)
            elif tile.type == "Heart":
                heart = Heart(tile.image, 1.0, tile.x * TILE_SCALE, tile.y, tile.properties)
                _map.objects_layer.append(heart)
            else:
                sprite = MapObject(tile.image, TILE_SCALE,
                    tile.x * TILE_SCALE, tile.y * TILE_SCALE,
                    tile.properties)

                _map.objects_layer.append(sprite)
        return _map



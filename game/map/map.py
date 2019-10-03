import arcade

from game.consts import TILE_SCALE
from game.map.parser.parser import MapParser


class Map:
    def __init__(self):
        self.walls_layer = arcade.SpriteList()
        self.objects_layer = arcade.SpriteList()

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
            sprite = arcade.Sprite(tile.image, TILE_SCALE)
            sprite.left = tile.x * TILE_SCALE
            sprite.bottom = tile.y * TILE_SCALE

            _map.objects_layer.append(sprite)
        return _map

import arcade

from game.consts import TILE_SCALE
from game.map.parser.parser import MapParser
from game.map.map_object import MapObject
from game.enemies.enemies import Enemy


class Map:
    def __init__(self):
        self.walls_layer = arcade.SpriteList()
        self.objects_layer = arcade.SpriteList()
        self.enemies_layer = arcade.SpriteList()

    def draw(self):
        self.walls_layer.draw()
        self.objects_layer.draw()
        self.enemies_layer.draw()

    def update(self):
        self.objects_layer.update()
        self.enemies_layer.update()


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
            if tile.type == "Enemy":
                enemy = Enemy(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y, tile.properties)
                _map.enemies_layer.append(enemy)
            else:
                sprite = MapObject(tile.image, TILE_SCALE,
                    tile.x * TILE_SCALE, tile.y * TILE_SCALE,
                    tile.properties)
                _map.objects_layer.append(sprite)
        return _map
                
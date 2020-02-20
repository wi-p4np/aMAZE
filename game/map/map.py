import arcade

from game.consts import TILE_SCALE
from game.enemies.enemies import Enemy
from game.items.destroyable_wall import DestroyableWall
from game.items.finish import Finish
from game.items.gem import Gem
from game.items.score import Score
from game.items.heart import Heart
from game.items.invincibilityCandy import InvincibilityCandy
from game.items.map_object import MapObject
from game.items.score import Score
from game.items.star import Star
from game.items.door import Door
from game.items.door_key import DoorKey
from game.map.parser.parser import MapParser


class Map:
    def __init__(self):
        self.walls_layer = arcade.SpriteList()
        self.objects_layer = arcade.SpriteList()
        self.enemies_layer = arcade.SpriteList()
        self.collidable_objects_layer = arcade.SpriteList()

    def draw(self):
        self.walls_layer.draw()
        self.objects_layer.draw()
        self.enemies_layer.draw()
        self.collidable_objects_layer.draw()

    def update(self, delta_time):
        for _object in self.objects_layer:
            _object.update(delta_time)

        for _object in self.enemies_layer:
            _object.update(delta_time)

        for _object in self.collidable_objects_layer:
            _object.update(delta_time)

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
                enemy = Enemy(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.enemies_layer.append(enemy)

            elif tile.type == "Gem":
                gem = Gem(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(gem)

            elif tile.type == "Star":
                star = Star(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(star)

            elif tile.type == "Key":
                door_key = DoorKey(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(door_key)

            elif tile.type == "Door":
                door = Door(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.collidable_objects_layer.append(door)

            elif tile.type == "DestroyableWall":
                destroyable_wall = DestroyableWall(tile.image, 1.0, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.collidable_objects_layer.append(destroyable_wall)

            elif tile.type == "Finish":
                finish = Finish(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(finish)

            elif tile.type == "InvincibilityCandy":
                invincibility_candy = InvincibilityCandy(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(invincibility_candy)

            elif tile.type == "Coin":
                coin = Score(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(coin)

            elif tile.type == "Finish":
                finish = Finish(tile.image, TILE_SCALE, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(finish)

            elif tile.type == "Heart":
                heart = Heart(tile.image, 1.0, tile.x * TILE_SCALE, tile.y * TILE_SCALE, tile.properties)
                _map.objects_layer.append(heart)

            else:
                sprite = MapObject(tile.image, TILE_SCALE,
                    tile.x * TILE_SCALE, tile.y * TILE_SCALE,
                    tile.properties)

                _map.objects_layer.append(sprite)
        return _map

import xml.etree.ElementTree as ET

from game.map.parser.layer import Layer

from game.map.parser.map_config import MapConfig
from game.map.parser.object_layer import ObjectLayer
from game.map.parser.object_tile import ObjectTile
from game.map.parser.tile import Tile
from game.map.parser.tileset import Tileset


class MapParser:
    @staticmethod
    def read(map_path):
        xml = ET.fromstring(open(map_path).read())

        tileset = Tileset.from_xml(xml)
        layers = _read_layers(xml, tileset)
        object_layers = _read_object_layers(xml, tileset)

        config = MapConfig(layers, object_layers, tileset)
        return config


def _read_layers(xml, tileset):
    layers = {}
    for _layer in xml.findall("./layer"):
        layer = Layer(
            _layer.attrib['id'], _layer.attrib['name'],
            _layer.attrib['width'], _layer.attrib['height'])

        row = []
        data = _layer.find('data')
        for index, _tile in enumerate(data.getchildren()):
            tile = None
            x, y = index % layer.width, int(index / layer.width)

            if 'gid' in _tile.attrib:

                tile = Tile(
                    x * tileset.tilewidth, y * tileset.tileheight,
                    tileset.tilewidth, tileset.tileheight,
                    tileset.tiles[int(_tile.attrib['gid'])])

            row.append(tile)

            if x == layer.width-1:
                layer.tiles.append(row)
                row = []

        layers[layer.name] = layer
    return layers


def _read_object_layers(xml, tileset):
    layers = {}
    for _layer in xml.findall("./objectgroup"):
        layer = ObjectLayer(_layer.attrib['id'], _layer.attrib['name'],
                            _layer.attrib.get('offsetx', 0), _layer.attrib.get('offsety', 0))

        for _object in _layer.findall("object"):
            object_tile = ObjectTile(
                _object.attrib['id'],
                _object.attrib.get('name'),
                _object.attrib.get('type'),
                tileset.tiles[int(_object.attrib['gid'])-1],
                float(_object.attrib['x']) + layer.offset_x,
                float(_object.attrib['y']) + layer.offset_y,
                _object.attrib['width'],
                _object.attrib['height'],
                _object.attrib.get('visible'))

            for _property in _object.findall("properties/property"):
                object_tile.add_property(_property.attrib['name'], _property.attrib['value'])

            layer.objects.append(object_tile)
        layers[layer.name] = layer
    return layers

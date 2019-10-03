import os


class Tileset:
    def __init__(self, name, firstgid, tilewidth, tileheight, base_path="."):
        self.name = name
        self.firstgid = int(firstgid)
        self.tilewidth = int(tilewidth)
        self.tileheight = int(tileheight)
        self.base_path = base_path
        self.tiles = {}

    def add_tile(self, gid, source):
        self.tiles[gid] = os.path.join(self.base_path, source)

    @staticmethod
    def from_xml(xml):
        _tileset = xml.find("./tileset")
        tileset = Tileset(
            _tileset.attrib['name'], _tileset.attrib['firstgid'],
            _tileset.attrib['tilewidth'], _tileset.attrib['tileheight'],
            "maps")

        for tile in _tileset.findall('tile'):
            tile_image = tile.find("image")
            tileset.add_tile(int(tile.attrib['id'])+1, tile_image.attrib['source'])
        return tileset


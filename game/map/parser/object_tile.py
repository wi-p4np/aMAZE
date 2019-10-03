
class ObjectTile:
    def __init__(self, id, name, type, image, x, y, width, height, visible):
        self.id = id
        self.name = name
        self.image = image
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        self.properties = {}

    def add_property(self, key, value):
        self.properties[key] = value

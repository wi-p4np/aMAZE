

class Layer:
    def __init__(self, id, name, width, height):
        self.id = id
        self.name = name
        self.width = int(width)
        self.height = int(height)
        self.tiles = []

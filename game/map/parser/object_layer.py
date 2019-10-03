
class ObjectLayer:
    def __init__(self, id, name, offset_x, offset_y):
        self.id = id
        self.name = name
        self.offset_x = int(offset_x)
        self.offset_y = int(offset_y)
        self.objects = []

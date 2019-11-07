class ObjectLayer:
    def __init__(self, id, name, offset_x, offset_y):
        self.id = id
        self.name = name
        self.offset_x = float(offset_x)
        self.offset_y = float(offset_y)
        self.objects = []

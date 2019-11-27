import arcade
from game.items.map_object import MapObject
from game.managers.event_manager import EventManager

class DoorKey(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.door_id = properties['doorId']

    def on_hit(self):
       event_name = "ON_DOOR_{}_OPEN".format(self.door_id)
       EventManager.emit(event_name)
       self.remove_from_sprite_lists()

    def update(self, delta_time):
        pass
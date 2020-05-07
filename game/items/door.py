import arcade
from game.items.map_object import MapObject
from game.managers.event_manager import EventManager

class Door(MapObject):
    def __init__(self, asset_path, scale, x, y, properties):
        super().__init__(asset_path, scale, x, y, properties)
        self.door_id = properties['doorId']
        event_name = "ON_DOOR_{}_OPEN".format(self.door_id)
        EventManager.add_handler(event_name, self.on_open)

    def on_open(self):
       self.remove_from_sprite_lists()

    def on_hit(self):
    	pass

    def update(self, delta_time):
        pass

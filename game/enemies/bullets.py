import arcade
from game.consts import BULLET_SCALE
from game.physics import PhysicsEngineSimple


class Bullet(arcade.Sprite):
	def __init__(self, parent, asset_path, x, y, change_x, change_y, speed):
		super().__init__(asset_path, BULLET_SCALE)

		self.parent = parent
		self.center_x = x
		self.center_y = y
		self.speed = speed
		self.change_x = change_x * speed
		self.change_y = change_y * speed
		self.physics_engine = PhysicsEngineSimple(self)
		self.map = map

	def update(self):
		results = self.physics_engine.check(self.parent.game.players_list)
		if len(results) > 0:
			player = results[0]
			player.on_hit()
			self.remove_from_sprite_lists()

		check_walls = self.physics_engine.check(self.parent.game.map.walls_layer)
		if len(check_walls) > 0:
			self.remove_from_sprite_lists()

		self.physics_engine.resolve()
		self.physics_engine.update()
		return

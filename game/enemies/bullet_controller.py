import arcade
from game.enemies.bullets import Bullet


class BulletController:
	def __init__(self, game):
		self.game = game
		self.bullets = arcade.SpriteList()

	def update(self, delta_time):
		self.bullets.update()

	def draw(self):
		self.bullets.draw()

	def shoot_bullet(self, x, y, change_x, change_y, speed):
		bullet = Bullet(self, "assets/sprites/items/coinBronze.png", x, y, change_x, change_y, speed)
		self.bullets.append(bullet)
		return bullet

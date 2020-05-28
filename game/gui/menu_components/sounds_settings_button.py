import arcade
from game.gui.components.button import Button
from game.managers.sounds_manager import SoundsManager

BUTTON_SPRITE = 'assets/sprites/UI/grey_button01.png'
SCALING = 0.80


class SoundsButton(Button):
	def __init__(self, window, center_x, center_y):
		super().__init__(center_x, center_y)

		self.window = window
		self.icon = arcade.Sprite(BUTTON_SPRITE, SCALING)
		self.text = "SOUNDS:"
		self.text_settings = {'x': 70, 'y': 8, 'color': arcade.csscolor.BLACK, 'font_size': 18}
		self.center_x = center_x
		self.center_y = center_y
		self.pressed = False

	def on_press(self):
		self.pressed = True
		SoundsManager.sounds_on = True
		SoundsManager.save_settings()
		self.text = "SOUNDS: ON"



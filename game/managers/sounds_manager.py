import arcade


class SoundsManager:
	sounds = {}

	@staticmethod
	def register_sound(sound_name, asset_path):
		SoundsManager.sounds[sound_name] = arcade.Sound(asset_path)

	@staticmethod
	def play(sound_name):
		SoundsManager.sounds[sound_name].play()


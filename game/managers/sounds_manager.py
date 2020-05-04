import arcade
import json


class SoundsManager:
	sounds = {}
	music_on = False
	sounds_on = False
	music_name = None

	@staticmethod
	def register_sound(sound_name, asset_path):
		SoundsManager.sounds[sound_name] = arcade.Sound(asset_path)

	@staticmethod
	def play_sound(sound_name):
		if SoundsManager.sounds_on:
			SoundsManager.sounds[sound_name].play_sound()

	@staticmethod
	def setup_music(file_name):
		SoundsManager.music_name = arcade.Sound(file_name)

	@staticmethod
	def play_music():
		if SoundsManager.music_on:
			SoundsManager.music_name.play_music()

	@staticmethod
	def save_settings():
		settings = {'music_on': SoundsManager.music_on, 'sounds_on': SoundsManager.sounds_on}
		with open("./saves/music_settings.json", "w") as write_file:
			json.dump(settings, write_file)

	@staticmethod
	def load_settings():
		with open("./saves/music_settings.json", "r") as read_file:
			settings = json.load(read_file)

			SoundsManager.sounds_on = settings['sounds_on']
			SoundsManager.music_on = settings['music_on']

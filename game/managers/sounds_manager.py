import arcade
import json
import os

SETTINGS_PATH = "./saves/music_settings.json"


class SoundsManager:
    sounds = {}
    music_on = True
    sounds_on = True
    music = None

    @staticmethod
    def register_sound(sound_name, asset_path):
        SoundsManager.sounds[sound_name] = arcade.Sound(asset_path)

    @staticmethod
    def play_sound(sound_name):
        if SoundsManager.sounds_on:
            SoundsManager.sounds[sound_name].play()

    @staticmethod
    def setup_music(file_name):
        SoundsManager.music = arcade.Sound(file_name)

    @staticmethod
    def play_music():
        if SoundsManager.music_on:
            SoundsManager.music.play()

    @staticmethod
    def save_settings():
        settings = {
            'music_on': SoundsManager.music_on,
            'sounds_on': SoundsManager.sounds_on
        }

        with open(SETTINGS_PATH, "w") as write_file:
            json.dump(settings, write_file)

    @staticmethod
    def load_settings():
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as read_file:
                settings = json.load(read_file)

                SoundsManager.sounds_on = settings['sounds_on']
                SoundsManager.music_on = settings['music_on']
        else:
            SoundsManager.save_settings()


from game.managers.score_manager import ScoreManager
from os import listdir


LEVELS_MENU = 'maps/'


class SceneManager:
    game = None

    @staticmethod
    def setup(game):
        SceneManager.game = game
        SceneManager.map = LEVELS_MENU + sorted(listdir(LEVELS_MENU))[0]

    @staticmethod
    def restart(game):
        ScoreManager.score = 0
        ScoreManager.gem_score = 0
        ScoreManager.health = 3
        SceneManager.game.change_scene('game')

    @staticmethod
    def change_scene(scene_name):
        SceneManager.game.change_scene(scene_name)

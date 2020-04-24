
class SceneManager:
    game = None

    @staticmethod
    def setup(game):
        SceneManager.game = game

    @staticmethod
    def restart(game):
        SceneManager.game.change_scene('game')
        SceneManager.game = game.Mygame()


    @staticmethod
    def change_scene(scene_name):
        SceneManager.game.change_scene(scene_name)

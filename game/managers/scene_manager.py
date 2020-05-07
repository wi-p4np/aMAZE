class SceneManager:
    game = None

    @staticmethod
    def setup(game):
        SceneManager.game = game

    @staticmethod
    def change_scene(scene_name):
        SceneManager.game.change_scene(scene_name)

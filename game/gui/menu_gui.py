from game.gui.menu_components.menu_panel import MenuPanel
from game.gui.menu_components.select_level_button import SelectLevelButton
from game.gui.menu_components.settings_button import SettingsButton
from game.gui.menu_components.levels_panel import LevelsPanel
from game.gui.menu_components.settings_panel import SettingsPanel
from game.gui.menu_components.start_game_button import StartButton
from game.gui.menu_components.exit_button import ExitButton
from game.gui.menu_components.back_to_menu_button import BackToMenu
from game.gui.components.pause_background import PauseBackground
from game.consts import SCREEN_WIDTH


class MenuGui:
    def __init__(self):

        self.menu_panel = MenuPanel()
        self.menu_panel.add_component(PauseBackground())
        self.menu_panel.add_component(StartButton(SCREEN_WIDTH / 2, 250))
        self.menu_panel.add_component(ExitButton(self.menu_panel, SCREEN_WIDTH / 2, 400))
        self.levels_panel = LevelsPanel()
        self.levels_panel.add_component(PauseBackground())
        self.menu_panel.add_component(SelectLevelButton(self.levels_panel, self.menu_panel, SCREEN_WIDTH / 2, 300))
        self.levels_panel.add_component(BackToMenu(self.levels_panel, self.menu_panel, 910, 600))
        self.settings_panel = SettingsPanel()
        self.settings_panel.add_component(PauseBackground())
        self.menu_panel.add_component(SettingsButton(self.settings_panel, self.menu_panel, SCREEN_WIDTH / 2, 350))
        self.settings_panel.add_component(BackToMenu(self.settings_panel, self.menu_panel, 910, 600))

    def draw(self):
        self.menu_panel.draw()
        self.levels_panel.draw()
        self.settings_panel.draw()

    def update(self, delta_time):
        self.menu_panel.update()
        self.levels_panel.update()
        self.menu_panel.update()

    def on_mouse_press(self, x, y, button, modifiers):
        self.menu_panel.on_mouse_press(x, y, button, modifiers)
        self.levels_panel.on_mouse_press(x, y, button, modifiers)
        self.settings_panel.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.menu_panel.on_mouse_release(x, y, button, modifiers)
        self.levels_panel.on_mouse_release(x, y, button, modifiers)
        self.settings_panel.on_mouse_release(x, y, button, modifiers)

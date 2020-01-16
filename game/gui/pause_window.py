import arcade

from game.gui.components.dialogue_box import DialogueBox
from game.gui.themes import gui_theme
from game.managers.score_manager import ScoreManager
from game.consts import SCREEN_WIDTH

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300


class ShowPauseButton(arcade.gui.TextButton):
    def __init__(self, dialoguebox, x, y, width=110, height=50, text="SHOW", theme=None):
        super().__init__(SCREEN_WIDTH-width, y, width, height, text, theme=theme)
        self.dialoguebox = dialoguebox

    def on_press(self):
        if not self.dialoguebox.active:
            self.pressed = True
            ScoreManager.pauseWindowIsActive = True
            self.dialoguebox.active = True
            self.active = False
            #self.dialoguebox.set

    def on_release(self):
        if self.pressed:
            self.pressed = False

    def draw(self):
        if not ScoreManager.pauseWindowIsActive:
            super().draw()



class CloseButton(arcade.gui.TextButton):
    def __init__(self, dialoguebox, x, y, width=110, height=50, text="BACK", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.dialoguebox = dialoguebox

    def on_press(self):
        if self.dialoguebox.active:
            self.pressed = True
            ScoreManager.pauseWindowIsActive = False

    def on_release(self):
        if self.pressed and self.dialoguebox.active:
            self.pressed = False
            self.dialoguebox.active = False
            ScoreManager.gameIsActive = True


class PauseWindow(DialogueBox):
    def __init__(self):
        super().__init__(555, 300,
            WINDOW_WIDTH, WINDOW_HEIGHT, (220, 228, 255), gui_theme.dialogue_box_texture)

        self.half_width = self.width/2
        self.half_height = self.height/2

        color = (220, 228, 255)
        close_button = CloseButton(self, 555, 300,
                                   theme=gui_theme)
        self.button_list.append(close_button)
        message = "GO TO MENU."
        self.text_list.append(arcade.gui.Text(message, 555, 400, gui_theme.font_color))

    def draw(self):
        super().on_draw()

    def on_update(self, delta_time):
        if ScoreManager.pauseWindowIsActive:
            ScoreManager.gameIsActive = False

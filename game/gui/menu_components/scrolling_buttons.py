import arcade
from game.gui.components.button import Button
from game.gui.menu_components.levels_panel import LevelsPanel

DOWN_BUTTON_SPRITE = 'assets/sprites/UI/red_sliderDown.png'
DOWN_BUTTON_GREY = 'assets/sprites/UI/grey_sliderDown.png'
UP_BUTTON_SPRITE = 'assets/sprites/UI/red_sliderUp.png'
UP_BUTTON_GREY = 'assets/sprites/UI/grey_sliderUp.png'
SCALING = 1


class UpButton(Button):
    def __init__(self, window, center_x, center_y):
        super().__init__(center_x, center_y)

        self.window = window
        self.center_x = center_x
        self.center_y = center_y
        self.icon = arcade.Sprite(UP_BUTTON_GREY, SCALING)
        self.pressed = False

    def on_press(self):
        self.pressed = True
        if self.window.offset > 0:
            self.window.offset -= 1
            self.window.add_levels_buttons()

    def on_release(self):
        if self.pressed:
            self.pressed = False

    def draw(self):
        if self.window.offset == 0:
            self.icon = arcade.Sprite(UP_BUTTON_GREY, SCALING)
        else:
            self.icon = arcade.Sprite(UP_BUTTON_SPRITE, SCALING)
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()


class DownButton(Button):
    def __init__(self, window, center_x, center_y):
        super().__init__(center_x, center_y)

        self.window = window
        self.center_x = center_x
        self.center_y = center_y
        self.icon = arcade.Sprite(DOWN_BUTTON_SPRITE, SCALING)
        self.pressed = False

    def on_press(self):
        self.pressed = True
        if self.window.offset < (len(self.window.level_list)-self.window.size):
            self.window.offset += 1
            self.window.add_levels_buttons()

    def on_release(self):
        if self.pressed:
            self.pressed = False

    def draw(self):
        if self.window.offset == (len(self.window.level_list) - self.window.size):
            self.icon = arcade.Sprite(DOWN_BUTTON_GREY, SCALING)
        else:
            self.icon = arcade.Sprite(DOWN_BUTTON_SPRITE, SCALING)
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y
        self.icon.draw()

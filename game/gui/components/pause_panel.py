import arcade
from game.managers.score_manager import ScoreManager


class PausePanel:
    def __init__(self):
        self.visible = False
        self.components = []
        self.text = 'OPTIONS'
        self.x = 0
        self.y = 0

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        if self.visible:
            for component in self.components:
                component.update()
        else:
            return

    def on_mouse_press(self, x, y, button, modifiers):
        if self.visible:
            viewport_left, viewport_right, viewport_bottom, viewport_top = arcade.get_viewport()
            x = viewport_left + self.x + x
            y = viewport_bottom + self.y + y
            for component in self.components:
                component.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        for component in self.components:
            component.on_mouse_release(x, y, button, modifiers)


    def draw(self):
        if self.visible:
            arcade.set_background_color(arcade.color.WHEAT)
            viewport_left, viewport_right, viewport_bottom, viewport_top = arcade.get_viewport()
            for component in self.components:
                component.center_x = viewport_left + self.x + component.initial_x
                component.center_y = viewport_top + self.y - component.initial_y
                component.draw()
            arcade.draw_text(self.text, viewport_left + 375, viewport_top - 70, arcade.csscolor.BLACK, 50)
        else:
            return
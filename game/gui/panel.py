import arcade


class GUIPanel:
    def __init__(self):

        self.visible = True
        self.components = []
        self.x = 0
        self.y = 0
        self.text = None
        self.text_settings = {'x': 0, 'y': 0, 'color': arcade.csscolor.WHITE_SMOKE, 'font_size': 0}

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        if self.visible:
            for component in self.components:
                component.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.visible:
            viewport_left, viewport_right, viewport_bottom, viewport_top = arcade.get_viewport()
            x = viewport_left + self.x + x
            y = viewport_bottom + self.y + y
            for component in self.components:
                component.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.visible:
            for component in self.components:
                component.on_mouse_release(x, y, button, modifiers)

    def draw(self):
        if self.visible:
            viewport_left, viewport_right, viewport_bottom, viewport_top = arcade.get_viewport()
            for component in self.components:
                component.center_x = viewport_left + self.x + component.initial_x
                component.center_y = viewport_top + self.y - component.initial_y
                component.draw()
            if self.text:
                arcade.draw_text(self.text, viewport_left + self.text_settings['x'],
                                 viewport_top - self.text_settings['y'], self.text_settings['color'],
                                 self.text_settings['font_size'])

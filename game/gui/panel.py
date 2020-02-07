import arcade


class GUIPanel:
    def __init__(self):
        self.components = []
        self.x = 0
        self.y = 0

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        for component in self.components:
            component.update()

    def draw(self):
        viewport_left, viewport_right, viewport_bottom, viewport_top = arcade.get_viewport()
        for component in self.components:
            component.center_x = viewport_left + self.x + component.initial_x
            component.center_y = viewport_top + self.y - component.initial_y
            component.draw()

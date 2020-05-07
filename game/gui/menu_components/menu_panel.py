from game.gui.panel import GUIPanel


class MenuPanel(GUIPanel):
    def __init__(self):
        super().__init__()
        self.visible = True
        self.components = []
        self.text = None
        self.x = 0
        self.y = 0

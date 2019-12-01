import arcade

class ShowButton(arcade.gui.TextButton):
    def __init__(self, dialoguebox, x, y, width=110, height=50, text="SHOW", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.dialoguebox = dialoguebox

    def on_press(self):
        if not self.dialoguebox.active:
            self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.dialoguebox.active = True


class CloseButton(arcade.gui.TextButton):
    def __init__(self, dialoguebox, x, y, width=110, height=50, text="BACK", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.dialoguebox = dialoguebox


    def on_press(self):
        if self.dialoguebox.active:
            self.pressed = True

    def on_release(self):
        if self.pressed and self.dialoguebox.active:
            self.pressed = False
            self.dialoguebox.active = False


class PauseWindow(arcade.Window):
    def __init__(self):
        super().__init__()

        self.half_width = self.width/2
        self.half_height = self.height/2
        self.theme = None


    def add_dialogue_box(self):
        color = (220, 228, 255)
        dialoguebox = arcade.gui.DialogueBox(self.half_width, self.half_height, self.half_width*1.5,
                                             self.half_height*1.9, color, self.theme)
        close_button = CloseButton(dialoguebox, self.half_width, self.half_height-205,
                                   theme=self.theme)
        dialoguebox.button_list.append(close_button)
        message = "CHOOSE NEXT WORLD."
        dialoguebox.text_list.append(arcade.gui.Text(message, self.half_width, self.height-100, self.theme.font_color))
        self.dialogue_box_list.append(dialoguebox)

    def add_text(self):
        message = "LEVEL FINISHED. SEE WHAT COMES NEXT"
        self.text_list.append(arcade.gui.Text(message, self.half_width, self.half_height, self.theme.font_color))

    def add_button(self):
        show_button = ShowButton(self.dialogue_box_list[0], self.half_width, self.half_height-100, theme=self.theme)
        self.button_list.append(show_button)

    def set_dialogue_box_texture(self):
        dialogue_box = "assets/sprites/UI/textures/crate0_diffuse.png"
        self.theme.add_dialogue_box_texture(dialogue_box)

    def set_button_texture(self):
        normal = "assets/sprites/UI/grey_button03.png"
        hover = "assets/sprites/UI/grey_button01.png"
        clicked = "assets/sprites/UI/grey_button02.png"
        locked = "assets/sprites/UI/grey_button01.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_theme(self):
        self.theme = arcade.gui.Theme()
        self.set_dialogue_box_texture()
        self.set_button_texture()
        self.theme.set_font(22, arcade.color.SADDLE_BROWN)

    def setup(self):
        arcade.set_background_color(arcade.color.GOLDENROD)
        self.set_theme()
        self.add_dialogue_box()
        self.add_text()
        self.add_button()

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        #arcade.finish_render()

    def on_update(self, delta_time):
        if self.dialogue_box_list[0].active:
            return


def main():
    window = Window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

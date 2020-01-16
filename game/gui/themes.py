import arcade

gui_theme = arcade.gui.Theme()
dialogue_box = "assets/sprites/UI/textures/crate0_diffuse.png"

gui_theme.add_dialogue_box_texture(dialogue_box)

normal = "assets/sprites/UI/grey_button03.png"
hover = "assets/sprites/UI/grey_button01.png"
clicked = "assets/sprites/UI/grey_button02.png"
locked = "assets/sprites/UI/grey_button01.png"
gui_theme.add_button_textures(normal, hover, clicked, locked)

gui_theme.set_font(22, arcade.color.SADDLE_BROWN)
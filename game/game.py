"""
Platformer Game
"""
import arcade

from game.player.player import Player


# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SCALING)

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.wall_list = None
        self.player_list = None
        self.player = None

        # Separate variable that holds the player sprite
        self.player_sprite = None


        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        self.player = Player("assets/sprites/enemies/bee.png", SCALING, 60, 60)

        self.wall_list = arcade.SpriteList()

        # --- Load in a map from the tiled editor ---

        map_name = "template.tmx"
        walls_layer_name = 'Walls'

        # Read in the tiled map
        my_map = arcade.read_tiled_map(map_name, SCALING)

   
        self.wall_list = arcade.generate_sprites(my_map, walls_layer_name, SCALING)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.wall_list, 0)



    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()

        self.player.draw()


    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)

    def update(self, delta_time):
        self.physics_engine.update()
        self.player.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

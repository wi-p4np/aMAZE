import arcade

PLAYER_MOVEMENT_SPEED = 5


class Player(arcade.Sprite):
    def __init__(self, asset_path, scale, x, y):
        super().__init__(asset_path, scale)

        self.center_x = x
        self.center_y = y

    def on_key_press(self, key):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = -PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = 0

    def update(self):
        #sgem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)
        pass


    #def collision_gem(sprite1: arcade.Sprite, sprite2: arcade.Sprite):
        #if 
        #arcade.check_for_collision(sprite1: arcade.Sprite, sprite2: arcade.Sprite)
        


"""
Physics engines for top-down or platformers.
"""
# pylint: disable=too-many-arguments, too-many-locals, too-few-public-methods

import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList


class PhysicsEngineSimple:
    """
    This class will move everything, and take care of collisions.
    """

    def __init__(self, sprite: Sprite):
        """
        Constructor.
        """
        assert(isinstance(sprite, Sprite))
        self.sprite = sprite

        self._prev_x = sprite.center_x
        self._prev_y = sprite.center_y
        self._hits_list = []
        self._collision_on_x = False
        self._collision_on_y = False

    def update(self):
        """
        Move everything
        """
        # --- Move in the x direction

        self._prev_x, self._prev_y = self.sprite.center_x, self.sprite.center_y
        self._hits_list = []
        self._collision_on_x = False
        self._collision_on_y = False

        #self.player_sprite.center_y += self.player_sprite.change_y

    def check(self, others: SpriteList):
        total_hits_list = []

        # check X
        self.sprite.center_x += self.sprite.change_x

        hit_list = \
            arcade.check_for_collision_with_list(self.sprite,
                                                 others)
        if hit_list:
            self._collision_on_x = True

        self.sprite.center_x = self._prev_x
        total_hits_list.extend(hit_list)

        # check Y
        self.sprite.center_y += self.sprite.change_y

        hit_list = \
            arcade.check_for_collision_with_list(self.sprite,
                                                 others)
        if hit_list:
            self._collision_on_y = True

        self.sprite.center_y = self._prev_y

        total_hits_list.extend(hit_list)

        self._hits_list.extend(total_hits_list)
        return total_hits_list

    def resolve(self):
        """
        Resolve collisions
        """
        if not self._collision_on_x:
            self.sprite.center_x += self.sprite.change_x

        if not self._collision_on_y:
            self.sprite.center_y += self.sprite.change_y


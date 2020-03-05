"""
Physics engines for top-down or platformers.
"""
# pylint: disable=too-many-arguments, too-many-locals, too-few-public-methods

from arcade.geometry import check_for_collision_with_list
from arcade.geometry import check_for_collision
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList


class PhysicsEngineSimple:
    """
    This class will move everything, and take care of collisions.
    """

    def __init__(self, player_sprite: Sprite):
        """
        Constructor.
        """
        assert(isinstance(player_sprite, Sprite))
        self.player_sprite = player_sprite

        self._prev_x = player_sprite.center_x
        self._prev_y = player_sprite.center_y
        self._hits_list = []

    def check(self, others: SpriteList):
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          others)
        self._hits_list.extend(hit_list)
        return hit_list

    def resolve(self):
        """
        Resolve collisions
        """
        if len(self._hits_list) > 0:
            self.player_sprite.center_x = self._prev_x
            self.player_sprite.center_y = self._prev_y

    def update(self):
        """
        Move everything
        """
        # --- Move in the x direction

        self._prev_x, self._prev_y = self.player_sprite.center_x, self.player_sprite.center_y
        self._hits_list = []

        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

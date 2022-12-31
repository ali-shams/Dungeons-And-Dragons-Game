from random import choice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from helper.hints import AxisLoc

from grid.world import World


class Character:
    """
    class Character
    """

    def __init__(self, loc: 'AxisLoc', *args, **kwargs) -> None:
        """
        Constructor
        Parameters
        ----------
        `loc`: `AxisLoc`
        """
        self.loc: 'AxisLoc' = loc
        self.row: int = loc[0]
        self.col: int = loc[1]

    def update_loc(self, movement: str, world: World) -> 'AxisLoc':
        """
        update entity loc based on movement in the world
        Parameters
        ----------
        `movement`: `str`
            entity movement
        `world`: `World`
        Returns
        -------
        `AxisLoc`: updated AxisLoc
        """
        # update self.row and self.col because of load the game
        # in the middle of the game
        self.row = self.loc[0]
        self.col = self.loc[1]

        if movement in ('up', 'down'):
            self.check_height_boundary(movement, world)
        else:
            self.check_width_boundary(movement, world)
        self.loc = (self.row, self.col)

    def check_height_boundary(self, movement: str, world: World) -> None:
        """
        check north and south boundary
        Parameters
        ----------
        `movement`: `str`
            entity movement
        `world`: `World`
        """
        if (self.row - 1 < 0 and movement == 'up') or (
                self.row + 1 == world.height and movement == 'down'):
            pass
        elif movement == 'up':
            self.row -= 1
        else:
            self.row += 1

    def check_width_boundary(self, movement: str, world: World) -> None:
        """
        check west and east boundary
        Parameters
        ----------
        `movement`: `str`
            entity movement
        `world`: `World`
        """
        if (self.col - 1 < 0 and movement == 'left') or (
                self.col + 1 == world.width and movement == 'right'):
            pass
        elif movement == 'left':
            self.col -= 1
        else:
            self.col += 1

    def distance(self, other) -> int:
        """
        calculate self.loc distance from other.loc
        based on Manhattan distance
        Parameters
        ----------
        `self`: `Object`
        `other`: `Object`
        Returns
        -------
        `int`: distance self instance from other distance
        """
        x_distance: int = abs(self.row - other.row)
        y_distance: int = abs(self.col - other.col)
        return x_distance + y_distance

    def which_direction_of(self, other) -> str:
        """
        calculate self.loc direction from other.loc
        based on Manhattan geometry
        Parameters
        ----------
        `self`: `Object`
        `other`: `Object`
        Returns
        -------
        `str`: direction of self relative to the other object
        """
        if self.row > other.row and self.col > other.col:
            movement: str = choice(('down', 'right'))
        elif self.row > other.row and self.col < other.col:
            movement: str = choice(('down', 'left'))

        elif self.row < other.row and self.col > other.col:
            movement: str = choice(('up', 'right'))
        elif self.row < other.row and self.col < other.col:
            movement: str = choice(('up', 'left'))

        elif self.row == other.row and self.col > other.col:
            movement: str = 'right'
        elif self.row == other.row and self.col < other.col:
            movement: str = 'left'

        elif self.row > other.row and self.col == other.col:
            movement: str = 'down'
        elif self.row < other.row and self.col == other.col:
            movement: str = 'up'
        return movement

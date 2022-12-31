from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character.user import User
    from game.game import Game

import numpy as np

from helper.utils import ConstantCharacters as CONSTANTS


class World:
    """
    class World
    """

    def __init__(self, game: 'Game', *args, **kwargs) -> None:
        """
        Constructor
        Parameters
        ----------
        `game` : `Game`
        """
        self.height: int = game.height
        self.width: int = game.width
        self.create_world()

    def create_world(self) -> None:
        """
        Create height x width numpy array
        example:
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
        """
        self.world: np = np.full(shape=(self.height, self.width),
                                 fill_value=None)

    def display_world(self, user: 'User') -> None:
        """
        display world in terminal
        example:
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
        Parameters
        ----------
        `user`: `User`
        """
        for row in range(self.height):
            print((CONSTANTS.SPACE_CHARACTER.value +
                   CONSTANTS.HORIZONTAL_PLACE_HOLDER.value) * self.width)
            for col in range(self.width):
                if (row, col) == user.loc:
                    print((CONSTANTS.VERTICAL_PLACE_HOLDER.value +
                           CONSTANTS.USER_CHARACTER.value),
                          end=CONSTANTS.SPACE_CHARACTER.value)
                else:
                    print((CONSTANTS.VERTICAL_PLACE_HOLDER.value +
                           CONSTANTS.SPACE_CHARACTER.value * 2),
                          end=CONSTANTS.SPACE_CHARACTER.value)
            print(CONSTANTS.VERTICAL_PLACE_HOLDER.value)
        print((CONSTANTS.SPACE_CHARACTER.value +
               CONSTANTS.HORIZONTAL_PLACE_HOLDER.value) * self.width)

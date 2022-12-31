from helper.hints import AxisLoc

from character.character import Character


class User(Character):
    """
    class User
    """

    def __init__(self, user_loc: 'AxisLoc', *args, **kwargs) -> None:
        """
        Constructor
        Parameters
        ----------
        `user_loc` : `AxisLoc`
        """
        super().__init__(user_loc)

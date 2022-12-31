from helper.hints import AxisLoc

from character.character import Character


class Dragon(Character):
    """
    class Dragon
    """

    def __init__(self, dragon_loc: AxisLoc, *args, **kwargs) -> None:
        """
        Constructor
        Parameters
        ----------
        `dragon_loc` : `AxisLoc
        """
        super().__init__(dragon_loc)

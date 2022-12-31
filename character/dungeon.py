from helper.hints import AxisLoc

from character.character import Character


class Dungeon(Character):
    """
    class Dungeon
    """

    def __init__(self, dungeon_loc: AxisLoc, *args, **kwargs) -> None:
        """
        Constructor
        Parameters
        ----------
        `dungeon_loc` : `AxisLocation`
        """
        super().__init__(dungeon_loc)

from typing import (
    Tuple,
    Annotated,
    NewType
)

from character.character import Character

AxisLoc = NewType('AxisLoc', Tuple[int, int])
QuadrupleLocs = NewType('QuadrupleLocs', Annotated[Tuple[AxisLoc], 4])
Players = NewType('Player', Annotated[Character, 3])

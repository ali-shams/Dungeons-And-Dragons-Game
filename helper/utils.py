from enum import Enum
from typing import Tuple


class ConstantCharacters(Enum):
    """
    class ConstantCharacters
    """
    WELCOME_MESSAGE: str = 'Welcome to the Dungeons & Dragons'
    MOVEMENTS: Tuple = ('up', 'right', 'down', 'left')
    HORIZONTAL_PLACE_HOLDER: str = '\u2501' * 3  # Unicode character “-”
    VERTICAL_PLACE_HOLDER: str = '\u2502'  # Unicode character “|”
    SPACE_CHARACTER: str = ' '
    USER_CHARACTER: str = ' U'
    DIFFICULTY_LEVEL: Tuple = ('hard', 'medium', 'easy')

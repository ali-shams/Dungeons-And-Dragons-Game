from helper.utils import ConstantCharacters as CONSTANTS


class Base:
    """
    class Base
    """

    @property
    def height(self) -> str:
        """
        getter for world height attribute
        """
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        """
        setter for world height attribute
        Parameters
        ----------
        `height` : `int`
            world height attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if str(height).isdigit():
            if int(height) > 1:
                self.__height: int = int(height)
            else:
                raise ValueError(f'{height} is invalid. '
                                 f'height must be greater than 1.')
        else:
            raise TypeError(f'{height} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def width(self) -> str:
        """
        getter for world width attribute
        """
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        """
        setter for world width attribute
        Parameters
        ----------
        `width` : `int`
            world width attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if str(width).isdigit():
            if int(width) > 1:
                self.__width: int = int(width)
            else:
                raise ValueError(f'{width} is invalid. '
                                 f'width must be greater than 1.')
        else:
            raise TypeError(f'{width} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def difficulty(self) -> str:
        """
        getter for difficulty attribute
        """
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty: str) -> None:
        """
        setter for difficulty attribute
        Parameters
        ----------
        `difficulty` : `str`
            game difficulty attribute
        Raises
        ----------
        ValueError: when difficulty is not a possible value
        """
        if difficulty in CONSTANTS.DIFFICULTY_LEVEL.value:
            self.__difficulty: str = difficulty
        else:
            raise ValueError(f'{difficulty} is invalid. '
                             'difficulty must be "hard", "medium" or "easy".')

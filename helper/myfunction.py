import functools
from tabulate import tabulate
from typing import List


def style(func) -> None:
    """
    decorate print built-in function
    example:
    +-----------------+
    | [Your messages] |
    +-----------------+
    Parameters
    ----------
    `func`: `builtins`
    """

    @functools.wraps(func)
    def wrapper_style(message) -> None:
        table: List[List] = [[message]]
        styled_message: tabulate = tabulate(table, tablefmt='grid')
        return func(styled_message)

    return wrapper_style


@style
def _print(message: str) -> None:
    """
    print message with specific style, decorated by style function
    Parameters
    ----------
    `message`: `str`
    """
    return print(message)

import os
from time import sleep
from typing import Tuple, List
from random import choices

from helper.hints import Players
from helper.myfunction import _print
from helper.utils import ConstantCharacters as CONSTANTS

from game.game import Game
from grid.world import World
from character.user import User
from character.dragon import Dragon
from character.dungeon import Dungeon
from character.character import Character


def main() -> Tuple[Game, World, User, Dragon, Dungeon]:
    """
    clear screen and create a game, world, user, dragon,
    and dungeon instances
    Returns
    -------
    `game`: `Game`
        an instance of the Game class
    `world`: `World`
        an instance of the World class
    `user`: `User`
        an instance of the User class
    `dragon`: `Dragon`
        an instance of the Dragon class
    `dungeon`: `Dungeon`
        an instance of the Dungeon class
    """
    clear_screen()
    _print(CONSTANTS.WELCOME_MESSAGE.value)
    game: Game = Game()
    world: World = World(game)
    (user, dragon, dungeon) = create_characters(game)
    return (game, world, user, dragon, dungeon)


def clear_screen() -> None:
    """
    clear terminal screen based on OS
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def create_characters(game: Game) -> Players:
    """
    create user, dragon, and dungeon characters based on location
    Parameters
    ----------
    `game`: `Game`
    Returns
    -------
    `(User, Dragon, Dungeon)`: quadruple characters
    """
    user: User = User(game.user_loc)
    dragon: Dragon = Dragon(game.dragon_loc)
    dungeon: Dungeon = Dungeon(game.dungeon_loc)
    return (user, dragon, dungeon)


def play_game(game: Game,
              world: World,
              user: User,
              dragon: Dragon,
              dungeon: Dungeon) -> None:
    """
    start game flow
    Parameters
    ----------
    `game`: `Game`
    `world`: `World`
    `user`: `User`
    `dragon`: `Dragon`
    `dungeon`: `Dungeon`
    """
    display_world(world, user)
    sensitivity_check(world, user, dragon, dungeon)
    action: str = display_menu(user)
    while action != 'quit':

        if action in CONSTANTS.MOVEMENTS.value:
            user.update_loc(action, world)
            sensitivity_check(world, user, dragon, dungeon)

            if is_win(user, dungeon) or is_lose(user, dragon):
                break

        elif action == 'help':
            help_game(game, user, dragon, dungeon)

        elif action == 'save':
            save_game(game, world, user, dragon, dungeon)

        elif action == 'load':
            load_game(game, world, user, dragon, dungeon)

        elif action == 'new':
            (game, world, user, dragon, dungeon) = main()

        else:
            while action not in CONSTANTS.MOVEMENTS.value and \
                    action not in \
                    ['quit', 'help', 'save', 'load', 'new']:
                _print('Unknown command, please try again.')
                action: str = display_menu(user)
            continue

        display_world(world, user)
        action: str = display_menu(user)

    else:
        _print('End')


def display_world(world: World, user: User) -> None:
    """
    display the world with user location in terminal
    example:
         ━━━ ━━━ ━━━ ━━━ ━━━
        │   │ U │   │   │   │
         ━━━ ━━━ ━━━ ━━━ ━━━
        │   │   │   │   │   │
         ━━━ ━━━ ━━━ ━━━ ━━━
        │   │   │   │   │   │
         ━━━ ━━━ ━━━ ━━━ ━━━
    'U' is user location
    Parameters
    ----------
    `world`: `World`
    `user`: `User`
    """
    clear_screen()
    world.display_world(user)


def sensitivity_check(world: World,
                      user: User,
                      dragon: Dragon,
                      dungeon: Dungeon) -> None:
    """
    check sensitivity based on the distance user from the dragon
    Parameters
    ----------
    `world`: `World`
    `user`: `User`
    `dragon`: `Dragon`
    `dungeon`: `Dungeon`
    """
    user_distance_of_dragon: int = user.distance(dragon)
    user_direction_toward_dragon: str = user.which_direction_of(dragon)
    dragon_direction_toward_user: str = dragon.which_direction_of(user)

    if user_distance_of_dragon == 1 or user_distance_of_dragon == 3:
        movement: str = choose_movement_by_distance(
            user_direction_toward_dragon,
            dragon_direction_toward_user,
            user_distance_of_dragon)

        if is_not_collocations_after_movement(movement,
                                              world,
                                              dragon,
                                              dungeon):
            dragon.update_loc(movement, world)

    elif user_distance_of_dragon == 2:
        _print('** Be careful. The dragon is near your '
               f'{dragon_direction_toward_user}.! **')


def choose_movement_by_distance(user_direction_toward_dragon: str,
                                dragon_direction_toward_user: str,
                                user_distance_of_dragon: int) -> str:
    """
    choose movement based on the distance user from the dragon
    Parameters
    ----------
    `user_direction_toward_dragon`: `str`
    `dragon_direction_toward_user`: `str`
    `user_distance_of_dragon`: `int`
        distance user from dragon
    Returns
    -------
    `str`: a movement based on the user's location relative to the dragon
    """
    if user_distance_of_dragon == 1:
        _print('** The dragon is on your '
               f'{dragon_direction_toward_user} side. **')
        movement: str = choose_movement_by_probability(
            user_direction_toward_dragon, 90)

    elif user_distance_of_dragon == 3:
        movement: str = choose_movement_by_probability(
            user_direction_toward_dragon, 30)

    return movement


def choose_movement_by_probability(user_direction_toward_dragon: str,
                                   percentage: int) -> str:
    """
    choose movement by specific probability based on
    the distance user from the dragon
    Parameters
    ----------
    `user_direction_toward_dragon`: `str`
    `percentage`: `int`
        probability percentage
    Returns
    -------
    `str`: a movement based on the user's location relative to
           the dragon and a specific probability
    """
    weights: List = [percentage] + [(100 - percentage) / 3] * 3
    if user_direction_toward_dragon == 'up':
        ...
    elif user_direction_toward_dragon == 'left':
        rotate_probability(weights, 1)
    elif user_direction_toward_dragon == 'down':
        rotate_probability(weights, 2)
    else:
        rotate_probability(weights, 3)
    movement: str = ' '.join(choices(CONSTANTS.MOVEMENTS.value, weights))
    return movement


def rotate_probability(weights: list, count: int) -> None:
    """
    rotate weights probability based on movement
    Parameters
    ----------
    `weights`: `list`
    `count`: `int`
        count for rotate
    """
    for _ in range(count):
        weights.append(weights.pop(0))


def is_not_collocations_after_movement(movement: str,
                                       world: World,
                                       dragon: Dragon,
                                       dungeon: Dungeon) -> bool:
    """
    check collocations with dungeon, after the dragon move
    Parameters
    ----------
    `movement`: str
    `world`: `World`
    `dragon`: `Dragon`
    `dungeon`: `Dungeon`
    Returns
    -------
    `bool`: true if the dragon's movement causes its location
    to match with the location of the dungeon,
            false otherwise
    """
    collocations_obj: Character = Character(dragon.loc)
    collocations_obj.update_loc(movement, world)
    is_not_collocation: bool = True
    if collocations_obj.loc == dungeon.loc:
        is_not_collocation = False
    return is_not_collocation


def display_menu(user: User) -> str:
    """
    display message for choosing possible action
    possible actions are:
    [x] UP, RIGHT, DOWN AND LEFT
    [x] HELP
    [x] NEW
    [x] SAVE
    [x] LOAD
    [x] QUIT
    Parameters
    ----------
    `user`: `User`
    Returns
    -------
    `str`: a possible action
    """
    action: str = input(f'Your are currently on room {user.loc},\n'
                        f'you can move "UP", "RIGHT", "DOWN" AND "LEFT",\n'
                        f'Enter "HELP" to help,\n'
                        f'Enter "NEW" to new,\n'
                        f'Enter "SAVE" to save,\n'
                        f'Enter "LOAD" to load,\n'
                        f'Enter "QUIT" to quit: ').lower()
    return action


def is_win(user: User, dungeon: Dungeon) -> bool:
    """
    check user win if user loc equal dungeon loc
    Parameters
    ----------
    `user`: `User`
    `dungeon`: `Dungeon`
    Returns
    -------
    `bool`: win or lose
    """
    if user.loc == dungeon.loc:
        _print('** Congratulation you win! **')
        return True


def is_lose(user: User, dragon: Dragon) -> bool:
    """
    check user lose if user loc equals dragon loc
    Parameters
    ----------
    `user`: `User`
    `dragon`: `Dragon`
    Returns
    -------
    `bool`: win or lose
    """
    if user.loc == dragon.loc:
        _print('** OH NO! The dragon got you! Better luck next time! **')
        return True


def help_game(game: Game,
              user: User,
              dragon: Dragon,
              dungeon: Dungeon) -> None:
    """
    help game based on game difficulty
    Parameters
    ----------
    `game`: `Game`
    `user`: `User`
    `dragon`: `Dragon`
    `dungeon`: `Dungeon`
    """
    if game.reward_level != 0:

        if game.difficulty == CONSTANTS.DIFFICULTY_LEVEL.value[0] \
                or game.difficulty == CONSTANTS.DIFFICULTY_LEVEL.value[1]:
            dragon_direction_toward_user: str = dragon.which_direction_of(user)
            _print('** The dragon is on your '
                   f'{dragon_direction_toward_user} side. **')
            game.reward_level -= 1

        else:
            dungeon_direction_toward_user: str = \
                dungeon.which_direction_of(user)
            _print('** The dungeon is on your '
                   f'{dungeon_direction_toward_user} side. **')

    else:
        _print('You are out of reward. '
               'Your reward level is 0 now.')
    sleep(2)


def save_game(game: Game,
              world: World,
              user: User,
              dragon: Dragon,
              dungeon: Dungeon) -> None:
    """
    save game status
    Parameters
    ----------
    `game`: `Game`
    `world`: `World`
    `user`: `User`
    `dragon`: `Dragon`
    `dungeon`: `Dungeon`
    """
    game.save_data(world, user, dragon, dungeon)
    _print('The game status was saved successfully.')
    sleep(2)


def load_game(game: Game,
              world: World,
              user: User,
              dragon: Dragon,
              dungeon: Dungeon) -> None:
    """
    load game status
    Parameters
    ----------
    `game`: `Game`
    `world`: `World`
    `user`: `User`
    `dragon`: `Dragon`
    `dungeon`: `Dungeon`
    """
    clear_screen()
    game.load_data()
    (world.height, world.width,
     user.loc, dragon.loc, dungeon.loc) = \
        (game.height, game.width,
         game.user_loc, game.dragon_loc,
         game.dungeon_loc)
    _print('The game status was loaded successfully.')
    sleep(2)


if __name__ == '__main__':
    (game, world, user, dragon, dungeon) = main()
    play_game(game, world, user, dragon, dungeon)

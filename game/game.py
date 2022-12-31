from itertools import product
from random import sample
from typing import List

from game.base import Base
from grid.world import World
from character.user import User
from character.dragon import Dragon
from character.dungeon import Dungeon
from database.database import DataBase


class Game(Base):
    """
    class Game
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.db: DataBase = DataBase()
        self.make_decsion()

    def make_decsion(self) -> None:
        """
        deciding whether the game is new or load
        Raises
        ----------
        ValueError: when decision is invalid
        """
        decision: str = input('Enter "new" for new game or "load"'
                              'to select among games loads: ').lower()
        if decision == 'new':
            self.get_dimensions()
            self.set_difficulty()
            self.set_reward()
            self.get_new_coordinates()
        elif decision == 'load':
            self.load_data()
        else:
            raise ValueError(f'{decision} is invalid. '
                             f'you must choose between "new" or "load".')

    def get_dimensions(self) -> None:
        """
        get height, width from end user for create world
        """
        self.height: int = input('Enter height of your grid world: ')
        self.width: int = input('Enter width of your grid world: ')

    def set_difficulty(self) -> None:
        """
        get game difficulty from end user
        """
        self.difficulty: str = input('Choose difficulty, '
                                     '"hard", "medium" or "easy": ').lower()

    def set_reward(self) -> None:
        """
        set reward level based on game difficulty
        """
        self.reward_level: int = 1
        if self.difficulty == 'medium':
            self.reward_level: int = 3

    def get_new_coordinates(self) -> None:
        """
        get three random coordinates for user, dragon and dungeon
        in height x width world
        """
        all_possible_coordinates: List = list(
            product(range(self.height), range(self.width)))
        (self.user_loc, self.dragon_loc, self.dungeon_loc) = sample(
            all_possible_coordinates, k=3)

    def save_data(self,
                  world: World,
                  user: User,
                  dragon: Dragon,
                  dungeon: Dungeon) -> None:
        """
        save data into the database
        Parameters
        ----------
        `world`: `World`
        `user`: `User`
        `dragon`: `Dragon`
        `dungeon`: `Dungeon`
        """
        self.db.save_data(world.height, world.width,
                          user.loc, dragon.loc, dungeon.loc,
                          self.reward_level, self.difficulty)

    def load_data(self) -> None:
        """
        load data from the database
        """
        (self.height, self.width, self.user_loc, self.dragon_loc,
         self.dungeon_loc, self.reward_level, self.difficulty) = \
            self.db.load_data()

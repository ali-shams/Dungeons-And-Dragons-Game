import psycopg2.extras
import functools
from datetime import datetime
from typing import List

from helper.hints import AxisLoc
from helper.config import config


class DataBase:
    """
    class DataBase
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.__conn = None
        self.__cur = None

    def connect(func) -> None:
        """
        connect to the PostgreSQL database server
        Parameters
        ----------
        `func`
        Raises
        ----------
        Exception: error while connecting to PostgreSQL
        """

        @functools.wraps(func)
        def wrapper(self, *args) -> None:
            try:
                params = config()
                self.__conn = psycopg2.connect(**params)
                self.__cur = self.__conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                return func(self, *args)
            except (Exception,
                    psycopg2.Error) as error:
                print('Error while connecting to PostgreSQL', error)
            finally:
                if (self.__conn):
                    self.__cur.close()
                    self.__conn.close()

        return wrapper

    connect = staticmethod(connect)

    @connect
    def save_data(self, height: int, width: int,
                  user_loc: AxisLoc, dragon_loc: AxisLoc, dungeon_loc: AxisLoc,
                  reward_level: int, difficulty: str) -> None:
        """
        save game status
        Parameters
        ----------
        `height`: `int`
        `width`: `int`
        `user_loc`: `AxisLoc`
        `dragon_loc`: `AxisLoc`
        `dungeon_loc`: `AxisLoc`
        `reward_level`: `int`
        `difficulty`: `str`
        """
        insert_script = "INSERT INTO game_status" \
                        "(world_height, world_width, user_loc," \
                        "dragon_loc, dungeon_loc," \
                        "reward_level, difficulty, last_save) VALUES " \
                        "(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert_value = (height, width,
                        user_loc, dragon_loc, dungeon_loc, reward_level,
                        difficulty, datetime.now())
        self.__cur.execute(insert_script, insert_value)
        self.__conn.commit()

    @connect
    def load_data(self):
        """
        load three last loads
        """
        self.__cur.execute('select * from game_status ORDER BY last_save DESC LIMIT 3')
        records = self.__cur.fetchall()
        load_numbers = [record['id'] for record in records]

        if not records:
            print('There is no load slot yet.')
        else:
            self.display_loads(records)
            load_number: int = int(input('Please select load game '
                                         'based on an load number: '))
            if load_number in load_numbers:
                record = self.find_load(load_number, records)
                return (record['world_height'],
                        record['world_width'],
                        eval(record['user_loc']),
                        eval(record['dragon_loc']),
                        eval(record['dungeon_loc']),
                        record['reward_level'],
                        record['difficulty'])
            else:
                raise ValueError('Load in invalid.')

    def display_loads(self, records: List) -> None:
        """
        display games loads
        Parameters
        ----------
        `records`: `List`
        """
        for record in records:
            print(f'Load number "{record["id"]}" - '
                  f'Date saved "{record["last_save"]}"')

    def find_load(self, load_number: int, records: List) -> List:
        """
        find load number in records
        Parameters
        ----------
        `load_number`: `int`
        `records`: `List`
        Returns
        -------
        `List`
        """
        for record in records:
            if record['id'] == load_number:
                return record

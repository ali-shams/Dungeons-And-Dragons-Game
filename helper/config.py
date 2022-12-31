from typing import Dict

from configparser import ConfigParser


def config(filename: str = 'database/database.ini',
           section: str = 'postgresql') -> Dict:
    """
    create a parser and read config file
    Parameters
    ----------
    `filename` : `str`
        database.ini file path in your directory
    `section` : `str`
        default postgresql
    Returns
    -------
    `Dict`: a dict of config information
    """
    parser = ConfigParser()
    parser.read(filename)
    db: Dict = dict()
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

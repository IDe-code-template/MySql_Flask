"""
    Main module for getting the config from 
    an .ini file on the root of the project
"""
import configparser
import os


def readConfigFile(section_name, key_name):
    """
    Read Configuration file

    Args:
        section_name (:string) section name of the ini file.
        key_name (:string) key name for getting value
    Returns:
        String: Value if 
    Raises:
        Exception if any DB error occures
    """
    try:
        curr_folder = os.path.dirname(os.path.abspath(__file__))
        initfile = os.path.join(os.path.dirname(curr_folder), "config.ini")
        config = configparser.ConfigParser()
        config.read(initfile)
        return config.get(section_name, key_name)
    except Exception as err:
        raise err

import os
from configparser import ConfigParser

config = ConfigParser(interpolation=None)
config.read(os.path.join('data', 'data.ini'))



def get_conf_param(section, parameter):
    result = config.get(section, parameter)
    return result


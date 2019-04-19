# -*- coding: utf-8 -*-

import configparser

DEFAULT_CONFIG_FILE = "./config.ini"

class ConfigUtil():


    def __init__(self, config_file=None):
        self.config = configparser.ConfigParser()
        print('config-read')
        if config_file:
            self.config.read(config_file)
        self.config.read(DEFAULT_CONFIG_FILE)

_util = ConfigUtil()


def get(section, key):
    return _util.config.get(section, key)


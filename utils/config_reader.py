import configparser

from utils.constants import Constants


class ConfigReader:

    config = configparser.ConfigParser()

    config.read(
        Constants.CONFIG_FILE_PATH
    )

    @classmethod
    def get(cls, section, key):

        return cls.config.get(
            section,
            key
        )
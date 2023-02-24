from configparser import ConfigParser
import os.path as path


class Configurator:

    # fill the initial configuration file inside the verify method
    @staticmethod
    def verify():
        if not path.exists("config.ini"):
            config = ConfigParser()
            config["CONSTANTS"] = {
                "version": "1.0.0",
                "env": "TEST"
            }
            with open("config.ini", "w") as file:
                config.write(file)


    @staticmethod
    def read(section, key):
        Configurator.verify()
        config = ConfigParser()
        config.read("config.ini")
        return config[section][key]

    @staticmethod
    def read_list(section, key, delimiter):
        Configurator.verify()
        config = ConfigParser()
        config.read("config.ini")
        data = config[section][key].split(delimiter)
        return list(map(str.strip, data))

    @staticmethod
    def update(section, key, value):
        Configurator.verify()
        config = ConfigParser()
        config.read("config.ini")
        config.set(section, key, value)
        with open("config.ini", "w") as file:
            config.write(file)

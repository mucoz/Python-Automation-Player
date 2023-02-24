import window, sys
from logger import Logger as log
from configurator import Configurator as config
from globals import Globals


def initialize():
    # start logging
    log.start()
    # verify config.ini file
    config.verify()
    # read env from config file
    Globals.env = config.read("CONSTANTS", "env")


def main():
    # create new python file and a class
    # inside the class, write "main" method
    # write everything under that main method
    # add the class name to the list in pipeline file

    initialize()
    log.info("Window is being created...")
    win = window.NewWindow()
    log.info("Window has been closed.")
    log.finish()


main()

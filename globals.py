from enum import Enum
import logger
import utils

class PlayStatus(Enum):
    NOT_STARTED = 0,
    STARTED = 1,
    PAUSED = 2,
    RESUMED = 3,
    STOPPED = 4,
    COMPLETED = 5


class Globals:
    env = ""
    label_status = "Ready."
    progressbar_length = 0
    progressbar_status = 0
    playing_status = ""

    @staticmethod
    def update_status(message):
        Globals.label_status = message
        Globals.progressbar_status += 1
        logger.Logger.info(message)

    @staticmethod
    def check_progress():
        if Globals.playing_status == PlayStatus.PAUSED:
            Globals.label_status = "Current task has been paused."
            while True:
                if Globals.playing_status == PlayStatus.RESUMED:
                    return
                if Globals.playing_status == PlayStatus.STOPPED:
                    Globals.label_status = "Current has been stopped."
                    return
        if Globals.playing_status == PlayStatus.STOPPED:
            Globals.label_status = "Current has been stopped."
            return

    @staticmethod
    def throw_exception(text):
        if Globals.playing_status != PlayStatus.STOPPED:
            logger.Logger.error(text)
            utils.show_message("Error", text, 48)
            Globals.playing_status = PlayStatus.STOPPED
        return


# the variables that need to be transffered between pipeline modules will be defined here
# example
class Variables:
    data_dict = {}
import time
from globals import Globals
from logger import Logger as log


class TaskOne:

    def __init__(self):
        Globals.label_status = "Task one is being initialized..."
        Globals.progressbar_status = 0
        Globals.progressbar_length = 4

    def main(self):

        try:
            for i in range(Globals.progressbar_length):
                Globals.update_status("Processing module #1 task #" + str(i+1) + "...")
                log.info("task_one_" + str(i+1) + " has been executed.")
                time.sleep(1)

        except Exception:
            Globals.throw_exception("Error occurred while working on task one.")
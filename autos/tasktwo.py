import time
from globals import Globals
from logger import Logger as log


class TaskTwo:

    def __init__(self):
        Globals.label_status = "Task one is being initialized..."
        Globals.progressbar_status = 0
        Globals.progressbar_length = 7

    def main(self):

        try:
            for i in range(Globals.progressbar_length):
                Globals.update_status("Processing module #2 task #" + str(i+1) + "...")
                log.info("task_two" + str(i+1) + " has been exeecuted.")
                time.sleep(1)
        except Exception:
            Globals.throw_exception("Error occurred while working task two.")
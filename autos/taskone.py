import time
from globals import Globals


class TaskOne:

    def __init__(self):
        Globals.label_status = "Task one is being initialized..."
        Globals.progressbar_status = 0
        Globals.progressbar_length = 4

    def main(self):

        try:
            for i in range(Globals.progressbar_length):
                Globals.progressbar_status = i + 1
                Globals.label_status = "Processing " + str(i)
                print("task_one_" + str(i+1) + " has been executed.")
                time.sleep(1)
        except Exception:
            Globals.throw_exception("Error occurred while working on task one.")
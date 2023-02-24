from autos.taskone import TaskOne
from autos.tasktwo import TaskTwo
from globals import Globals, PlayStatus
import sys


class Sentinel(Exception): pass


class SetTrace(object):
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        sys.settrace(self.func)
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.settrace(None)
        # This catches Sentinel, and lets other errors through
        return isinstance(exc_value, Sentinel)


def monitor(frame, event, arg):
    if event == "line":
        Globals.check_progress()
        if Globals.check_progress() == PlayStatus.STOPPED:
            raise Sentinel

    return monitor


class Pipeline:

    @staticmethod
    def start():
        # write the automation modules inside this list
        task_list = [TaskOne, TaskTwo]

        for task in task_list:
            next_task = task()
            with SetTrace(monitor):
                next_task.main()
            if Globals.playing_status == PlayStatus.STOPPED:
                Globals.progressbar_status = 100
                Globals.playing_status = PlayStatus.COMPLETED
                del next_task
                return
            del next_task
        Globals.progressbar_status = 100
        Globals.playing_status = PlayStatus.COMPLETED


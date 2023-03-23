import tkinter as tk
from tkinter import ttk
from threading import Thread
from logger import Logger as log
from globals import Globals, PlayStatus
from pipeline import Pipeline


class NewWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Automation Player')
        self.window.resizable(False, False)
        self.center_screen(284, 90)
        self.background_color = '#E0E0E0'
        self.window.configure(bg=self.background_color)
        self.window.iconbitmap(r"icon.ico")
        self.window.resizable(False, False)
        self.create_elements()
        self.label_status["text"] = Globals.label_status
        self.progressbar_status["value"] = Globals.progressbar_status
        self.playing_status = Globals.playing_status
        self.button_stop["state"] = "disabled"
        self.window.mainloop()

    def center_screen(self, width, height):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (width / 2))
        y_cordinate = int((screen_height / 2) - (height / 2))
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x_cordinate, y_cordinate))

    def create_elements(self):

        self.button_start = ttk.Button(self.window, text='Start', command=self.button_start_onclick)
        self.button_start.place(x=24, y=22, width=89, height=32)

        self.button_stop = ttk.Button(self.window, text='Stop', command=self.button_stop_onclick)
        self.button_stop.place(x=162, y=22, width=89, height=32)

        self.label_status = ttk.Label(self.window, text='', background=self.background_color)
        self.label_status.place(x=24, y=62)

        self.progressbar_status = ttk.Progressbar(self.window, orient='horizontal', length=180, mode='determinate')
        self.progressbar_status.place(x=24, y=90, width=227, height=16)

    def check_globals(self):
        while True:
            self.label_status["text"] = Globals.label_status
            self.progressbar_status.configure(maximum=Globals.progressbar_length)
            self.progressbar_status["value"] = Globals.progressbar_status
            if Globals.playing_status == PlayStatus.COMPLETED:
                self.label_status["text"] = "Completed."
                self.progressbar_status["value"] = 100
                self.button_start["text"] = "Start"
                self.button_start["state"] = "enabled"
                self.button_stop["state"] = "disabled"
                break

    def button_start_onclick(self):
        if self.button_start["text"] == "Start":
            Globals.playing_status = PlayStatus.STARTED
            self.button_start["text"] = "Pause"
            self.button_stop["state"] = "enabled"
            self.window.geometry("284x120")
            check_globals_thread = Thread(target=self.check_globals)
            check_globals_thread.setDaemon(True)
            check_globals_thread.start()
            pipeline_thread = Thread(target=Pipeline.start)
            pipeline_thread.setDaemon(True)
            pipeline_thread.start()
        elif self.button_start["text"] == "Pause":
            Globals.label_status = "Current task is being paused..."
            Globals.playing_status = PlayStatus.PAUSED
            self.button_start["text"] = "Resume"
        elif self.button_start["text"] == "Resume":
            Globals.label_status = "Current task is being resumed..."
            Globals.playing_status = PlayStatus.RESUMED
            self.button_start["text"] = "Pause"
        else:
            Globals.playing_status = PlayStatus.NOT_STARTED
            self.button_start["text"] = "Start"

    def button_stop_onclick(self):
        Globals.label_status = "Current task is being stopped..."
        Globals.playing_status = PlayStatus.STOPPED
        self.button_start["state"] = "disabled"
        self.button_stop["state"] = "disabled"


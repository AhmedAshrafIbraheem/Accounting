import tkinter as tk
import tkinter.font as tf
import accessories.Calendar2 as Calendar
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB
import datetime
import time


class CalendarImp(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.date, fg=Acc.white,
                                command=self.dateWindow, bg=Acc.green, font=self.font)
        self.configureParts()

        self.top = tk.Toplevel()
        self.top.destroy()
        self.calendar = None
        self.okButton = None
        self.choosenTime = None

    def configureParts(self):
        self.button.grid(row=0, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def dateWindow(self):
        self.top.destroy()
        self.top = tk.Toplevel()
        self.top.title(Acc.date)
        self.calendar = Calendar.Calendar(master=self.top, firstweekday=Calendar.calendar.SATURDAY)
        self.okButton = tk.Button(self.top, font=self.font, text=Acc.ok,
                                  command=self.get_time, bg=Acc.green)
        self.configureDateWindow()

    def configureDateWindow(self):
        self.calendar.grid(row=0, column=0, sticky="news")
        self.okButton.grid(row=1, column=0, sticky="news")

        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)
        self.top.resizable(width=False, height=False)

    def get_time(self):
        if self.calendar._selection is not None:
            self.choosenTime = self.calendar.datetime(self.calendar._date.year,
                                                      self.calendar._date.month, int(self.calendar._selection[0]))
            self.button['text'] = self.choosenTime.ctime()
        self.top.destroy()

    def getTimeValue(self):
        return self.choosenTime.ctime()

    def check(self):
        if self.choosenTime is None:
            MB.timeNotChoosen()
            return False
        if self.choosenTime > datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"):
            MB.futureDate()
            return False
        return True

    def clear(self):
        self.button['text'] = Acc.date
        self.choosenTime = None

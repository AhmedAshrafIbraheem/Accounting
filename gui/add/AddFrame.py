import tkinter as tk
import control.Controller as Con
import gui.add.AddButtons as AB


class AddFrame(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.addButtons = AB.AddButtons(self, self.controller)

        self.configureParts()

    def configureParts(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.addButtons.view()

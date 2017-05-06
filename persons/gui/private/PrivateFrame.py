import tkinter as tk
import tkinter.font as tf
import accessories.Accessories as Acc
import control.Controller as Con
import gui.private.PrivateButtons as Pri


class PrivateFrame(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.configureFrame()

        self.font = tf.Font(family='Helvetica', size=15, weight='bold')
        self.passwordEntryFrame = tk.Frame(self, bg=Acc.gray)
        self.entry = tk.Entry(self.passwordEntryFrame, show=Acc.passwordSymbol, font=self.font, justify='center')
        self.entry.bind(Acc.enterKey, self.check)
        self.label = tk.Label(self.passwordEntryFrame, text=Acc.password, bg=Acc.green, font=self.font)
        self.button = tk.Button(self.passwordEntryFrame, relief=tk.GROOVE, text=Acc.ok,
                                command=self.check, bg=Acc.green, font=self.font)
        self.configurePasswordEntry()

        self.privateButtons = Pri.PrivateButtons(self, self.controller)

    def check(self, event=None):
        if self.controller.checkPassword(self.entry.get()):
            self.removePasswordEntry()
            self.privateButtons.view()
        else:
            self.entry.delete(0, 'end')
            self.entry.focus_set()

    def configureFrame(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def configurePasswordEntry(self):
        self.passwordEntryFrame.grid(sticky="news")
        self.entry.grid(row=0, column=1, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=0, column=2, sticky="ew")
        self.button.grid(row=0, column=0, sticky="ew")

        self.passwordEntryFrame.rowconfigure(0, weight=1)
        self.passwordEntryFrame.columnconfigure(0, weight=3)
        self.passwordEntryFrame.columnconfigure(1, weight=5)
        self.passwordEntryFrame.columnconfigure(2, weight=1)

    def removePasswordEntry(self):
        self.passwordEntryFrame.destroy()

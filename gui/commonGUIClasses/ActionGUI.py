import tkinter as tk
import tkinter.font as tf
import control.Controller as Con
import accessories.Accessories as Acc
import gui.commonGUIClasses.GroupsGUI as Gr
import abc


class ActionGUI(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.groupsFrame = Gr.GroupsGUI(self, self.controller)

        self.areaLabel = tk.Label(self, text=Acc.area, bg=Acc.green, font=self.font, fg=Acc.white)
        self.areaEntry = tk.Entry(self, font=self.font, justify='center')
        self.areaEntry.bind(Acc.enterKey, self.resume)

        self.paidLabel = tk.Label(self, text=Acc.paid, bg=Acc.green, font=self.font, fg=Acc.white)
        self.paidEntry = tk.Entry(self, font=self.font, justify='center')
        self.paidEntry.bind(Acc.enterKey, self.resume)

        self.priceLabel = tk.Label(self, text=Acc.price, bg=Acc.green, font=self.font, fg=Acc.white)
        self.priceEntry = tk.Entry(self, font=self.font, justify='center')
        self.priceEntry.bind(Acc.enterKey, self.resume)

        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)

    @abc.abstractmethod
    def resume(self, event=None):
        ''' checks input, if true operation is done. '''

    def check(self):
        if not self.groupsFrame.check():
            return False
        if not self.controller.testAction(self.areaEntry.get(), self.paidEntry.get(), self.priceEntry.get()):
            return False
        return True

    def configureParts(self):
        self.groupsFrame.grid(row=1, column=0, columnspan=2, sticky="news")

        self.areaEntry.grid(row=2, column=0, sticky="ew")
        self.paidEntry.grid(row=3, column=0, sticky="ew")
        self.priceEntry.grid(row=4, column=0, sticky="ew")

        self.areaLabel.grid(row=2, column=1, sticky="ew")
        self.paidLabel.grid(row=3, column=1, sticky="ew")
        self.priceLabel.grid(row=4, column=1, sticky="ew")

        self.button.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

        for i in range(6):
            self.rowconfigure(i, weight=1)

    def getArea(self):
        return self.areaEntry.get().strip()

    def getPaid(self):
        return self.paidEntry.get().strip()

    def getPrice(self):
        return self.priceEntry.get().strip()

    def clear(self):
        self.areaEntry.delete(0, 'end')
        self.paidEntry.delete(0, 'end')
        self.priceEntry.delete(0, 'end')
        self.groupsFrame.clear()

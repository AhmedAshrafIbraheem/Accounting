import tkinter as tk
import tkinter.font as tf
import control.Controller as Con
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB
import gui.commonGUIClasses.GroupsGUI as Gr


class UpdateStore(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.groupsFrame = Gr.GroupsGUI(self, self.controller)

        self.areaLabel = tk.Label(self, text=Acc.area, bg=Acc.green, font=self.font, fg=Acc.white)
        self.areaEntry = tk.Entry(self, font=self.font, justify='center')
        self.areaEntry.bind(Acc.enterKey, self.resume)

        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts()

    def resume(self, event=None):
        if self.check():
            if MB.confirmation():
                self.groupsFrame.setArea(self.getArea())
                self.clear()

    def check(self):
        if not self.groupsFrame.check():
            return False
        if not self.groupsFrame.checkArea(self.getArea()):
            return False
        return True

    def configureParts(self):
        self.groupsFrame.grid(row=0, column=0, columnspan=2, sticky="news")

        self.areaEntry.grid(row=1, column=0, sticky="ew")
        self.areaLabel.grid(row=1, column=1, sticky="ew")

        self.button.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

        for i in range(3):
            self.rowconfigure(i, weight=1)

    def getArea(self):
        return self.areaEntry.get().strip()

    def clear(self):
        self.areaEntry.delete(0, 'end')
        self.groupsFrame.clear()

import control.Controller as Con
import gui.commonGUIClasses.GroupsGUI as Gr
import tkinter as tk
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class RedundantFrame(Gr.GroupsGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Gr.GroupsGUI.__init__(self, master, controller, *args, **kwargs)

        self.areaLabel = tk.Label(self, text="الهالك", bg=Acc.green, font=self.font, fg=Acc.white)
        self.areaEntry = tk.Entry(self, font=self.font, justify='center')
        self.areaEntry.bind(Acc.enterKey, self.resume)

        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts2()

    def fillKindMenu(self):
        kinds = self.choosenSub.sons
        for i in range(kinds.__len__()):
            self.kindMenu.add_radiobutton(label=kinds[i].getNameAreaString(), variable=self.kindVar,
                                          value=i, indicatoron=0, command=self.kindFunction)

    def kindFunction(self):
        self.choosenKind = self.choosenSub.sons[self.kindVar.get()]
        self.kindMB.config(text=self.choosenKind.getNameAreaString())

    def configureParts2(self):
        self.areaEntry.grid(row=3, column=0, sticky="ew")
        self.areaLabel.grid(row=3, column=1, sticky="ew")

        self.button.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

    def check(self):
        if super().check():
            if self.choosenKind.checkArea(self.areaEntry.get().strip()):
                return True
        return False

    def clear(self):
        super().clear()
        self.areaEntry.delete(0, 'end')

    def resume(self, event=None):
        if self.check():
            if MB.confirmation():
                self.choosenKind.updateArea(-1 * float(self.areaEntry.get().strip()))
                self.clear()
import tkinter as tk
import tkinter.font as tf
import accessories.Accessories as Acc
import control.Controller as Con
import accessories.MessageBoxes as MB


class GroupsGUI(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.font = tf.Font(family='Helvetica', size=18, weight='bold')
        self.lightFont = tf.Font(family='Helvetica', size=15, weight='bold')

        self.mainLabel = tk.Label(self, text=Acc.mainGroup, font=self.font)
        self.mainGroupMB = tk.Menubutton(self, text=Acc.chooseMainGroup, font=self.font, bg=Acc.black, fg=Acc.white)
        self.mainGroupMenu = tk.Menu(self.mainGroupMB, tearoff=0, font=self.lightFont)
        self.mainGroupMB.config(menu=self.mainGroupMenu)
        self.mainGroupVar = tk.IntVar()

        self.subLabel = tk.Label(self, text=Acc.subGroup, font=self.font)
        self.subGroupMB = tk.Menubutton(self, text=Acc.chooseSubGroup, font=self.font, bg=Acc.black, fg=Acc.white)
        self.subGroupMenu = tk.Menu(self.subGroupMB, tearoff=0, font=self.lightFont)
        self.subGroupMB.config(menu=self.subGroupMenu)
        self.subGroupVar = tk.IntVar()

        self.kindLabel = tk.Label(self, text=Acc.kind, font=self.font)
        self.kindMB = tk.Menubutton(self, text=Acc.chooseKind, font=self.font, bg=Acc.black, fg=Acc.white)
        self.kindMenu = tk.Menu(self.kindMB, tearoff=0, font=self.lightFont)
        self.kindMB.config(menu=self.kindMenu)
        self.kindVar = tk.IntVar()

        self.choosenMain = None
        self.choosenSub = None
        self.choosenKind = None

        self.fillMainMenu()

        self.configureParts()

    def fillMainMenu(self):
        mainGroups = self.controller.getMenuGroups()
        for i in range(mainGroups.__len__()):
            self.mainGroupMenu.add_radiobutton(label=mainGroups[i].name, variable=self.mainGroupVar,
                                               value=i, indicatoron=0, command=self.mainGroupFunction)

    def fillSubMenu(self):
        subGroups = self.choosenMain.sons
        for i in range(subGroups.__len__()):
            self.subGroupMenu.add_radiobutton(label=subGroups[i].name, variable=self.subGroupVar,
                                              value=i, indicatoron=0, command=self.subGroupFunction)

    def fillKindMenu(self):
        kinds = self.choosenSub.sons
        for i in range(kinds.__len__()):
            self.kindMenu.add_radiobutton(label=kinds[i].name, variable=self.kindVar,
                                          value=i, indicatoron=0, command=self.kindFunction)

    def mainGroupFunction(self):
        self.choosenMain = self.controller.getMenuGroups()[self.mainGroupVar.get()]
        self.mainGroupMB.config(text=self.choosenMain.name)
        self.clearSub()
        self.clearKind()
        self.fillSubMenu()

    def subGroupFunction(self):
        self.choosenSub = self.choosenMain.sons[self.subGroupVar.get()]
        self.subGroupMB.config(text=self.choosenSub.name)
        self.clearKind()
        self.fillKindMenu()

    def kindFunction(self):
        self.choosenKind = self.choosenSub.sons[self.kindVar.get()]
        self.kindMB.config(text=self.choosenKind.name)

    def clearSub(self):
        if self.subGroupMenu.index('end') is not None:
            for i in range(self.subGroupMenu.index('end') + 1):
                self.subGroupMenu.delete(0)
        self.subGroupMB.config(text=Acc.chooseSubGroup)
        self.choosenSub = None

    def clearKind(self):
        if self.kindMenu.index('end') is not None:
            for i in range(self.kindMenu.index('end') + 1):
                self.kindMenu.delete(0)
        self.kindMB.config(text=Acc.chooseKind)
        self.choosenKind = None

    def configureParts(self):
        self.mainGroupMB.grid(row=0, column=0, sticky="ew")
        self.mainLabel.grid(row=0, column=1, sticky="ew")

        self.subGroupMB.grid(row=1, column=0, sticky="ew")
        self.subLabel.grid(row=1, column=1, sticky="ew")

        self.kindMB.grid(row=2, column=0, sticky="ew")
        self.kindLabel.grid(row=2, column=1, sticky="ew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

    def check(self):
        if self.mainGroupMB.cget('text') == Acc.chooseMainGroup:
            MB.mainGroupNotChosen()
            return False
        if self.subGroupMB.cget('text') == Acc.chooseSubGroup:
            MB.subGroupNotChosen()
            return False
        if self.kindMB.cget('text') == Acc.chooseKind:
            MB.kindNotChosen()
            return False
        return True

    def checkEnoughArea(self, area):
        return self.choosenKind.checkArea(area)

    def checkArea(self, area):
        return self.choosenKind.check(area)

    def setArea(self, area):
        self.choosenKind.setArea(area)

    def updateArea(self, area):
        self.choosenKind.updateArea(area)

    def clear(self):
        self.mainGroupMB.config(text=Acc.chooseMainGroup)
        self.clearSub()
        self.clearKind()

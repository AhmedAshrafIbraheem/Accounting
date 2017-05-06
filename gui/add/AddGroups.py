import tkinter as tk
import tkinter.font as tf
import accessories.Accessories as Acc
import control.Controller as Con
import accessories.MessageBoxes as MB


class MainGroupGUI(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.entry = tk.Entry(self, font=self.font, justify='center')
        self.entry.bind(Acc.enterKey, self.resume)
        self.label = tk.Label(self, text="الاسم", bg=Acc.green, font=self.font)
        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts()

    def configureParts(self):
        self.entry.grid(row=0, column=0, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=0, column=1, sticky="ew")
        self.button.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

    def resume(self, event=None):
        if self.check():
            if self.checkRepeatedNames(self.controller.getMenuGroups()):
                if MB.confirmation():
                    self.controller.addMainGroup(self.entry.get().strip())
                    self.clear()

    def check(self):
        if self.entry.get().strip().__len__() == 0:
            MB.emptyEntry()
            self.entry.focus_set()
            return False
        return True

    def checkRepeatedNames(self, arrayOfObjects):
        name = self.entry.get().strip()
        for obj in arrayOfObjects:
            if obj.name == name:
                MB.repeatedNames()
                return False
        return True

    def clear(self):
        self.entry.delete(0, 'end')


class SubGroupGUI(MainGroupGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        MainGroupGUI.__init__(self, master, controller, *args, **kwargs)

        self.lightFont = tf.Font(family='Helvetica', size=15, weight='bold')

        self.mainLabel = tk.Label(self, text=Acc.mainGroup, font=self.font)
        self.mainGroupMB = tk.Menubutton(self, text=Acc.chooseMainGroup, font=self.font, bg=Acc.black, fg=Acc.white)
        self.mainGroupMenu = tk.Menu(self.mainGroupMB, tearoff=0, font=self.lightFont)
        self.mainGroupMB.config(menu=self.mainGroupMenu)
        self.mainGroupVar = tk.IntVar()
        self.choosenMain = None

        self.fillMainMenu()

        self.configureParts2()

    def fillMainMenu(self):
        mainGroups = self.controller.getMenuGroups()
        for i in range(mainGroups.__len__()):
            self.mainGroupMenu.add_radiobutton(label=mainGroups[i].name, variable=self.mainGroupVar,
                                               value=i, indicatoron=0, command=self.mainGroupFunction)

    def mainGroupFunction(self):
        self.choosenMain = self.controller.getMenuGroups()[self.mainGroupVar.get()]
        self.mainGroupMB.config(text=self.choosenMain.name)

    def configureParts2(self):
        self.entry.grid_forget()
        self.label.grid_forget()
        self.button.grid_forget()

        self.mainGroupMB.grid(row=0, column=0, sticky="ew")
        self.mainLabel.grid(row=0, column=1, sticky="ew")

        self.entry.grid(row=1, column=0, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=1, column=1, sticky="ew")
        self.button.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(2, weight=1)

    def resume(self, event=None):
        if self.check():
            if self.checkRepeatedNames(self.choosenMain.sons):
                if MB.confirmation():
                    self.controller.addSubGroup(self.entry.get().strip(), self.choosenMain)
                    self.clear()

    def check(self):
        if super().check():
            if not (self.mainGroupMB.cget('text') == Acc.chooseMainGroup):
                return True
            MB.mainGroupNotChosen()
        return False

    def clear(self):
        super().clear()
        self.mainGroupMB.config(text=Acc.chooseMainGroup)
        self.choosenMain = None


class KindGUI(SubGroupGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        SubGroupGUI.__init__(self, master, controller, *args, **kwargs)

        self.subLabel = tk.Label(self, text=Acc.subGroup, font=self.font)
        self.subGroupMB = tk.Menubutton(self, text=Acc.chooseSubGroup, font=self.font, bg=Acc.black, fg=Acc.white)
        self.subGroupMenu = tk.Menu(self.subGroupMB, tearoff=0, font=self.lightFont)
        self.subGroupMB.config(menu=self.subGroupMenu)
        self.subGroupVar = tk.IntVar()
        self.choosenSub = None

        self.configureParts3()

    def fillSubMenu(self):
        subGroups = self.choosenMain.sons
        for i in range(subGroups.__len__()):
            self.subGroupMenu.add_radiobutton(label=subGroups[i].name, variable=self.subGroupVar,
                                              value=i, indicatoron=0, command=self.subGroupFunction)

    def mainGroupFunction(self):
        self.choosenMain = self.controller.getMenuGroups()[self.mainGroupVar.get()]
        self.mainGroupMB.config(text=self.choosenMain.name)
        self.clearSub()
        self.fillSubMenu()

    def subGroupFunction(self):
        self.choosenSub = self.choosenMain.sons[self.subGroupVar.get()]
        self.subGroupMB.config(text=self.choosenSub.name)

    def clearSub(self):
        if self.subGroupMenu.index('end') is not None:
            for i in range(self.subGroupMenu.index('end') + 1):
                self.subGroupMenu.delete(0)
        self.subGroupMB.config(text=Acc.chooseSubGroup)
        self.choosenSub = None

    def configureParts3(self):
        self.entry.grid_forget()
        self.label.grid_forget()
        self.button.grid_forget()

        self.subGroupMB.grid(row=1, column=0, sticky="ew")
        self.subLabel.grid(row=1, column=1, sticky="ew")

        self.entry.grid(row=2, column=0, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=2, column=1, sticky="ew")
        self.button.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(3, weight=1)

    def resume(self, event=None):
        if self.check():
            if self.checkRepeatedNames(self.choosenSub.sons):
                if MB.confirmation():
                    self.controller.addKind(self.entry.get().strip(), self.choosenSub)
                    self.clear()

    def check(self):
        if super().check():
            if not (self.subGroupMB.cget('text') == Acc.chooseSubGroup):
                return True
            else:
                MB.subGroupNotChosen()
        return False

    def clear(self):
        super().clear()
        self.clearSub()

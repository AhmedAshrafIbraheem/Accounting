import tkinter as tk
import control.Controller as Con
import accessories.MessageBoxes as MB
import accessories.Accessories as Acc
import abc

import gui.commonGUIClasses.PersonGUI as Per


class CompleteActionGUI(Per.PersonGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Per.PersonGUI.__init__(self, master, controller, *args, **kwargs)

        self.actionLabel = tk.Label(self, text=Acc.action, font=self.font)
        self.actionMB = tk.Menubutton(self, text=Acc.chooseAction, font=self.font, bg=Acc.black, fg=Acc.white)
        self.actionMenu = tk.Menu(self.actionMB, tearoff=0, font=self.lightFont)
        self.actionMB.config(menu=self.actionMenu)
        self.actionVar = tk.IntVar()
        self.choosenAction = None
        self.actions = []

        self.kindLabel = tk.Label(self, text=Acc.kind, font=self.font)
        self.kindMB = tk.Menubutton(self, text=Acc.chooseKind, font=self.font, bg=Acc.black, fg=Acc.white)
        self.kindMenu = tk.Menu(self.kindMB, tearoff=0, font=self.lightFont)
        self.kindMB.config(menu=self.kindMenu)
        self.kindVar = tk.IntVar()
        self.choosenkind = None
        self.kinds = []

        self.entry = tk.Entry(self, font=self.font, justify='center')
        self.entry.bind(Acc.enterKey, self.resume)
        self.label = tk.Label(self, text=Acc.paid, bg=Acc.green, font=self.font)
        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)

        self.configureParts2()

    def fillKindMenu(self):
        kindsSet = set()
        actions = self.choosenPerson.actions
        for i in range(actions.__len__()):
            if not actions[i].finished():
                if actions[i].kindIndex not in kindsSet:
                    kindsSet.add(actions[i].kindIndex)
                    self.kinds.append(actions[i].kind)

        for i in range(self.kinds.__len__()):
            self.kindMenu.add_radiobutton(label=self.kinds[i].getString(), variable=self.kindVar,
                                          value=i, indicatoron=0, command=self.kindFunction)

    def fillActionMenu(self):
        actions = self.choosenPerson.actions
        for i in range(actions.__len__()):
            if not actions[i].finished():
                if actions[i].kind is self.choosenkind:
                    self.actions.append(actions[i])

        for i in range(self.actions.__len__()):
            self.actionMenu.add_radiobutton(label=self.actions[i].getString(), variable=self.actionVar,
                                            value=i, indicatoron=0, command=self.actionFunction)

    def kindFunction(self):
        self.choosenkind = self.kinds[self.kindVar.get()]
        self.kindMB.config(text=self.choosenkind.getString())
        self.clearAction()
        self.fillActionMenu()

    def actionFunction(self):
        self.choosenAction = self.actions[self.actionVar.get()]
        self.actionMB.config(text=self.choosenAction.getString())

    def personFunction(self):
        super().personFunction()
        self.clearKind()
        self.clearAction()
        self.fillKindMenu()

    @abc.abstractmethod
    def resume(self, event=None):
        ''' check and if true, operation is done '''

    def configureParts2(self):
        self.kindMB.grid(row=1, column=0, sticky="ew")
        self.kindLabel.grid(row=1, column=1, sticky="ew")
        self.actionMB.grid(row=2, column=0, sticky="ew")
        self.actionLabel.grid(row=2, column=1, sticky="ew")
        self.entry.grid(row=3, column=0, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=3, column=1, sticky="ew")
        self.button.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

    def check(self):
        if super().check():
            if not (self.kindMB.cget('text') == Acc.chooseKind):
                if not (self.actionMB.cget('text') == Acc.chooseAction):
                    if self.choosenAction.checkForComplete(self.entry.get().strip()):
                        return True
                else:
                    MB.actionNotChoosen()
            else:
                MB.kindNotChosen()
        self.entry.focus_set()
        return False

    def clear(self):
        super().clear()
        self.entry.delete(0, 'end')
        self.clearAction()
        self.clearKind()

    def clearAction(self):
        if self.actionMenu.index('end') is not None:
            for i in range(self.actionMenu.index('end') + 1):
                self.actionMenu.delete(0)
        self.actionMB.config(text=Acc.chooseAction)
        self.choosenAction = None
        self.actions = []

    def clearKind(self):
        if self.kindMenu.index('end') is not None:
            for i in range(self.kindMenu.index('end') + 1):
                self.kindMenu.delete(0)
        self.kindMB.config(text=Acc.chooseKind)
        self.choosenkind = None
        self.kinds = []


class CompleteBuyActionGUI(CompleteActionGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        CompleteActionGUI.__init__(self, master, controller, *args, **kwargs)

    def setVars(self, chhoseString=None, normalString=None, persons=None, errorFunction=None):
        super().setVars(Acc.chooseSupplier, Acc.supplier, self.controller.getSuppliers(), MB.supplierNotChosen)

    def resume(self, event=None):
        if self.check():
            if MB.confirmation():
                self.controller.addCompleteBuyAction(self.choosenAction, self.entry.get().strip())
                self.clear()


class CompleteSellActionGUI(CompleteActionGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        CompleteActionGUI.__init__(self, master, controller, *args, **kwargs)

    def setVars(self, chhoseString=None, normalString=None, persons=None, errorFunction=None):
        super().setVars(Acc.chooseCustomer, Acc.customer, self.controller.getCustomers(), MB.customerNotChosen)

    def resume(self, event=None):
        if self.check():
            if MB.confirmation():
                self.controller.addCompleteSellAction(self.choosenAction, self.entry.get().strip())
                self.clear()

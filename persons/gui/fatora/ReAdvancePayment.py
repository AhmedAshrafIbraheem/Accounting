import tkinter as tk
import tkinter.font as tf
import control.Controller as Con
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class ReAdvancePayment(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')
        self.lightFont = tf.Font(family='Helvetica', size=15, weight='bold')

        self.mainLabel = tk.Label(self, text=Acc.advancePayment, font=self.font)
        self.mainMB = tk.Menubutton(self, text=Acc.chooseAdvancePayment, font=self.font, bg=Acc.black, fg=Acc.white)
        self.mainMenu = tk.Menu(self.mainMB, tearoff=0, font=self.lightFont)
        self.mainMB.config(menu=self.mainMenu)
        self.mainVar = tk.IntVar()
        self.choosenAdvancePayment = None

        self.entry = tk.Entry(self, font=self.font, justify='center')
        self.entry.bind(Acc.enterKey, self.resume)
        self.label = tk.Label(self, text=Acc.money, bg=Acc.green, font=self.font)
        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts()
        self.fillMenu()

    def fillMenu(self):
        advancePayments = self.controller.getAdvancePayments()
        for i in range(advancePayments.__len__()):
            if not advancePayments[i].finished():
                self.mainMenu.add_radiobutton(label=advancePayments[i].getString(), variable=self.mainVar,
                                              value=i, indicatoron=0, command=self.mainFunction)

    def mainFunction(self):
        self.choosenAdvancePayment = self.controller.getAdvancePayments()[self.mainVar.get()]
        self.mainMB.config(text=self.choosenAdvancePayment.getString())

    def menuClear(self):
        if self.mainMenu.index('end') is not None:
            for i in range(self.mainMenu.index('end') + 1):
                self.mainMenu.delete(0)
        self.mainMB.config(text=Acc.chooseAdvancePayment)
        self.choosenAdvancePayment = None

    def configureParts(self):
        self.mainMB.grid(row=0, column=0, sticky="ew")
        self.mainLabel.grid(row=0, column=1, sticky="ew")

        self.entry.grid(row=1, column=0, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=1, column=1, sticky="ew")
        self.button.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

    def resume(self, event=None):
        if self.check():
                if MB.confirmation():
                    self.controller.reAdvancePayment(self.entry.get().strip(), self.choosenAdvancePayment)
                    self.clear()

    def check(self):
        if not (self.mainMB.cget('text') == Acc.chooseAdvancePayment):
            if self.choosenAdvancePayment.checkPaid(self.entry.get().strip()):
                if self.controller.checkEnoughMoney(self.entry.get().strip()):
                    return True
        else:
            MB.advancePaymentNotChosen()
        self.entry.focus_set()
        return False

    def clear(self):
        self.entry.delete(0, 'end')
        self.menuClear()
        self.fillMenu()

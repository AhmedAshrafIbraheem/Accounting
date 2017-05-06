import tkinter as tk
import tkinter.font as tf
import control.Controller as Con
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB
import abc


class MoneyExchangeGUI(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.nameEntry = tk.Entry(self, font=self.font, justify='center')
        self.nameEntry.bind(Acc.enterKey, self.resume)
        self.nameLabel = tk.Label(self, text=Acc.action, bg=Acc.green, font=self.font)

        self.moneyEntry = tk.Entry(self, font=self.font, justify='center')
        self.moneyEntry.bind(Acc.enterKey, self.resume)
        self.moneyLabel = tk.Label(self, text=Acc.money, bg=Acc.green, font=self.font)

        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts()

    def configureParts(self):
        self.nameEntry.grid(row=0, column=0, sticky="ew")
        self.nameEntry.focus_set()
        self.nameLabel.grid(row=0, column=1, sticky="ew")

        self.moneyEntry.grid(row=1, column=0, sticky="ew")
        self.moneyLabel.grid(row=1, column=1, sticky="ew")

        self.button.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

    @abc.abstractmethod
    def resume(self, event=None):
        ''' checks input, if true operation is done.'''

    def check(self):
        if self.nameEntry.get().strip().__len__() == 0:
            MB.emptyEntry()
            return False
        if self.controller.testExchange(self.moneyEntry.get().strip()):
            return True
        self.nameEntry.focus_set()
        return False

    def clear(self):
        self.nameEntry.delete(0, 'end')
        self.moneyEntry.delete(0, 'end')


class PaymentGUI(MoneyExchangeGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        MoneyExchangeGUI.__init__(self, master, controller, *args, **kwargs)

    def resume(self, event=None):
        if self.check():
            if self.controller.checkEnoughMoney(self.moneyEntry.get().strip()):
                if MB.confirmation():
                    self.controller.addPayment(self.nameEntry.get().strip(), self.moneyEntry.get().strip())
                    self.clear()


class AdvancePaymentGUI(MoneyExchangeGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        MoneyExchangeGUI.__init__(self, master, controller, *args, **kwargs)

    def resume(self, event=None):
        if self.check():
            if self.controller.checkMoney(self.moneyEntry.get().strip()):
                if MB.confirmation():
                    self.controller.addAdvancePayment(self.nameEntry.get().strip(), self.moneyEntry.get().strip())
                    self.clear()

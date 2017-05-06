import tkinter as tk
import tkinter.font as tf
import accessories.Accessories as Acc
import control.Controller as Con
import accessories.MessageBoxes as MB
import abc


class AddPersonGUI(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.nameEntry = tk.Entry(self, font=self.font, justify='center')
        self.nameEntry.bind(Acc.enterKey, self.resume)
        self.nameLabel = tk.Label(self, text="الاسم", bg=Acc.green, font=self.font)

        self.numberEntry = tk.Entry(self, font=self.font, justify='center')
        self.numberEntry.bind(Acc.enterKey, self.resume)
        self.numberLabel = tk.Label(self, text="التليفون", bg=Acc.green, font=self.font)

        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts()

    def configureParts(self):
        self.nameEntry.grid(row=0, column=0, sticky="ew")
        self.nameEntry.focus_set()
        self.nameLabel.grid(row=0, column=1, sticky="ew")

        self.numberEntry.grid(row=1, column=0, sticky="ew")
        self.numberLabel.grid(row=1, column=1, sticky="ew")

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
        if self.nameEntry.get().strip().__len__() == 0 or self.numberEntry.get().strip().__len__() == 0:
            MB.emptyEntry()
            self.nameEntry.focus_set()
            return False
        return True

    def checkRepeatedNames(self, arrayOfObjects):
        name = self.nameEntry.get().strip()
        for obj in arrayOfObjects:
            if obj.name == name:
                MB.repeatedNames()
                return False
        return True

    def clear(self):
        self.nameEntry.delete(0, 'end')
        self.numberEntry.delete(0, 'end')


class AddSupplierGUI(AddPersonGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        AddPersonGUI.__init__(self, master, controller, *args, **kwargs)

    def resume(self, event=None):
        if self.check():
            if self.checkRepeatedNames(self.controller.getSuppliers()):
                if MB.confirmation():
                    self.controller.addSupplier(self.nameEntry.get().strip(), self.numberEntry.get().strip())
                    self.clear()


class AddCustomerGUI(AddPersonGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        AddPersonGUI.__init__(self, master, controller, *args, **kwargs)

    def resume(self, event=None):
        if self.check():
            if self.checkRepeatedNames(self.controller.getSuppliers()):
                if MB.confirmation():
                    self.controller.addCustomer(self.nameEntry.get().strip(), self.numberEntry.get().strip())
                    self.clear()

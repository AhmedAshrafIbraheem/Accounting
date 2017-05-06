import tkinter as tk
import tkinter.font as tf
import control.Controller as Con
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class PersonGUI(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')
        self.lightFont = tf.Font(family='Helvetica', size=15, weight='bold')

        self.personLabel = tk.Label(self, font=self.font)
        self.personMB = tk.Menubutton(self, font=self.font, bg=Acc.black, fg=Acc.white)
        self.personMenu = tk.Menu(self.personMB, tearoff=0, font=self.lightFont)
        self.personMB.config(menu=self.personMenu)
        self.personVar = tk.IntVar()
        self.choosenPerson = None

        self.persons = None
        self.chooseString = None
        self.errorFunction = None

        self.setVars()
        self.fillPersonMenu()
        self.configureParts()

    def setVars(self, chhoseString=None, normalString=None, persons=None, errorFunction=None):
        self.chooseString = chhoseString
        self.persons = persons
        self.personMB.config(text=self.chooseString)
        self.personLabel.config(text=normalString)
        self.errorFunction = errorFunction

    def check(self):
        if self.personMB.cget('text') == self.chooseString:
            self.errorFunction()
            return False
        return True

    def fillPersonMenu(self):
        for i in range(self.persons.__len__()):
            self.personMenu.add_radiobutton(label=self.persons[i].name, variable=self.personVar,
                                            value=i, indicatoron=0, command=self.personFunction)

    def personFunction(self):
        self.choosenPerson = self.persons[self.personVar.get()]
        self.personMB.config(text=self.choosenPerson.name)

    def configureParts(self):
        self.personMB.grid(row=0, column=0, sticky="ew")
        self.personLabel.grid(row=0, column=1, sticky="ew")

        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

    def clear(self):
        self.personMB.config(text=self.chooseString)
        self.choosenPerson = None


class SupplierGUI(PersonGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        PersonGUI.__init__(self, master, controller, *args, **kwargs)

    def setVars(self, chhoseString=None, normalString=None, persons=None, errorFunction=None):
        super().setVars(Acc.chooseSupplier, Acc.supplier, self.controller.getSuppliers(), MB.supplierNotChosen)


class CustomerGUI(PersonGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        PersonGUI.__init__(self, master, controller, *args, **kwargs)

    def setVars(self, chhoseString=None, normalString=None, persons=None, errorFunction=None):
        super().setVars(Acc.chooseCustomer, Acc.customer, self.controller.getCustomers(), MB.customerNotChosen)

import tkinter as tk
import control.Controller as Con
import gui.commonGUIClasses.WithBackFrame as Abs
import accessories.Accessories as Acc
import gui.view.ViewSuperClass as VSC


class ViewButtons(Abs.WithBackFrame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Abs.WithBackFrame.__init__(self, master, *args, **kwargs)

        self.controller = controller

        self.viewSuppliers = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                       text="عرض الموردين", command=self.viewSupplierTree)
        self.viewCustomers = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                       text="عرض العملاء", command=self.viewCustomerTree)
        self.configureButtons()

    def configureButtons(self):
        self.viewSuppliers.grid(row=0, column=0, sticky="news")
        self.viewCustomers.grid(row=1, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        for i in range(2):
            self.rowconfigure(i, weight=1)

    def viewSupplierTree(self):
        self.anyButtonClicked()
        VSC.ViewSuperClass(self.replacer, self.controller.getSupplierTreeNames(),
                           self.controller.getSuppliersValues()).grid(row=1, column=0, sticky="news")

    def viewCustomerTree(self):
        self.anyButtonClicked()
        VSC.ViewSuperClass(self.replacer, self.controller.getCustomerTreeNames(),
                           self.controller.getCustomersValues()).grid(row=1, column=0, sticky="news")

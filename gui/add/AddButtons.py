import tkinter as tk
import control.Controller as Con
import gui.commonGUIClasses.WithBackFrame as Abs
import accessories.Accessories as Acc
import gui.add.AddGroups as Gr
import gui.add.AddPersons as Per


class AddButtons(Abs.WithBackFrame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Abs.WithBackFrame.__init__(self, master, *args, **kwargs)

        self.controller = controller

        self.mainButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                    text="إضافة مجموعة رئيسية", command=self.viewMainFrame)
        self.subButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                   text="إضافة مجموعة فرعية", command=self.viewSubFrame)
        self.kindButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                    text="إضافة صنف", command=self.viewKindFrame)
        self.supplierButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                        text="إضافة مورد", command=self.viewSupplierFrame)
        self.customerButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                        text="إضافة عميل", command=self.viewCustomerFrame)
        self.configureButtons()

    def configureButtons(self):
        self.mainButton.grid(row=0, column=0, sticky="news")
        self.subButton.grid(row=1, column=0, sticky="news")
        self.kindButton.grid(row=2, column=0, sticky="news")
        self.supplierButton.grid(row=3, column=0, sticky="news")
        self.customerButton.grid(row=4, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        for i in range(5):
            self.rowconfigure(i, weight=1)

    def viewMainFrame(self):
        self.anyButtonClicked()
        Gr.MainGroupGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewSubFrame(self):
        self.anyButtonClicked()
        Gr.SubGroupGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewKindFrame(self):
        self.anyButtonClicked()
        Gr.KindGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewSupplierFrame(self):
        self.anyButtonClicked()
        Per.AddSupplierGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewCustomerFrame(self):
        self.anyButtonClicked()
        Per.AddCustomerGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

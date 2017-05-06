import tkinter as tk
import accessories.Accessories as Acc
import control.Controller as Con
import gui.commonGUIClasses.WithBackFrame as Abs
import gui.private.MoneyPasswordFrames as MPF
import gui.private.OldBuyAction as OBA
import gui.private.OldSellAction as OSA
import gui.private.UpdateStore as US


class PrivateButtons(Abs.WithBackFrame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Abs.WithBackFrame.__init__(self, master, *args, **kwargs)

        self.controller = controller

        self.viewMoneyButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                         text="عرض المبلغ الموجود بالخزينة", command=self.viewViewMoneyFrame)
        self.updateMoneyButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                           text="تعديل المبلغ الموجود بالخزينة", command=self.viewUpdateMoneyFrame)
        self.updatePasswordButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                              text="تعديل كلمة السر", command=self.viewUpdatePasswordFrame)
        self.oldSellActionButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                             text="عملية بيع بتاريخ قديم", command=self.viewOldBuyActionFrame)
        self.oldBuyActionButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                            text="عملية شراء بتاريخ قديم", command=self.viewOldSellActionFrame)
        self.storeAmountsButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                            text="تعديل الكميات الموجودة بالمخازن", command=self.viewStoreAmountsFrame)
        self.configureButtons()

    def configureButtons(self):
        self.viewMoneyButton.grid(row=0, column=0, sticky="news")
        self.updateMoneyButton.grid(row=1, column=0, sticky="news")
        self.updatePasswordButton.grid(row=2, column=0, sticky="news")
        self.oldSellActionButton.grid(row=3, column=0, sticky="news")
        self.oldBuyActionButton.grid(row=4, column=0, sticky="news")
        self.storeAmountsButton.grid(row=5, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)

    def viewViewMoneyFrame(self):
        self.anyButtonClicked()
        MPF.ViewMoneyFrame(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewUpdateMoneyFrame(self):
        self.anyButtonClicked()
        MPF.UpdateMoneyFrame(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewUpdatePasswordFrame(self):
        self.anyButtonClicked()
        MPF.UpdatePasswordFrame(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewStoreAmountsFrame(self):
        self.anyButtonClicked()
        US.UpdateStore(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewOldSellActionFrame(self):
        self.anyButtonClicked()
        OSA.OldSellAction(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewOldBuyActionFrame(self):
        self.anyButtonClicked()
        OBA.OldBuyAction(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

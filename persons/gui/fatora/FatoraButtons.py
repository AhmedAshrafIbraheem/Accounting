import tkinter as tk
import gui.commonGUIClasses.WithBackFrame as Abs
import accessories.Accessories as Acc
import control.Controller as Con
import gui.fatora.BuyAction as Buy
import gui.fatora.SellAction as Sell
import gui.fatora.CompleteActionGUI as CA
import gui.fatora.MoneyExchangeGUI as Mo
import gui.fatora.ReAdvancePayment as RAP
import gui.fatora.RedundantFrame as RF


class FatoraButtons(Abs.WithBackFrame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Abs.WithBackFrame.__init__(self, master, *args, **kwargs)

        self.controller = controller

        self.buyButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                   text="عملية شراء", command=self.viewBuyFrame)
        self.sellButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                    text="عملية بيع", command=self.viewSellFrame)
        self.completeBuyButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                           text="تكملة عملية شراء", command=self.viewCompleteBuyFrame)
        self.completeSellButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                            text="تكملة عملية بيع", command=self.viewCompleteSellFrame)
        self.paymentButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                       text="مصروفات", command=self.viewPaymentFrame)
        self.advancePaymentButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                              text="سلفة", command=self.viewAdvancePaymentFrame)
        self.reAdvancePaymentButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                                text="رد سلفة", command=self.viewReAdvancePaymentFrame)
        self.redundantButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                         text="هالك", command=self.viewRedundantFrame)

        self.configureButtons()

    def configureButtons(self):
        self.buyButton.grid(row=0, column=0, sticky="news")
        self.sellButton.grid(row=1, column=0, sticky="news")
        self.completeBuyButton.grid(row=2, column=0, sticky="news")
        self.completeSellButton.grid(row=3, column=0, sticky="news")
        self.paymentButton.grid(row=4, column=0, sticky="news")
        self.advancePaymentButton.grid(row=5, column=0, sticky="news")
        self.reAdvancePaymentButton.grid(row=6, column=0, sticky="news")
        self.redundantButton.grid(row=7, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        for i in range(8):
            self.rowconfigure(i, weight=1)

    def viewBuyFrame(self):
        self.anyButtonClicked()
        Buy.BuyAction(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewSellFrame(self):
        self.anyButtonClicked()
        Sell.SellAction(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewCompleteBuyFrame(self):
        self.anyButtonClicked()
        CA.CompleteBuyActionGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewCompleteSellFrame(self):
        self.anyButtonClicked()
        CA.CompleteSellActionGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewPaymentFrame(self):
        self.anyButtonClicked()
        Mo.PaymentGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewAdvancePaymentFrame(self):
        self.anyButtonClicked()
        Mo.AdvancePaymentGUI(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewReAdvancePaymentFrame(self):
        self.anyButtonClicked()
        RAP.ReAdvancePayment(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

    def viewRedundantFrame(self):
        self.anyButtonClicked()
        RF.RedundantFrame(self.replacer, self.controller).grid(row=1, column=0, sticky="news")

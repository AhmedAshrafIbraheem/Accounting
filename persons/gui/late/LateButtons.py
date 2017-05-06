import tkinter as tk
import control.Controller as Con
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB
import gui.commonGUIClasses.WithBackFrame as WB


class LateButtons(WB.WithBackFrame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        WB.WithBackFrame.__init__(self, master, *args, **kwargs)

        self.controller = controller

        self.sellActionLabel = tk.Label(self, text="المبالغ المتاخرة علي العملاء",
                                        fg=Acc.red, font=self.font)
        self.buyActionLabel = tk.Label(self, text="المبالغ المتاخرة عليك للموردين",
                                       fg=Acc.red, font=self.font)
        self.advancePaymentLabel = tk.Label(self, text="المبالغ المتاخرة عليك من السلفات",
                                            fg=Acc.red, font=self.font)
        self.sellButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                    text="عرض", command=self.viewSellActions)
        self.buyButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                   text="عرض", command=self.viewBuyActions)
        self.advancePaymentButton = tk.Button(self, font=self.font, bg=Acc.green, fg=Acc.white,
                                              text="عرض", command=self.viewAdvancePayments)
        self.configureFrames()

    def configureFrames(self):
        self.sellButton.grid(row=0, column=0)
        self.sellActionLabel.grid(row=0, column=1)
        self.buyButton.grid(row=1, column=0)
        self.buyActionLabel.grid(row=1, column=1)
        self.advancePaymentButton.grid(row=2, column=0)
        self.advancePaymentLabel.grid(row=2, column=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        for i in range(3):
            self.rowconfigure(i, weight=1)

    def viewSellActions(self):
        lates = self.controller.getLateSellActions()
        if not lates:
            MB.nothingFound()
        #else:
        #self.configureLabelFrame(self.sellActionFrame, self.sellActionLabel, labels)

    def viewBuyActions(self):
        lates = self.controller.getLateBuyActions()
        if not lates:
            MB.nothingFound()
        #else:
        #self.configureLabelFrame(self.buyActionFrame, self.buyActionLabel, labels)

    def viewAdvancePayments(self):
        lates = self.controller.getLateAdvancePayments()
        if not lates:
            MB.nothingFound()
        #else:
        #self.configureLabelFrame(self.advancePaymentFrame, self.advancePaymentLabel, labels)

    def configureLabelFrame(self, frame: tk.Frame, mainLabel: tk.Label, labels):
        frame.columnconfigure(0, weight=1)
        mainLabel.grid(row=0, columnspan=2, column=1)
        for i in range(labels.__len__()):
            #tk.Label(frame, text=labels[i], font=self.lightFont).grid(row=i+1, column=0, columnspan=2)
            frame.rowconfigure(i, weight=1)
        frame.rowconfigure(labels.__len__(), weight=1)

import tkinter as tk
import tkinter.font as tf

import accessories.Accessories as Acc
import control.Controller as Con
import gui.add.AddFrame as Add
import gui.fatora.FatoraFrame as Fat
import gui.late.LateFrame as LF
import gui.private.PrivateFrame as Pri
import gui.view.ViewFrame as VF


class MainInterface:
    def __init__(self, root, controller: Con.Controller):

        self.parent = root
        self.controller = controller

        self.partsFrame = tk.Frame(self.parent)
        self.lateFrame = LF.LateFrame(self.parent, self.controller)
        self.privateFrame = Pri.PrivateFrame(self.parent, self.controller)
        self.addFrame = Add.AddFrame(self.parent, self.controller)
        self.moneyFrame = Fat.FatoraFrame(self.parent, self.controller)
        self.dataFrame = VF.ViewFrame(self.parent, self.controller)

        self.font = tf.Font(family='Helvetica', size=20, weight='bold')

        self.privateButton = tk.Button(self.partsFrame, font=self.font, bg=Acc.black, relief=tk.GROOVE,
                                       text="خاص", fg=Acc.red, command=lambda: self.viewFrame(self.privateButton))
        self.addButton = tk.Button(self.partsFrame, font=self.font, bg=Acc.black, relief=tk.GROOVE,
                                   text="إضافة", fg=Acc.red, command=lambda: self.viewFrame(self.addButton))
        self.moneyButton = tk.Button(self.partsFrame, font=self.font, bg=Acc.black, relief=tk.GROOVE,
                                     text="فاتورة", fg=Acc.red, command=lambda: self.viewFrame(self.moneyButton))
        self.dataButton = tk.Button(self.partsFrame, font=self.font, bg=Acc.black, relief=tk.GROOVE,
                                    text="المعلومات", fg=Acc.red, command=lambda: self.viewFrame(self.dataButton))

        self.configurePartsFrame()
        self.configureOtherFrames(self.lateFrame)
        self.configureParent()

    def viewFrame(self, button: tk.Button):
        if button.cget('bg') == Acc.black:
            self.colorAll()
            self.forgetAll()
            button.config(bg=Acc.white)
            self.configureOtherFrames(self.getButtonFrame(button))

    def forgetAll(self):
        self.lateFrame.grid_forget()
        self.privateFrame.grid_forget()
        self.addFrame.grid_forget()
        self.moneyFrame.grid_forget()
        self.dataFrame.grid_forget()

    def colorAll(self):
        self.privateButton.config(bg=Acc.black)
        self.addButton.config(bg=Acc.black)
        self.moneyButton.config(bg=Acc.black)
        self.dataButton.config(bg=Acc.black)

    def getButtonFrame(self, button: tk.Button):
        if button == self.privateButton:
            return self.privateFrame
        elif button == self.addButton:
            return self.addFrame
        elif button == self.moneyButton:
            return self.moneyFrame
        return self.dataFrame

    def configurePartsFrame(self):
        self.partsFrame.grid(row=0, column=0, sticky="ew")
        self.privateButton.grid(row=0, column=3, sticky="ew")
        self.addButton.grid(row=0, column=2, sticky="ew")
        self.moneyButton.grid(row=0, column=1, sticky="ew")
        self.dataButton.grid(row=0, column=0, sticky="ew")

        for i in range(4):
            self.partsFrame.columnconfigure(i, weight=1)

    def configureOtherFrames(self, frame: tk.Frame):
        frame.grid(row=1, column=0, sticky="news")

    def configureParent(self):
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=1)

import control.Controller as Con
import accessories.MessageBoxes as MB
import gui.commonGUIClasses.ActionGUI as Act
import gui.commonGUIClasses.PersonGUI as Per


class BuyAction(Act.ActionGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Act.ActionGUI.__init__(self, master, controller, *args, **kwargs)

        self.personFrame = Per.SupplierGUI(self, self.controller)
        self.configureParts()

    def configureParts(self):
        self.personFrame.grid(row=0, column=0, columnspan=2, sticky="news")
        super().configureParts()

    def resume(self, event=None):
        if self.check():
            if MB.confirmation():
                self.controller.addBuyAction(self.personFrame.choosenPerson, self.groupsFrame.choosenKind,
                                             self.getArea(), self.getPaid(), self.getPrice())
                self.clear()

    def check(self):
        if super().check():
            if self.personFrame.check():
                if self.controller.checkEnoughMoney(self.getPaid()):
                    return True
        return False

    def clear(self):
        super().clear()
        self.personFrame.clear()

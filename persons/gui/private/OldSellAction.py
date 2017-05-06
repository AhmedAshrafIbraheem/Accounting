import control.Controller as Con
import accessories.MessageBoxes as MB
import gui.commonGUIClasses.ActionGUI as Act
import gui.commonGUIClasses.PersonGUI as Per
import gui.commonGUIClasses.TimeGUI as Ti


class OldSellAction(Act.ActionGUI):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        Act.ActionGUI.__init__(self, master, controller, *args, **kwargs)

        self.personFrame = Per.CustomerGUI(self, self.controller)
        self.timeFrame = Ti.CalendarImp(self)
        self.configureParts()

    def configureParts(self):
        self.personFrame.grid(row=0, column=0, columnspan=2, sticky="news")
        super().configureParts()
        self.button.grid_forget()
        self.timeFrame.grid(row=5, column=0, columnspan=2, sticky="news")
        self.button.grid(row=6, column=0, columnspan=2, sticky="ew")
        self.rowconfigure(6, weight=1)

    def resume(self, event=None):
        if self.check():
            if MB.confirmation():
                self.controller.addOldSellAction(self.personFrame.choosenPerson, self.groupsFrame.choosenKind,
                                                 self.getArea(), self.getPaid(), self.getPrice(),
                                                 self.timeFrame.getTimeValue())
                self.clear()

    def check(self):
        if super().check():
            if self.personFrame.check() and self.timeFrame.check():
                if self.groupsFrame.checkEnoughArea(self.getArea()):
                    return True
        return False

    def clear(self):
        super().clear()
        self.personFrame.clear()
        self.timeFrame.clear()

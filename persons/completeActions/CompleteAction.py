import actions.Action as Act


class CompleteAction:

    tableParameters = "ActionIndex INT, Paid REAL, Time TEXT"
    columnNames = ["ActionIndex", "Paid", "Time"]

    def __init__(self, action: Act.Action, actionIndex, paid, time):
        self.action = action
        self.action.addSon(self)
        self.actionIndex = actionIndex
        self.paid = paid
        self.time = time

    def updateDad(self):
        self.action.addToPaid(self.paid)

    def getParameterValues(self):
        return [self.actionIndex, self.paid, self.time]

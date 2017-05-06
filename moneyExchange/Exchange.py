import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class Exchange:

    tableParameters = "Name TEXT, Money REAL, Time TEXT"
    columnNames = ["Name", "Money", "Time"]

    def __init__(self, name, money, time):
        self.name = name
        self.money = money
        self.time = time

    def getParamtersValues(self):
        return [self.name, self.money, self.time]

    @staticmethod
    def check(money):
        if not Acc.isNumber(money):
            MB.nonNumberPaid()
            return False
        return True

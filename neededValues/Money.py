import sqlite3
import dealingWithFiles.SqliteFile as SQ
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class Money:

    tableName = "Money"
    tableParameters = "Number REAL"
    columnNames = ["Number"]
    columnToUpdate = "Number"

    def __init__(self, money=0):
        self.money = money

    def getParameterValues(self):
        return [self.money]

    def update(self, money):
        SQ.SqliteClass.update(Money.tableName, Money.tableParameters, Money.columnNames, self.getParameterValues(),
                              Money.columnToUpdate, float(money))
        self.money = money

    def addTo(self, increase):
        self.update(float(self.money) + float(increase))

    def subtractFrom(self, decrease):
        self.update(float(self.money) - float(decrease))

    def check(self, money):
        if not Acc.isNumber(money):
            MB.nonNumberPaid()
            return False
        return True

    def checkEnoughMoney(self, money):
        if self.check(money):
            if float(money) < float(self.money) + Acc.EPS:
                return True
            else:
                MB.notEnoughMoney()
        return False

    def save(self):
        SQ.SqliteClass.save(Money.tableName, Money.tableParameters, self.getParameterValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, Money.tableName, Money.tableParameters)

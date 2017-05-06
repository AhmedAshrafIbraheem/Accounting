import sqlite3
import moneyExchange.Exchange as Ex
import dealingWithFiles.SqliteFile as SQ
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB
import datetime


class AdvancePayment (Ex.Exchange):

    tableName = "AdvancePayments"
    tableParameters = ", Paid REAL"
    columnNames = ["Paid"]
    columnToUpdate = "Paid"

    def __init__(self, name, money, time, paid=0):
        Ex.Exchange.__init__(self, name, money, time)
        self.paid = paid

    def getParamtersValues(self):
        return super().getParamtersValues() + [self.paid]

    def addToPaid(self, paid):
        SQ.SqliteClass.update(AdvancePayment.tableName, Ex.Exchange.tableParameters + AdvancePayment.tableParameters,
                              Ex.Exchange.columnNames + AdvancePayment.columnNames, self.getParamtersValues(),
                              AdvancePayment.columnToUpdate, float(float(self.paid) + float(paid)))
        self.paid = float(float(self.paid) + float(paid))

    def finished(self):
        if self.rest() <= Acc.EPS:
            return True
        return False

    def checkPaid(self, paid):
        if not Acc.isNumber(paid):
            MB.nonNumberPaid()
            return False
        if float(paid) > float(self.rest()) + Acc.EPS:
            MB.paidGreaterThanRest()
            return False
        return True

    def isLate(self, timeAgo):
        if not self.finished():
            if datetime.datetime.strptime(self.time, "%a %b %d %H:%M:%S %Y") < timeAgo:
                return True
        return False

    def save(self):
        SQ.SqliteClass.save(AdvancePayment.tableName, Ex.Exchange.tableParameters + AdvancePayment.tableParameters,
                            self.getParamtersValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, AdvancePayment.tableName,
                                   Ex.Exchange.tableParameters + AdvancePayment.tableParameters)

    def getString(self):
        return (self.nameString() + " ** " + self.priceString() + " ** " + self.paidString() + " ** " +
                self.restString() + " ** " + self.timeString())

    def timeString(self): return str(self.time) + ":" + str("الوقت")

    def restString(self): return str("االمبلغ المتبقي") + ":" + str(self.rest())

    def paidString(self): return str("المبلغ المدفوع") + ":" + str(self.paid)

    def priceString(self): return str("السعر الكلي") + ":" + str(self.money)

    def nameString(self): return str(self.name)

    def rest(self):
        return float(float(self.money) - float(self.paid))

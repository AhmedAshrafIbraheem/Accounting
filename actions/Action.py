import datetime
import groups.Kind as K
import persons.Person as Per
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class Action:

    tableParameters = "PersonIndex INT, KindIndex INT, Area REAL, Paid REAL, Price REAL, Time TEXT"
    columnNames = ["PersonIndex", "KindIndex", "Area", "Paid", "Price", "Time"]
    columnToUpdate = "Paid"

    def __init__(self, person: Per.Person, personIndex, kind: K.Kind, kindIndex, area, paid, price, time):
        self.person = person
        self.personIndex = personIndex
        self.kind = kind
        self.kindIndex = kindIndex
        self.area = area
        self.paid = paid
        self.price = price
        self.time = time
        self.person.addAction(self)
        self.sons = []

    def addSon(self, son):
        self.sons.append(son)

    @staticmethod
    def check(area, paid, price):
        if not Acc.isNumber(area):
            MB.nonNumberArea()
            return False
        if not Acc.isNumber(paid):
            MB.nonNumberPaid()
            return False
        if not Acc.isNumber(price):
            MB.nonNumberPrice()
            return False
        if float(paid) > float(price) + Acc.EPS:
            MB.paidGreaterThanPrice()
            return False
        return True

    def checkForComplete(self, paid):
        if not Acc.isNumber(paid):
            MB.nonNumberPaid()
            return False
        if float(paid) > float(self.rest()) + Acc.EPS:
            MB.paidGreaterThanRest()
            return False
        return True

    def addToPaid(self, paid):
        self.paid = float(float(self.paid) + float(paid))

    def finished(self):
        if self.rest() > Acc.EPS:
            return False
        return True

    def getString(self):
        return (self.areaString() + " ** " + self.priceString() + " ** " + self.paidString() + " ** " +
                self.restString() + " ** " + self.timeString())

    def timeString(self): return str(self.time) + ":" + str("الوقت")

    def restString(self): return str("االمبلغ المتبقي") + ":" + str(self.rest())

    def paidString(self): return str("المبلغ المدفوع") + ":" + str(self.paid)

    def priceString(self): return str("السعر الكلي") + ":" + str(self.price)

    def areaString(self): return str("المساحة") + ":" + str(self.area)

    def rest(self): return float(float(self.price) - float(self.paid))

    def getParameterValues(self): return [self.personIndex, self.kindIndex, self.area, self.paid, self.price, self.time]

    def isLate(self, timeAgo):
        if not self.finished():
            if datetime.datetime.strptime(self.time, "%a %b %d %H:%M:%S %Y") < timeAgo:
                return True
        return False

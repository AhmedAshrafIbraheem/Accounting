import control.Data as Data
import datetime
import time as realTime
import actions.Action as Act
import actions.SellAction as SellAction
import actions.BuyAction as BuyAction
import moneyExchange.Exchange as EX
import groups.MainGroup as MG
import groups.SubGroup as SG
import groups.Kind as K
import persons.Supplier as Sup
import persons.Customer as Cus
import completeActions.CompleteBuyAction as CBA
import completeActions.CompleteSellAction as CSA
import moneyExchange.Payment as Py
import moneyExchange.AdvancePayment as APy


class Controller:
    def __init__(self):
        self.data = Data.Data()

    def getMoneyValue(self):
        return self.data.myMoney.money

    def getSuppliers(self):
        return self.data.suppliers

    def getCustomers(self):
        return self.data.customers

    def getMenuGroups(self):
        return self.data.mainGroups

    def getSellActions(self):
        return self.data.sellActions

    def getBuyActions(self):
        return self.data.buyActions

    def getAdvancePayments(self):
        return self.data.advancePayments

    def getLateSellActions(self):
        timeAgo = self.getTimeAgo()
        lateSellActions = []
        for sellAction in self.data.sellActions:
            if sellAction.isLate(timeAgo):
                lateSellActions.append(sellAction)
        return lateSellActions

    def getLateBuyActions(self):
        timeAgo = self.getTimeAgo()
        lateBuyActions = []
        for buyAction in self.data.buyActions:
            if buyAction.isLate(timeAgo):
                lateBuyActions.append(buyAction)
        return lateBuyActions

    def getLateAdvancePayments(self):
        timeAgo = self.getTimeAgo()
        lateAdvancePayments = []
        for advancePayment in self.data.advancePayments:
            if advancePayment.isLate(timeAgo):
                lateAdvancePayments.append(advancePayment)
        return lateAdvancePayments

    def getTimeAgo(self):
        return datetime.datetime.now() - datetime.timedelta(days=7)

    def checkPassword(self, password):
        return self.data.password.check(password)

    def updatePasswordValue(self, password):
        self.data.password.update(password)

    def checkMoney(self, money):
        return self.data.myMoney.check(money)

    def checkEnoughMoney(self, money):
        return self.data.myMoney.checkEnoughMoney(money)

    def updateMoneyValue(self, money):
        money = str(money).strip()
        if self.checkMoney(money):
            self.data.myMoney.update(money)
            return True
        return False

    def testAction(self, area, paid, price):
        return Act.Action.check(area, paid, price)

    def testExchange(self, paid):
        return EX.Exchange.check(paid)

    def addMainGroup(self, name):
        self.data.addMainGroup(MG.MainCollection(name))

    def addSubGroup(self, name, dad):
        self.data.addSubGroup(SG.SubCollection(name, dad, self.data.mainGroups.index(dad)))

    def addKind(self, name, dad):
        self.data.addKind(K.Kind(name, dad, self.data.subGroups.index(dad)))

    def addSupplier(self, name, number):
        self.data.addSupplier(Sup.Supplier(name, number))

    def addCustomer(self, name, number):
        self.data.addCustomer(Cus.Customer(name, number))

    def addBuyAction(self, person, kind, area, paid, price):
        actionTime = self.getTime()
        obj = BuyAction.BuyAction(person, self.data.suppliers.index(person), kind, self.data.kinds.index(kind),
                                  area, 0, price, actionTime)
        self.data.addBuyAction(obj)
        self.addCompleteBuyAction(obj, paid)

    def addSellAction(self, person, kind, area, paid, price):
        actionTime = self.getTime()
        obj = SellAction.SellAction(person, self.data.customers.index(person), kind, self.data.kinds.index(kind),
                                    area, 0, price, actionTime)
        self.data.addSellAction(obj)
        self.addCompleteSellAction(obj, paid)

    def addOldBuyActions(self, person, kind, area, paid, price, time):
        '''
        :param person:
        :param kind:
        :param area:
        :param paid:
        :param price:
        :param time:
        :return:
        '''
        actionTime = self.getTime(time)

    def addOldSellActions(self, person, kind, area, paid, price, time):
        '''
        :param person:
        :param kind:
        :param area:
        :param paid:
        :param price:
        :param time:
        :return:
        '''
        actionTime = self.getTime(time)

    def addCompleteBuyAction(self, action, paid):
        actionTime = self.getTime()
        self.data.addCompleteBuyAction(
            CBA.CompleteBuyAction(action, self.data.buyActions.index(action), paid, actionTime))

    def addCompleteSellAction(self, action, paid):
        actionTime = self.getTime()
        self.data.addCompleteSellAction(
            CSA.CompleteSellAction(action, self.data.sellActions.index(action), paid, actionTime))

    def addPayment(self, name, money):
        self.data.addPayment(Py.Payment(name, money, self.getTime()))

    def addAdvancePayment(self, name, money):
        self.data.addAdvancePayment(APy.AdvancePayment(name, money, self.getTime()))

    def reAdvancePayment(self, money, advancePayment):
        advancePayment.addToPaid(money)
        self.addPayment(advancePayment.name + " رد سلفة", money)

    def getTime(self, time=None):
        if time is None:
            return realTime.ctime()
        return time

    def getSupplierTreeNames(self):
        return Sup.Supplier.treeNames

    def getCustomerTreeNames(self):
        return Cus.Customer.treeNames

    def getSuppliersValues(self):
        rows = []
        for supplier in self.data.suppliers:
            rows.append(supplier.getParameterValues())
        return rows

    def getCustomersValues(self):
        rows = []
        for customer in self.data.customers:
            rows.append(customer.getParameterValues())
        return rows

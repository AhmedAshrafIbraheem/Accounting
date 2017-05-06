import dealingWithFiles.LoadData as LD
import neededValues.Money as Mo
import neededValues.Password as Pass


class Data:
    def __init__(self):
        self.mainGroups = []
        self.subGroups = []
        self.kinds = []

        self.customers = []
        self.suppliers = []

        self.myMoney = Mo.Money()
        self.password = Pass.Password()

        self.payments = []
        self.advancePayments = []

        self.buyActions = []
        self.sellActions = []

        self.completeBuyActions = []
        self.completeSellActions = []

        self.loadData()

    def addMainGroup(self, obj):
        obj.save()
        self.mainGroups.append(obj)

    def addSubGroup(self, obj):
        obj.save()
        self.subGroups.append(obj)

    def addKind(self, obj):
        obj.save()
        self.kinds.append(obj)

    def addCustomer(self, obj):
        obj.save()
        self.customers.append(obj)

    def addSupplier(self, obj):
        obj.save()
        self.suppliers.append(obj)

    def addPayment(self, obj):
        obj.save()
        self.myMoney.subtractFrom(obj.money)
        self.payments.append(obj)

    def addAdvancePayment(self, obj):
        obj.save()
        self.myMoney.addTo(obj.money)
        self.advancePayments.append(obj)

    def addBuyAction(self, obj):
        obj.save()
        obj.updateKind()
        self.buyActions.append(obj)

    def addSellAction(self, obj):
        obj.save()
        obj.updateKind()
        self.sellActions.append(obj)

    def addCompleteBuyAction(self, obj):
        obj.save()
        obj.updateDad()
        self.myMoney.subtractFrom(obj.paid)
        self.completeBuyActions.append(obj)

    def addCompleteSellAction(self, obj):
        obj.save()
        obj.updateDad()
        self.myMoney.addTo(obj.paid)
        self.completeSellActions.append(obj)

    def loadData(self):
        LD.LoadData.loadMainCollections(self.mainGroups)
        LD.LoadData.loadSubCollections(self.subGroups, self.mainGroups)
        LD.LoadData.loadKinds(self.kinds, self.subGroups)

        LD.LoadData.loadCustomers(self.customers)
        LD.LoadData.loadSuppliers(self.suppliers)

        self.myMoney = LD.LoadData.loadMoney()
        self.password = LD.LoadData.loadPassword()

        LD.LoadData.loadPayments(self.payments)
        LD.LoadData.loadAdvancePayments(self.advancePayments)

        LD.LoadData.loadBuyActions(self.buyActions, self.suppliers, self.kinds)
        LD.LoadData.loadSellActions(self.sellActions, self.customers, self.kinds)

        LD.LoadData.loadCompleteBuyActions(self.completeBuyActions, self.buyActions)
        LD.LoadData.loadCompleteSellActions(self.completeSellActions, self.sellActions)

import sqlite3


class LoadData:

    @staticmethod
    def openConnection():
        return sqlite3.connect('Data.db')

    @staticmethod
    def closeConnection(conn: sqlite3.Connection):
        conn.close()

    @staticmethod
    def loadMainCollections(mainCollections):
        import groups.MainGroup as MC
        conn = LoadData.openConnection()
        for row in MC.MainCollection.load(conn):
            mainCollections.append(MC.MainCollection(row[0]))
        LoadData.closeConnection(conn)

    @staticmethod
    def loadSubCollections(subCollections, mainCollections):
        import groups.SubGroup as SC
        conn = LoadData.openConnection()
        for row in SC.SubCollection.load(conn):
            subCollections.append(SC.SubCollection(row[0], mainCollections[row[1]], row[1]))
        LoadData.closeConnection(conn)

    @staticmethod
    def loadKinds(kinds, subCollections):
        import groups.Kind as K
        conn = LoadData.openConnection()
        for row in K.Kind.load(conn):
            obj = K.Kind(row[0], subCollections[row[1]], row[1], row[2])
            kinds.append(obj)
        LoadData.closeConnection(conn)

    @staticmethod
    def loadCustomers(customers):
        import persons.Customer as Cus
        conn = LoadData.openConnection()
        for row in Cus.Customer.load(conn):
            customers.append(Cus.Customer(row[0], row[1]))
        LoadData.closeConnection(conn)

    @staticmethod
    def loadSuppliers(suppliers):
        import persons.Supplier as Sup
        conn = LoadData.openConnection()
        for row in Sup.Supplier.load(conn):
            suppliers.append(Sup.Supplier(row[0], row[1]))
        LoadData.closeConnection(conn)

    @staticmethod
    def loadMoney():
        import neededValues.Money as Mo
        conn = LoadData.openConnection()
        myMoney = Mo.Money()
        moneyFlag = False
        for row in Mo.Money.load(conn):
            moneyFlag = True
            myMoney = Mo.Money(row[0])
        LoadData.closeConnection(conn)
        if not moneyFlag:
            myMoney.save()
        return myMoney

    @staticmethod
    def loadPassword():
        import neededValues.Password as Pa
        conn = LoadData.openConnection()
        myPassword = Pa.Password()
        passwordFlag = False
        for row in Pa.Password.load(conn):
            passwordFlag = True
            myPassword = Pa.Password(row[0])
        LoadData.closeConnection(conn)
        if not passwordFlag:
            myPassword.save()
        return myPassword

    @staticmethod
    def loadPayments(payments):
        import moneyExchange.Payment as Py
        conn = LoadData.openConnection()
        for row in Py.Payment.load(conn):
            payments.append(Py.Payment(row[0], row[1], row[2]))
        LoadData.closeConnection(conn)

    @staticmethod
    def loadAdvancePayments(advancePayments):
        import moneyExchange.AdvancePayment as APy
        conn = LoadData.openConnection()
        for row in APy.AdvancePayment.load(conn):
            advancePayments.append(APy.AdvancePayment(row[0], row[1], row[2], row[3]))
        LoadData.closeConnection(conn)

    @staticmethod
    def loadBuyActions(buyActions, suppliers, kinds):
        import actions.BuyAction as By
        conn = LoadData.openConnection()
        for row in By.BuyAction.load(conn):
            obj = By.BuyAction(suppliers[row[0]], row[0], kinds[row[1]], row[1],
                               row[2], row[3], row[4], row[5])
            buyActions.append(obj)
        LoadData.closeConnection(conn)

    @staticmethod
    def loadSellActions(sellActions, customers, kinds):
        import actions.SellAction as Se
        conn = LoadData.openConnection()
        for row in Se.SellAction.load(conn):
            obj = Se.SellAction(customers[row[0]], row[0], kinds[row[1]], row[1],
                                row[2], row[3], row[4], row[5])
            sellActions.append(obj)
        LoadData.closeConnection(conn)

    @staticmethod
    def loadCompleteBuyActions(completeBuyActions, buyActions):
        import completeActions.CompleteBuyAction as CBy
        conn = LoadData.openConnection()
        for row in CBy.CompleteBuyAction.load(conn):
            obj = CBy.CompleteBuyAction(buyActions[row[0]], row[0], row[1], row[2])
            completeBuyActions.append(obj)
        LoadData.closeConnection(conn)

    @staticmethod
    def loadCompleteSellActions(completeSellActions, sellActions):
        import completeActions.CompleteSellAction as CSe
        conn = LoadData.openConnection()
        for row in CSe.CompleteSellAction.load(conn):
            obj = CSe.CompleteSellAction(sellActions[row[0]], row[0], row[1], row[2])
            completeSellActions.append(obj)
        LoadData.closeConnection(conn)

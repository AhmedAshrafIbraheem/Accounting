import sqlite3
import moneyExchange.Exchange as Ex
import dealingWithFiles.SqliteFile as SQ


class Payment (Ex.Exchange):

    tableName = "Payments"

    def __init__(self, name, money, time):
        Ex.Exchange.__init__(self, name, money, time)

    def save(self):
        SQ.SqliteClass.save(Payment.tableName, Ex.Exchange.tableParameters, self.getParamtersValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, Payment.tableName, Ex.Exchange.tableParameters)

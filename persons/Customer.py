import sqlite3
import dealingWithFiles.SqliteFile as SQ
import persons.Person as P


class Customer (P.Person):

    tableName = "Customers"
    treeNames = ["اسم العميل", "التليفون"]

    def __init__(self, name, number):
        P.Person.__init__(self, name, number)

    def getString(self, parameter=None):
        return super().getString("العميل")

    def save(self):
        SQ.SqliteClass.save(Customer.tableName, P.Person.tableParameters, self.getParameterValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, Customer.tableName, P.Person.tableParameters)

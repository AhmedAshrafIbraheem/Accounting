import sqlite3
import dealingWithFiles.SqliteFile as SQ
import persons.Person as P


class Supplier (P.Person):

    tableName = "Suppliers"
    treeNames = ["اسم المورد", "التليفون"]

    def __init__(self, name, number):
        P.Person.__init__(self, name, number)

    def getString(self, parameter=None):
        return super().getString("المورد")

    def save(self):
        SQ.SqliteClass.save(Supplier.tableName, P.Person.tableParameters, self.getParameterValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, Supplier.tableName, P.Person.tableParameters)



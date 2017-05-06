import sqlite3
import dealingWithFiles.SqliteFile as SQ
import accessories.MessageBoxes as MB


class Password:

    tableName = "Password"
    tableParameters = "Password TEXT"
    columnNames = ["Password"]
    columnToUpdate = "Password"

    def __init__(self, password="test"):
        self.password = password

    def getParameterValues(self):
        return [self.password]

    def update(self, password):
        SQ.SqliteClass.update(Password.tableName, Password.tableParameters, Password.columnNames,
                              self.getParameterValues(), Password.columnToUpdate, password)
        self.password = password

    def check(self, password):
        if self.password == password:
            return True
        MB.wrongPassword()
        return False

    def save(self):
        SQ.SqliteClass.save(Password.tableName, Password.tableParameters, self.getParameterValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, Password.tableName, Password.tableParameters)

import sqlite3
import dealingWithFiles.SqliteFile as SQ


class MainCollection:

    tableName = "MainCollections"
    tableParameters = "Name TEXT"
    columnNames = ["Name"]

    def __init__(self, name):
        self.name = name
        self.sons = []

    def addSon(self, subCollection):
        self.sons.append(subCollection)

    def getParametersValues(self):
        return [self.name]

    def getString(self):
        return str(str(self.name) + " :" + "المجموعة الرئيسية")

    def remove(self, mainCollections, subCollections, kinds):
        for son in self.sons:
            son.remove(subCollections, kinds)
        mainCollections.remove(self)
        SQ.SqliteClass.remove(MainCollection.tableName, MainCollection.columnNames, self.getParametersValues())

    def save(self):
        SQ.SqliteClass.save(MainCollection.tableName, MainCollection.tableParameters, self.getParametersValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, MainCollection.tableName, MainCollection.tableParameters)

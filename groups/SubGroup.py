import sqlite3
import groups.MainGroup as MC
import dealingWithFiles.SqliteFile as SQ


class SubCollection:

    tableName = "SubCollections"
    tableParameters = "Name TEXT, DadIndex INT"
    columnNames = ["Name", "DadIndex"]

    def __init__(self, name, dad: MC.MainCollection, dadIndex):
        self.name = name
        self.dad = dad
        self.dadIndex = dadIndex
        self.dad.addSon(self)
        self.sons = []

    def addSon(self, kind):
        self.sons.append(kind)

    def getParametersValues(self):
        return [self.name, self.dadIndex]

    def getString(self):
        return str(str(str(self.name) + " :" + "المجموعة الفرعية") + " " + self.dad.getString())

    def remove(self, subCollections, kinds):
        for son in self.sons:
            son.remove(kinds)
        subCollections.remove(self)
        SQ.SqliteClass.remove(SubCollection.tableName, SubCollection.columnNames, self.getParametersValues())

    def save(self):
        SQ.SqliteClass.save(SubCollection.tableName, SubCollection.tableParameters, self.getParametersValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, SubCollection.tableName, SubCollection.tableParameters)

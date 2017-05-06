import sqlite3
import groups.SubGroup as SC
import dealingWithFiles.SqliteFile as SQ
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class Kind:

    tableName = "Kinds"
    tableParameters = "Name TEXT, DadIndex INT, Area REAL"
    columnNames = ["Name", "DadIndex", "Area"]
    columnToUpdate = "Area"

    def __init__(self, name, dad: SC.SubCollection, dadIndex, area=0):
        self.name = name
        self.dad = dad
        self.dad.addSon(self)
        self.dadIndex = dadIndex
        self.area = area

    def getParametersValues(self):
        return [self.name, self.dadIndex, self.area]

    def getString(self):
        return str(str(str(self.name) + " :" + "الصنف") + " " + self.dad.getString())

    def getNameAreaString(self):
        return str(self.name + "**" + str(self.area) + ":" + "المساحة")
    
    def remove(self, kinds):
        kinds.remove(self)
        SQ.SqliteClass.remove(Kind.tableName, Kind.columnNames, self.getParametersValues())

    def save(self):
        SQ.SqliteClass.save(Kind.tableName, Kind.tableParameters, self.getParametersValues())

    def setArea(self, area):
        self.updateArea(float(area) - float(self.area))

    def updateArea(self, area):
        SQ.SqliteClass.update(Kind.tableName, Kind.tableParameters, Kind.columnNames, self.getParametersValues(),
                              Kind.columnToUpdate, float(float(area) + float(self.area)))
        self.area = float(float(area) + float(self.area))

    def check(self, area):
        if not Acc.isNumber(area):
            MB.nonNumberArea()
            return False
        return True

    def checkArea(self, area):
        if self.check(area):
            if float(float(area) - float(self.area)) <= Acc.EPS:
                return True
            MB.notEnoughArea()
        return False

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, Kind.tableName, Kind.tableParameters)

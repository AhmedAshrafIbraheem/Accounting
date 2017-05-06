import sqlite3
import dealingWithFiles.SqliteFile as SQ
import groups.Kind as K
import persons.Person as Per
import actions.Action as Act


class BuyAction (Act.Action):

    tableName = "BuyActions"

    def __init__(self, person: Per.Person, personIndex, kind: K.Kind, kindIndex, area, paid, price, time):
        Act.Action.__init__(self, person, personIndex, kind, kindIndex, area, paid, price, time)

    def save(self):
        SQ.SqliteClass.save(BuyAction.tableName, Act.Action.tableParameters, self.getParameterValues())

    def addToPaid(self, paid):
        SQ.SqliteClass.update(BuyAction.tableName, Act.Action.tableParameters, Act.Action.columnNames,
                              self.getParameterValues(), Act.Action.columnToUpdate,
                              float(float(self.paid) + float(paid)))
        super().addToPaid(paid)

    def updateKind(self):
        self.kind.updateArea(self.area)

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, BuyAction.tableName, Act.Action.tableParameters)

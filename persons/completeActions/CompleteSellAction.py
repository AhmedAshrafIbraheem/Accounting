import sqlite3
import dealingWithFiles.SqliteFile as SQ
import actions.Action as Act
import completeActions.CompleteAction as Com


class CompleteSellAction (Com.CompleteAction):

    tableName = "CompleteSellActions"

    def __init__(self, action: Act.Action, actionIndex, paid, time):
        Com.CompleteAction.__init__(self, action, actionIndex, paid, time)

    def save(self):
        SQ.SqliteClass.save(CompleteSellAction.tableName, Com.CompleteAction.tableParameters, self.getParameterValues())

    @staticmethod
    def load(conn: sqlite3.Connection):
        return SQ.SqliteClass.load(conn, CompleteSellAction.tableName, Com.CompleteAction.tableParameters)

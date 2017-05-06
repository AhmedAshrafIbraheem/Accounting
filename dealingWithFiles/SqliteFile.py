import sqlite3


class SqliteClass:

    @staticmethod
    def openConnection():
        return sqlite3.connect('Data.db')

    @staticmethod
    def closeConnection(conn: sqlite3.Connection):
        conn.close()

    @staticmethod
    def save(tableName, tableParameters, values):
        conn = SqliteClass.openConnection()
        conn.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (" + tableParameters + ")")
        conn.execute("INSERT INTO " + tableName + " VALUES (" +
                     SqliteClass.__getQuestionMarks(values.__len__()) + ")", values)
        conn.commit()
        SqliteClass.closeConnection(conn)

    @staticmethod
    def remove(tableName, columnNames, values):
        conn = SqliteClass.openConnection()
        conn.execute("DELETE FROM " + tableName + "WHERE " +
                     SqliteClass.__oraganizeColumnNames(columnNames), values)
        conn.commit()
        SqliteClass.closeConnection(conn)

    @staticmethod
    def load(conn: sqlite3.Connection, tableName, tableParameters):
        conn.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (" + tableParameters + ")")
        return conn.execute("SELECT * from " + tableName)

    @staticmethod
    def update(tableName, tableParameters, columnNames, values, columnToUpdate, newValue):
        values.insert(0, newValue)
        conn = SqliteClass.openConnection()
        conn.execute("UPDATE " + tableName + " SET " + columnToUpdate + " = ?  WHERE " +
                     SqliteClass.__oraganizeColumnNames(columnNames), values)
        conn.commit()
        SqliteClass.closeConnection(conn)

    @staticmethod
    def __getQuestionMarks(length):
        questionMarks = ""
        for i in range(length):
            questionMarks += "?, "
        questionMarks = questionMarks[:-2]
        return questionMarks

    @staticmethod
    def __oraganizeColumnNames(columnNames):
        organizedColumnNames = ""
        for columnName in columnNames:
            organizedColumnNames += columnName + " = ? AND "
        organizedColumnNames = organizedColumnNames[:-4]
        return organizedColumnNames

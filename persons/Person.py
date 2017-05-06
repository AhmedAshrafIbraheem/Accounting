class Person:

    tableParameters = "Name TEXT, Number TEXT"
    columnNames = ["Name", "Number"]

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.actions = []

    def getParameterValues(self):
        return [self.name, self.number]

    def addAction(self, action):
        self.actions.append(action)

    def getString(self, parameter=None):
        return str(str(self.name) + " :" + parameter)

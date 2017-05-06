import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tf
import accessories.Accessories as Acc


class ViewSuperClass(tk.Frame):
    def __init__(self, master, columnNames, rows, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.font = tf.Font(family='Helvetica', size=18, weight='bold')
        self.columnNames = columnNames
        self.rows = rows

        self.treeView = ttk.Treeview(self)

        self.verticalScrollbar = tk.Scrollbar(self, orient="vertical", command=self.treeView.yview)
        self.horizontalScrollbar = tk.Scrollbar(self, orient="horizontal", command=self.treeView.xview)
        self.treeView.configure(yscrollcommand=self.verticalScrollbar.set, xscrollcommand=self.horizontalScrollbar.set)

        self.style = ttk.Style(self.treeView)
        self.style.configure('Treeview', rowheight=Acc.rowHeight)

        self.createUI()
        self.configureParts()
        self.viewData()

    def createUI(self):
        self.treeView['columns'] = self.columnNames[:self.columnNames.__len__() - 1]
        self.treeView.heading("#0", text=self.columnNames[self.columnNames.__len__() - 1])

        for columnName in self.columnNames[:self.columnNames.__len__() - 1]:
            self.treeView.heading(columnName, text=columnName)
            self.treeView.column(columnName, anchor='center')

    def viewData(self):
        numCols = self.columnNames.__len__()
        flag = True
        for row in self.rows:
            if flag:
                flag = False
                self.treeView.insert('', 'end', text=row[numCols - 1], values=row[:numCols - 1], tags=('tag',))
            else:
                flag = True
                self.treeView.insert('', 'end', text=row[numCols - 1], values=row[:numCols - 1], tags=('tag', 'gray',))
        self.treeView.tag_configure('tag', font=self.font)
        self.treeView.tag_configure('gray', background=Acc.gray)

    def configureParts(self):
        self.treeView.grid(row=0, column=0, sticky="news")
        self.verticalScrollbar.grid(row=0, column=1, sticky='ns')
        self.horizontalScrollbar.grid(row=1, column=0, sticky='ew')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

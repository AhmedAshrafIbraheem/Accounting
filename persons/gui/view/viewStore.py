import gui.view.ViewSuperClass as VSC


class viewStore(VSC.ViewSuperClass):
    def __init__(self, master, columnNames, rows, *args, **kwargs):
        VSC.ViewSuperClass.__init__(self, master, columnNames, rows, *args, **kwargs)

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

'''
    def mainer(self):
        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end') # adds + button

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))
'''
import tkinter as tk
import tkinter.font as tf
import control.Controller as Con
import accessories.Accessories as Acc
import accessories.MessageBoxes as MB


class ViewMoneyFrame(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.font = tf.Font(family='Helvetica', size=30, weight='bold')

        self.label = tk.Label(self, font=self.font,
                              text=str(self.controller.getMoneyValue()) + " :" + "المبلغ الموجود بالخزينة")
        self.configureLabel()

    def configureLabel(self):
        self.label.grid(sticky="news")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class UpdateMoneyFrame(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.font = tf.Font(family='Helvetica', size=18, weight='bold')
        self.entry = tk.Entry(self, font=self.font, justify='center')
        self.entry.bind(Acc.enterKey, self.resume)
        self.label = tk.Label(self, text="المبلغ الموجود بالخزينة", bg=Acc.green, font=self.font)
        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)

        self.configureParts()

    def configureParts(self):
        self.entry.grid(row=0, column=1, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=0, column=2, sticky="ew")
        self.button.grid(row=0, column=0, sticky="ew")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=1)

    def resume(self, event=None):
        if self.controller.updateMoneyValue(self.entry.get()):
            MB.showNewMoney(self.controller.getMoneyValue())
            self.entry.delete(0, 'end')
        else:
            self.entry.focus_set()


class UpdatePasswordFrame(tk.Frame):
    def __init__(self, master, controller: Con.Controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master
        self.controller = controller

        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.entry = tk.Entry(self, font=self.font, show=Acc.passwordSymbol, justify='center')
        self.entry.bind(Acc.enterKey, self.resume)
        self.label = tk.Label(self, text=Acc.newPassword, bg=Acc.green, font=self.font)
        self.button = tk.Button(self, relief=tk.GROOVE, text=Acc.ok,
                                command=self.resume, bg=Acc.green, font=self.font)
        self.configureParts()

    def configureParts(self):
        self.entry.grid(row=0, column=1, sticky="ew")
        self.entry.focus_set()
        self.label.grid(row=0, column=2, sticky="ew")
        self.button.grid(row=0, column=0, sticky="ew")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=1)

    def resume(self, event=None):
        self.controller.updatePasswordValue(self.entry.get())
        MB.showNewPassword(self.entry.get())
        self.entry.delete(0, 'end')

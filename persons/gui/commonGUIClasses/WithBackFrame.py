import tkinter as tk
import tkinter.font as tf
import accessories.Accessories as Acc


class WithBackFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.parent = master

        self.font = tf.Font(family='Helvetica', size=18, weight='bold')

        self.replacer = tk.Frame(self.parent)

        self.backFrame = tk.Frame(self.replacer)
        self.backButton = tk.Button(self.backFrame, font=self.font, bg=Acc.green, fg=Acc.white,
                                    text=Acc.back, command=self.backButtonClicked)

    def view(self):
        self.grid(sticky="news")

    def anyButtonClicked(self):
        self.grid_forget()
        self.replacer.grid(sticky="news")
        self.backFrame.grid(row=0, column=0, sticky="ew")
        self.backButton.grid(sticky="news")
        self.replacer.columnconfigure(0, weight=1)
        self.replacer.rowconfigure(1, weight=1)
        self.backFrame.columnconfigure(0, weight=1)
        self.backFrame.rowconfigure(0, weight=1)

    def backButtonClicked(self):
        self.replacer.grid_forget()
        for child in self.replacer.winfo_children():
            if not (child == self.backFrame):
                child.destroy()
        self.view()

import tkinter as tk
import gui.FirstInteface as FI
import control.Controller as Con

if __name__ == '__main__':
    root = tk.Tk()
    root.title("الحسابات")
    FI.MainInterface(root, Con.Controller())
    root.mainloop()

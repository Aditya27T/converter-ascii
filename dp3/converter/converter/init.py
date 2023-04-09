from logic import KonversiBilanganLogic
from gui import KonversiBilanganGUI
from tkinter import *

class KonversiBilanganController:
    def __init__(self, master):
        self.master = master
        self.konversi_bilangan_logic = KonversiBilanganLogic()
        self.konversi_bilangan_gui = KonversiBilanganGUI(self.master, self.konversi_bilangan_logic)

if __name__ == "__main__":
    root = Tk()
    konversi_bilangan_controller = KonversiBilanganController(root)
    root.mainloop()

# Path: con]\gui.py
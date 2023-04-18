from tkinter import messagebox
import src.filmDAO
import tkinter as tk
import tkinter.font as tkFont

class Filmy(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = self.master.winfo_reqwidth()
        window_height = self.master.winfo_reqheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self):
        """
        Metoda sloouží pro zobrazení tabulky s filmy, které jsou v kině.
        :return: None.
        """
        self.table = tk.Frame(self)
        self.table.pack(side="top")

        hlavicka_id = tk.Label(self.table)
        hlavicka_id ["text"]="ID"
        ft = tkFont.Font(family='Times', size=10)
        hlavicka_id["font"] = ft
        hlavicka_id["fg"] = "#333333"
        hlavicka_id.grid(row=0, column=0, sticky="ew")
        hlavicka_nazev = tk.Label(self.table)
        hlavicka_nazev ["text"]="Název filmu"
        hlavicka_nazev["font"] = ft
        hlavicka_nazev["fg"] = "#333333"
        hlavicka_nazev.grid(row=0, column=1, sticky="ew")
        hlavicka_delka = tk.Label(self.table)
        hlavicka_delka ["text"]="Délka"
        hlavicka_delka["font"] = ft
        hlavicka_delka["fg"] = "#333333"
        hlavicka_delka.grid(row=0, column=2, sticky="ew")
        hlavicka_rok = tk.Label(self.table)
        hlavicka_rok ["text"]="Rok vydání"
        hlavicka_rok["font"] = ft
        hlavicka_rok["fg"] = "#333333"
        hlavicka_rok.grid(row=0, column=3, sticky="ew")

        # nastavení minimální šířky
        for i in range(4):
            self.table.grid_columnconfigure(i, minsize=100)

        filmy = src.filmDAO.film()
        filmy = filmy.get_all()
        self.row_frames = []
        for i, row in enumerate(filmy):
            label_id = tk.Label(self.table)
            label_id ["text"]=row[0]
            ft = tkFont.Font(family='Times', size=10)
            label_id["font"] = ft
            label_id["fg"] = "#333333"
            label_id ["anchor"]="center"
            label_id.grid(row=i + 1, column=0, sticky="ew")
            lable_nazev = tk.Label(self.table)
            lable_nazev ["text"]=row[1]
            lable_nazev["font"] = ft
            lable_nazev["fg"] = "#333333"
            lable_nazev ["anchor"]="center"
            lable_nazev.grid(row=i + 1, column=1, sticky="ew")
            label_delka = tk.Label(self.table)
            label_delka ["text"]=row[2]
            label_delka["font"] = ft
            label_delka["fg"] = "#333333"
            label_delka ["anchor"]="center"
            label_delka.grid(row=i + 1, column=2, sticky="ew")
            label_rok = tk.Label(self.table)
            label_rok ["text"]=row[3]
            label_rok["font"] = ft
            label_rok["fg"] = "#333333"
            label_rok ["anchor"]="center"
            label_rok.grid(row=i + 1, column=3, sticky="ew")

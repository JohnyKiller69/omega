from tkinter import messagebox
import src.adminDAO
import tkinter as tk
import tkinter.font as tkFont

class Pracovnici(tk.Frame):
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
        Metoda vytváří tabulku s informacemi o zaměstnancích a tlačítky pro jejich odstranění.
        :return: None
        """
        self.table = tk.Frame(self)
        self.table.pack(side="top")

        hlavicka_id = tk.Label(self.table)
        hlavicka_id ["text"]="ID"
        ft = tkFont.Font(family='Times', size=10)
        hlavicka_id["font"] = ft
        hlavicka_id["fg"] = "#333333"
        hlavicka_id.grid(row=0, column=0, sticky="ew")

        hlavicka_username = tk.Label(self.table)
        hlavicka_username ["text"]="Username"
        hlavicka_username["font"] = ft
        hlavicka_username["fg"] = "#333333"
        hlavicka_username.grid(row=0, column=1, sticky="ew")

        hlavicka_pohlavi = tk.Label(self.table)
        hlavicka_pohlavi ["text"]="Pohlaví"
        hlavicka_pohlavi["font"] = ft
        hlavicka_pohlavi["fg"] = "#333333"
        hlavicka_pohlavi.grid(row=0, column=2, sticky="ew")

        hlavicka_role = tk.Label(self.table)
        hlavicka_role ["text"]="Role"
        hlavicka_role["font"] = ft
        hlavicka_role["fg"] = "#333333"
        hlavicka_role.grid(row=0, column=3, sticky="ew")

        # Nastavení minimální šířky
        for i in range(4):
            self.table.grid_columnconfigure(i, minsize=100)

        pracovnici = src.adminDAO.Admin()
        pracovnici = pracovnici.get_all()
        self.row_frames = []

        for i, row in enumerate(pracovnici):
            label_id = tk.Label(self.table)
            label_id ["text"]=row[0]
            ft = tkFont.Font(family='Times', size=10)
            label_id["font"] = ft
            label_id["fg"] = "#333333"
            label_id ["anchor"]="center"
            label_id.grid(row=i + 1, column=0, sticky="ew")
            lable_username = tk.Label(self.table)
            lable_username ["text"]=row[1]
            lable_username["font"] = ft
            lable_username["fg"] = "#333333"
            lable_username ["anchor"]="center"
            lable_username.grid(row=i + 1, column=1, sticky="ew")
            label_pohlavi = tk.Label(self.table)
            label_pohlavi ["text"]=row[2]
            label_pohlavi["font"] = ft
            label_pohlavi["fg"] = "#333333"
            label_pohlavi ["anchor"]="center"
            label_pohlavi.grid(row=i + 1, column=2, sticky="ew")
            label_role = tk.Label(self.table)
            label_role ["text"]=row[3]
            label_role["font"] = ft
            label_role["fg"] = "#333333"
            label_role ["anchor"]="center"
            label_role.grid(row=i + 1, column=3, sticky="ew")
            delete_button = tk.Button(self.table)
            delete_button ["text"]="Vymazat"
            delete_button ["command"]=lambda id=row[0]: self.delete_row(id)
            delete_button.grid(row=i + 1, column=4)

    def delete_row(self, id):
        """
        Metoda slouží k odstranění záznamu z tabulky a zároveň vymazání pracovníka z databáze
        :param id: Id pracovníka.
        :return: None.
        """
        if not messagebox.askyesno("Potvrzení", f"Opravdu chcete smazat pracovníka s ID {id}?"):
            return
        else:
            pracovnici = src.adminDAO.Admin()
            pracovnici.delete_pracovnik(id)

            for row_frame in self.row_frames:
                label_id = row_frame.grid_slaves(0, 0)[0]
                if str(label_id.cget("text")) == str(id):
                    row_frame.grid_forget()

            # zde aktualizuji data
            pracovnici = src.adminDAO.Admin()
            pracovnici = pracovnici.get_all()
            for i, row in enumerate(pracovnici):
                row_frame = self.row_frames[i]

                label_id = row_frame.grid_slaves(0, 0)[0]
                label_id.config(text=row[0])

                label_username = row_frame.grid_slaves(0, 1)[0]
                label_username.config(text=row[1])

                label_pohlavi = row_frame.grid_slaves(0, 2)[0]
                label_pohlavi.config(text=row[2])

                label_role = row_frame.grid_slaves(0, 3)[0]
                label_role.config(text=row[3])

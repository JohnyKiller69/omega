import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import src.rezervaceDAO
import src.promitaniDAO
import src.filmDAO
import tkinter.font as tkFont

class ReservationEditor:

    def __init__(self, root):
        self.root = root
        self.root.title("Správa rezervací")
        self.tree = ttk.Treeview(self.root,
                                 columns=("id", "Promítání id", "Zákazník", "Osob", "Datum", "Film", "Promítání"),
                                 show="headings")
        for col in ("id", "Promítání id", "Zákazník", "Osob", "Datum", "Film", "Promítání"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(side="left", fill="both", expand=True)

        vsechny_rez = src.rezervaceDAO.rezervace()
        self.rezervace = vsechny_rez.get_rezervace_s_jmeny_prijmenimi()

        # Vložíme data do tabulky
        for row in self.rezervace:
            datum = datetime.datetime.strptime(str(row[5]), '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M')
            self.tree.insert("", tk.END,
                             values=(row[0], row[1], f"{row[2]} {row[3]}", row[4], datum,row[6],row[7]))

        # Přidáme tlačítko pro mazání vybrané rezervace
        self.delete_button = tk.Button(self.root)
        self.delete_button ["text"]="Vymazat vybranou rezervaci"
        self.delete_button ["command"]=self.delete_reservation
        self.delete_button ["state"]="disabled"
        self.delete_button["fg"] = "#000000"
        self.delete_button["justify"] = "center"
        self.delete_button.pack()
        self.tree.bind("<<TreeviewSelect>>", self.toggle_delete_button)

        self.edit_button = tk.Button(self.root)
        self.edit_button ["text"]="Upravit ID promítání"
        self.edit_button ["command"]=self.edit_screening_id
        self.edit_button ["state"]="disabled"
        self.edit_button["fg"] = "#000000"
        self.edit_button["justify"] = "center"
        self.edit_button.pack()
        self.tree.bind("<<TreeviewSelect>>", self.toggle_buttons)


        width = 1000
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def toggle_buttons(self, event):
        if len(self.tree.selection()) > 0:
            item = self.tree.selection()[0]
            values = self.tree.item(item, "values")
            if values and values[1]:
                self.edit_button.config(state="normal")
                self.delete_button.config(state="normal")
            else:
                self.edit_button.config(state="disabled")
                self.delete_button.config(state="disabled")
        else:
            self.edit_button.config(state="disabled")


    def toggle_delete_button(self, event):
        if len(self.tree.selection()) > 0:
            self.delete_button.config(state="normal")
        else:
            self.delete_button.config(state="disabled")

    def delete_reservation(self):
        item = self.tree.selection()[0]
        item = item.split()[0]
        reservation_id = int(self.tree.item(item, "values")[0])

        confirm = messagebox.askyesno("Potvrzení smazání",
                                      f"Opravdu chcete smazat rezervaci s ID {reservation_id}?")

        if confirm:
            rm = src.rezervaceDAO.rezervace()
            rm.remove_reservation(reservation_id)

            self.tree.delete(item)
            messagebox.showinfo("Smazání úspěšné",
                                f"Rezervace s ID {reservation_id} byla úspěšně smazána.")
            self.delete_button.config(state="disabled")
            self.edit_button.config(state="disabled")
        else:
            return
    def edit_screening_id(self):
        item = self.tree.selection()[0]
        reservation_id = int(self.tree.item(item, "values")[0])

        promitani = src.promitaniDAO.promitani()
        promitani = promitani.all_rezervace()

        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Upravit rezervaci")
        self.edit_window.geometry("300x150")

        label = tk.Label(self.edit_window)
        label ["text"]="Vyberte nové ID promítání:"
        label.pack(pady=10)

        screening_var = tk.StringVar(self.edit_window)
        screening_menu = ttk.Combobox(self.edit_window,
                                      textvariable=screening_var, values=[s[0] for s in promitani])
        screening_menu.pack()




        def update_screening_id():
            new_screening_id = int(screening_var.get())
            if new_screening_id:
                # Aktualizujeme promítání v databázi
                update = src.rezervaceDAO.rezervace()
                update.update_screening_id(reservation_id, new_screening_id)

                for item in self.tree.get_children():
                    self.tree.delete(item)

                # Načtení nových dat z databáze
                vsechny_rez = src.rezervaceDAO.rezervace()
                self.rezervace = vsechny_rez.get_rezervace_s_jmeny_prijmenimi()

                # Vložení nových dat do tabulky
                for row in self.rezervace:
                    datum = datetime.datetime.strptime(str(row[5]), '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M')
                    self.tree.insert("", tk.END,
                                     values=(row[0], row[1], f"{row[2]} {row[3]}", row[4], datum, row[6], row[7]))



                self.edit_window.destroy()
                self.delete_button.config(state="disabled")
                self.edit_button.config(state="disabled")


        film_label = tk.Label(self.edit_window)
        film_label ["text"]=""
        ft = tkFont.Font(family='Times', size=10)
        film_label["font"] = ft
        film_label["fg"] = "#333333"
        film_label["justify"] = "center"
        film_label.pack()
        time_label = tk.Label(self.edit_window)
        time_label ["text"]=""
        ft = tkFont.Font(family='Times', size=10)
        time_label["font"] = ft
        time_label["fg"] = "#333333"
        time_label["justify"] = "center"
        time_label.pack()

        def show_screening_info(event):
            selected_id = screening_menu.get()

            film = src.filmDAO.film()
            film = film.get_film_by_id(selected_id)
            for x in film:
                film_title = x[0]

            film_label.config(text=f"Film: {film_title}")
            promitani = src.promitaniDAO.promitani()
            promitani = promitani.cas_promitani(selected_id)
            for x in promitani:
                cas = x[4]
            time_label.config(text=f"Čas promítání: {cas}")

        screening_menu.bind("<<ComboboxSelected>>", show_screening_info)

        confirm_button = tk.Button(self.edit_window)
        confirm_button ["text"]="Potvrdit"
        confirm_button ["command"]=update_screening_id
        confirm_button.pack(pady=10)

        edit_window_x = (self.root.winfo_screenwidth() // 2) - (self.edit_window.winfo_width() // 2)
        edit_window_y = (self.root.winfo_screenheight() // 2) - (self.edit_window.winfo_height() // 2)
        self.edit_window.geometry(f"+{edit_window_x}+{edit_window_y}")

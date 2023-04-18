import src.zakaznikDAO
from tkinter import ttk, messagebox
import re
import tkinter as tk

class Zakaznici:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Seznam zákazníků")
        self.is_tel_open = False
        self.is_mail_open = False
        self.tree = ttk.Treeview(self.window, columns=("id", "jmeno", "prijmeni", "body", "email", "telefon", "vek"),
                                 show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("jmeno", text="Jméno")
        self.tree.heading("prijmeni", text="Příjmení")
        self.tree.heading("body", text="Body")
        self.tree.heading("email", text="Email")
        self.tree.heading("telefon", text="Telefon")
        self.tree.heading("vek", text="Věk")
        self.tree.pack(fill=tk.BOTH, expand=True)

        zakaz = src.zakaznikDAO.zakaznik()
        zk = zakaz.get_uzivatel()
        for row in zk:
            self.tree.insert("", "end", values=row)

        self.edit_telefon = tk.Button(self.window)
        self.edit_telefon["text"] = "Změna telefoního čísla"
        self.edit_telefon["command"] = self.update_tel
        self.edit_telefon["state"] = "disabled"
        self.tree.bind("<<TreeviewSelect>>", self.toggle_buttons)
        self.edit_telefon["fg"] = "#000000"
        self.edit_telefon["justify"] = "center"
        self.edit_telefon.pack(side=tk.LEFT, padx=5, pady=5)

        self.edit_email = tk.Button(self.window)
        self.edit_email["text"] = "Změna emailu"
        self.edit_email["command"] = self.update_email
        self.edit_email["state"] = "disabled"
        self.tree.bind("<<TreeviewSelect>>", self.toggle_edit_email_button)
        self.edit_email["fg"] = "#000000"
        self.edit_email["justify"] = "center"
        self.edit_email.pack(side=tk.LEFT, padx=5, pady=5)

        self.smazat_zakaznika = tk.Button(self.window)
        self.smazat_zakaznika["text"] = "Odebrat zákazníka."
        self.smazat_zakaznika["command"] = self.delete_zak
        self.smazat_zakaznika["state"] = "disabled"
        self.tree.bind("<<TreeviewSelect>>", self.toggle_buttons)
        self.smazat_zakaznika["fg"] = "#000000"
        self.smazat_zakaznika["justify"] = "center"
        self.smazat_zakaznika.pack(side=tk.LEFT, padx=5, pady=5)

        self.window.mainloop()
    def delete_zak(self):
        """
        Metoda slouží k odstranění zákazník z tabulky a zároveň z databáze.
        :return: None.
        """
        if not self.is_mail_open and not self.is_tel_open:
            item = self.tree.selection()[0]
            item = item.split()[0]
            customer_id = int(self.tree.item(item, "values")[0])
            jmeno = str(self.tree.item(item, "values")[1])
            prijmeni = str(self.tree.item(item, "values")[2])

            confirm = messagebox.askyesno("Potvrzení smazání",
                                          f"Opravdu chcete smazat uživatele s ID {jmeno,prijmeni}?")

            if confirm:
                cust = src.zakaznikDAO.zakaznik()
                cust.remove_zak(customer_id)

                self.tree.delete(item)
                messagebox.showinfo("Smazání úspěšné",
                                    f"Zákazník{jmeno,prijmeni} byla úspěšně smazán.")
                self.edit_telefon.config(state="disabled")
                self.edit_email.config(state="disabled")
                self.smazat_zakaznika.config(state="disabled")
            else:
                return
    def db_update_email(self,id,email):
        """
        Metoda slouží k aktualizaci emailové adresy zákazníka, kontroluje se zdali je ve správném formátu a
        ještě jestli už není použita.
        :param id: Id zákazníka.
        :param email: Novým email zákazníka.
        :return:
        """
        if email and re.match(r"[^@]+@[^@]+\.[^@]+", email):
            try:
                try:
                    cust = src.zakaznikDAO.zakaznik()
                    cust.update_email(id, email)
                except Exception as e:
                    messagebox.showerror("Chyba", e)
                self.update_mail_window.destroy()
                self.edit_email.config(state="disabled")
                self.edit_telefon.config(state="disabled")
                self.smazat_zakaznika.config(state="disabled")

                for item in self.tree.get_children():
                    self.tree.delete(item)

                zakaz = src.zakaznikDAO.zakaznik()
                zk = zakaz.get_uzivatel()

                for row in zk:
                    self.tree.insert("", "end", values=row)

            except ValueError as e:
                messagebox.showerror("Chyba", str(e))
        else:
            raise ValueError("Email je ve špatném formátu.")
    def update_email(self):
        """
        Metoda otevře nové okno pro zadání nového emailu.
        :return: None.
        """
        if not self.is_mail_open and not self.is_tel_open:

            self.is_mail_open = True
            selected_item = self.tree.selection()[0]
            customer_id = self.tree.item(selected_item)["values"][0]

            self.update_mail_window = tk.Toplevel(self.window)
            self.update_mail_window.title("Aktualizovat email zákazníka")
            self.update_mail_window.geometry("+%d+%d" % (self.window.winfo_width() // 2,
                                                    self.window.winfo_height() // 2))

            self.update_mail_window.protocol("WM_DELETE_WINDOW", self.on_close_email)

            email_label = tk.Label(self.update_mail_window)
            email_label["text"] = "Nový email:"
            email_label["fg"] = "#333333"
            email_label["justify"] = "center"
            email_label.pack()

            email_entry = tk.Entry(self.update_mail_window)
            email_entry["fg"] = "#333333"
            email_entry["justify"] = "center"
            email_entry.pack()

            update_button = tk.Button(self.update_mail_window)
            update_button["text"] = "Aktualizovat"
            update_button["command"] = lambda: self.db_update_email(customer_id, email_entry.get())
            update_button.pack()


    def update_telefon(self,id,tel):
        """
        Metoda aktualizuj telefoní číslo ověří jestli je to skutečně číslo a přidá ho do tabulky.
        :param id: Id zákazníka.
        :param tel: Nové telefoní číslo.
        :return: None.
        """
        try:
            if not tel.isdigit() or len(tel) != 9:
                raise ValueError("Telefonní číslo musí být devítimístné číslo.")
            try:
                cust = src.zakaznikDAO.zakaznik()
                cust.update_tel(id, tel)
            except Exception as e:
                messagebox.showerror("Chyba", e)
            self.edit_telefon.config(state="disabled")
            self.edit_email.config(state="disabled")
            self.smazat_zakaznika.config(state="disabled")

            for item in self.tree.get_children():
                self.tree.delete(item)
            zakaz = src.zakaznikDAO.zakaznik()
            zk = zakaz.get_uzivatel()
            for row in zk:
                self.tree.insert("", "end", values=row)
        except ValueError as e:
            messagebox.showerror("Chyba", str(e))

    def update_tel(self):
        """
        Metoda vytváří nové okno pro zadání nového telefoního čísla.
        :return: None.
        """
        if not self.is_mail_open and not self.is_tel_open:
            self.is_tel_open = True
            selected_item = self.tree.selection()[0]
            customer_id = self.tree.item(selected_item)["values"][0]

            self.update_window = tk.Toplevel(self.window)
            self.update_window.title("Aktualizovat telefon zákazníka")
            self.update_window.geometry("+%d+%d" % (self.window.winfo_width() // 2,
                                                    self.window.winfo_height() // 2))

            self.update_window.protocol("WM_DELETE_WINDOW", self.on_close)


            phone_label = tk.Label(self.update_window)
            phone_label ["text"]="Nové telefonní číslo:"
            phone_label["fg"] = "#333333"
            phone_label["justify"] = "center"
            phone_label.pack()

            phone_entry = tk.Entry(self.update_window)
            phone_entry["fg"] = "#333333"
            phone_entry["justify"] = "center"
            phone_entry.pack()

            update_button = tk.Button(self.update_window)
            update_button ["text"]="Aktualizovat"
            update_button["command"] = lambda: self.update_telefon(customer_id, phone_entry.get())
            update_button.pack()






    def toggle_edit_email_button(self, event):
        """
        Metoda slouží pro přepínání tlačítka mezi normal a disabled podle toho jestli je vybrán řádek.
        :param event: None
        :return: None
        """
        if len(self.tree.selection()) > 0:
            self.edit_email.config(state="normal")
        else:
            self.edit_email.config(state="disabled")

    def toggle_buttons(self, event):
        """
        Metode slouží k nastavování tlačítek na normal nebo disabled podle toho jestli je řádek vybrán nebo ne.
        :param event: None.
        :return: None.
        """
        if len(self.tree.selection()) > 0:
            item = self.tree.selection()[0]
            values = self.tree.item(item, "values")
            if values and values[1]:
                self.edit_telefon.config(state="normal")
                self.edit_email.config(state="normal")
                self.smazat_zakaznika.config(state="normal")
            else:
                self.edit_telefon.config(state="disabled")
                self.edit_email.config(state="disabled")
                self.smazat_zakaznika.config(state="disabled")
        else:
            self.edit_telefon.config(state="disabled")

    def on_close(self):
        """
        Metoda zavře okno pro aktualizaci telefoního čísla.
        :return: None
        """
        self.is_tel_open = False
        self.update_window.destroy()

    def on_close_email(self):
        """
        Metoda zavře okno pro aktualizaci  emailu.
        :return: None
        """
        self.is_mail_open = False
        self.update_mail_window.destroy()
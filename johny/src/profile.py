import hashlib
import tkinter as tk
import src.adminDAO
import re
from tkinter import messagebox

class UserInfoWindow:
    def __init__(self, root, username,role,pohlavi):
        self.root = root
        self.username = username
        name = src.adminDAO.Admin()
        name = name.get_jmeno(self.username)
        self.username = name[0]
        self.name_popup = None
        self.pass_popup = None
        root.title("Profil")

        # create new top-level window
        self.window = tk.Toplevel(self.root)
        width = 400
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        # set window size and position
        self.window.geometry(alignstr)

        # create label at the top with username
        self.username_label = tk.Label(self.window)
        self.username_label["text"] = "Moje údaje"
        self.username_label["font"] = ("Arial", 16, "bold")
        self.username_label.pack(pady=10)

        frame1 = tk.Frame(self.window)
        frame1.pack(pady=5)

        # create three labels below the username label
        self.label1 = tk.Label(frame1)
        self.label1["text"] = "Username:"
        self.label1["bg"] = "#FFFFFF"
        self.label1["font"] = ("Times", 15)
        self.label1["fg"] = "#000000"
        self.label1["justify"] = "center"
        self.label1.pack(side="left")

        self.label4 = tk.Label(frame1)
        self.label4["text"] = self.username
        self.label4["bg"] = "#FFFFFF"
        self.label4["font"] = ("Times", 15)
        self.label4["fg"] = "#000000"
        self.label4["justify"] = "center"
        self.label4.pack(side="left")



        frame2 = tk.Frame(self.window)
        frame2.pack(pady=5)

        self.label2 = tk.Label(frame2)
        self.label2["text"] = "Role:"
        self.label2["bg"] = "#FFFFFF"
        self.label2["font"] = ("Times", 15)
        self.label2["fg"] = "#000000"
        self.label2["justify"] = "center"
        self.label2.pack(side="left")

        self.label5 = tk.Label(frame2)
        self.label5["text"] = role
        self.label5["bg"] = "#FFFFFF"
        self.label5["font"] = ("Times", 15)
        self.label5["fg"] = "#000000"
        self.label5["justify"] = "center"
        self.label5.pack(side="left")

        frame3 = tk.Frame(self.window)
        frame3.pack(pady=5)

        self.label3 = tk.Label(frame3)
        self.label3["text"] = "Pohlaví:"
        self.label3["bg"] = "#FFFFFF"
        self.label3["font"] = ("Times", 15)
        self.label3["fg"] = "#000000"
        self.label3["justify"] = "center"
        self.label3.pack(side="left")

        self.label6 = tk.Label(frame3)
        self.label6["text"] = pohlavi
        self.label6["bg"] = "#FFFFFF"
        self.label6["font"] = ("Times", 15)
        self.label6["fg"] = "#000000"
        self.label6["justify"] = "center"
        self.label6.pack(side="left")

        frame4 = tk.Frame(self.window)
        frame4.pack(pady=5)

        self.zmena_jmena = tk.Button(frame4)
        self.zmena_jmena["text"] = "změnit jméno"
        self.zmena_jmena["bg"] = "#FFFFFF"
        self.zmena_jmena["font"] = ("Times", 12)
        self.zmena_jmena["fg"] = "#000000"
        self.zmena_jmena["justify"] = "center"
        self.zmena_jmena.pack(side="left")
        self.zmena_jmena["command"] = self.zmenit_jmeno

        self.zmena_jmena = tk.Button(frame4)
        self.zmena_jmena["text"] = "změnit heslo"
        self.zmena_jmena["bg"] = "#FFFFFF"
        self.zmena_jmena["font"] = ("Times", 12)
        self.zmena_jmena["fg"] = "#000000"
        self.zmena_jmena["justify"] = "center"
        self.zmena_jmena.pack(side="left")
        self.zmena_jmena["command"] = self.zmenit_heslo

    def to_front(self):
        self.root.focus_set()
        print("zavolano")
    def zmenit_jmeno(self):
        if self.pass_popup is not None:
            return
        elif self.name_popup is not None:
            return

        def potvrdit():
            new_name = name_entry.get()
            try:
                if not new_name.strip():
                    raise Exception("Jméno nesmí být prázdné")
                elif len(new_name) < 2 or len(new_name) > 20:
                    raise Exception("Délka jména je mimo rozsah.")
                elif new_name == self.username:
                    raise Exception("Jméno je stejné.")
                elif not re.match(r'^\w+$', new_name):
                    raise Exception("Jméno nesmí obsahovat speciální znaky.")
                else:
                    admn = src.adminDAO.Admin()
                    admn.kontrola_jmena(new_name)
                    admn = src.adminDAO.Admin()
                    admn.update_jmena(self.username, new_name)
                    self.refresh_name(new_name)
                    self.to_front()
                    messagebox.showinfo("Úspěch", "Jméno bylo úspěšně změněno.")
                    self.close_name_popup()
            except Exception as e:
                messagebox.showerror("Chyba",e)
                self.name_popup.focus_set()


        def zrusit():
            self.close_name_popup()

        self.name_popup = tk.Toplevel(self.root)
        self.name_popup.title('Změnit jméno')
        self.name_popup.protocol("WM_DELETE_WINDOW", self.close_name_popup)

        name_label = tk.Label(self.name_popup)
        name_label ["text"]='Zadejte nové jméno:'
        name_label["fg"] = "#333333"
        name_label["justify"] = "center"
        name_label.pack(pady=(10, 0))

        name_entry = tk.Entry(self.name_popup)
        name_entry.pack(pady=(5, 10))
        name_entry["borderwidth"] = "1px"
        name_entry["fg"] = "#333333"
        name_entry["justify"] = "center"

        potvrdit_button = tk.Button(self.name_popup)
        potvrdit_button["text"]='Potvrdit'
        potvrdit_button["command"]=potvrdit
        potvrdit_button["fg"] = "#000000"
        potvrdit_button["justify"] = "center"
        potvrdit_button.pack(side='left', padx=(10, 5), pady=(0, 10))

        zrusit_button = tk.Button(self.name_popup)
        zrusit_button ["text"]='Zrušit'
        zrusit_button ["command"]=zrusit
        zrusit_button["fg"] = "#000000"
        zrusit_button["justify"] = "center"
        zrusit_button.pack(side='right', padx=(5, 10), pady=(0, 10))

        # Nastavení pozice okna uprostřed obrazovky
        self.name_popup.update_idletasks()
        width = self.name_popup.winfo_width()
        height = self.name_popup.winfo_height()
        screen_width = self.name_popup.winfo_screenwidth()
        screen_height = self.name_popup.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.name_popup.geometry(f"{width}x{height}+{x}+{y}")
    def refresh_name(self,name):
        self.label4.configure(text=name)
        self.username = name
    def close_name_popup(self):
        if self.name_popup is not None:
            self.name_popup.destroy()
            self.name_popup = None

    def close_pass_popup(self):
        if self.pass_popup is not None:
            self.pass_popup.destroy()
            self.pass_popup = None


    def zmenit_heslo(self):
        if self.pass_popup is not None:
            return
        if self.name_popup is not None:
            return

        def hash_password(password):
            """Hashes a password using SHA-256."""
            salt = b'somesalt'  # Change this to a random value for production use
            password = password.encode('utf-8')
            return hashlib.sha256(salt + password).hexdigest()

        def potvrdit():
            stare_heslo = heslo_entry.get()
            nove_heslo = heslo_entry2.get()
            nove_heslo_kon = heslo_entry3.get()
            specialni_znaky = "!@#$%^&*()-+?_=,<>/"


            try:
                if not stare_heslo:
                    raise Exception("Staré heslo nesmí být prázdné.")
                elif not nove_heslo:
                    raise Exception("Nové heslo nesmí být prázdné.")
                elif not nove_heslo_kon:
                    raise Exception("Potvrzení nového hesla nesmí být prázdné.")
                elif nove_heslo != nove_heslo_kon:
                    raise Exception("Nové heslo se neshoduje s potvrzením nového hesla.")

                elif not any(char in specialni_znaky for char in nove_heslo) \
                    or not any(char in specialni_znaky for char in specialni_znaky):
                    raise Exception("Nové heslo neobsahuje speciální znak.")
                elif len(nove_heslo) < 5 or len(nove_heslo) > 20 or len(nove_heslo_kon) < 5 or len(nove_heslo_kon) > 20:
                    raise Exception("Heslo musí být v rozsahu 5 až 20 znaků!")

                else:
                    admn = src.adminDAO.Admin()
                    stare_heslo = hash_password(stare_heslo)
                    admn.get_heslo(self.username,stare_heslo)
                    nove_heslo = hash_password(nove_heslo)
                    update = admn.update_heslo(self.username,nove_heslo)
                    if update == True:
                        messagebox.showinfo("Úspěch", "Heslo bylo úspěšně změněno.")
                        self.close_pass_popup()
                    else:
                        raise Exception("Update hesla se nepovedl!")
            except Exception as e:
                messagebox.showerror("Chyba", e)
                self.pass_popup.focus_set()

        def zrusit():
            self.close_pass_popup()

        self.pass_popup = tk.Toplevel(self.root)
        self.pass_popup.title('Změnit heslo')
        self.pass_popup.protocol("WM_DELETE_WINDOW", self.close_pass_popup)

        heslo_label = tk.Label(self.pass_popup)
        heslo_label ["text"]='Zadejte staré heslo:'
        heslo_label["fg"] = "#333333"
        heslo_label["justify"] = "center"
        heslo_label.pack(pady=(10, 0))

        heslo_entry = tk.Entry(self.pass_popup,show="*")
        heslo_entry.pack(pady=(5, 10))
        heslo_entry["borderwidth"] = "1px"
        heslo_entry["fg"] = "#333333"
        heslo_entry["justify"] = "center"

        heslo_label2 = tk.Label(self.pass_popup)
        heslo_label2["text"] = 'Zadejte nové heslo:'
        heslo_label2["fg"] = "#333333"
        heslo_label2["justify"] = "center"
        heslo_label2.pack(pady=(10, 0))

        heslo_entry2 = tk.Entry(self.pass_popup,show="*")
        heslo_entry2.pack(pady=(5, 10))
        heslo_entry2["borderwidth"] = "1px"
        heslo_entry2["fg"] = "#333333"
        heslo_entry2["justify"] = "center"

        heslo_label3 = tk.Label(self.pass_popup)
        heslo_label3["text"] = 'Zadejte znovu heslo:'
        heslo_label3["fg"] = "#333333"
        heslo_label3["justify"] = "center"
        heslo_label3.pack(pady=(10, 0))

        heslo_entry3 = tk.Entry(self.pass_popup,show="*")
        heslo_entry3.pack(pady=(5, 10))
        heslo_entry3["borderwidth"] = "1px"
        heslo_entry3["fg"] = "#333333"
        heslo_entry3["justify"] = "center"

        potvrdit_button = tk.Button(self.pass_popup)
        potvrdit_button["text"] = 'Potvrdit'
        potvrdit_button["command"] = potvrdit
        potvrdit_button["fg"] = "#000000"
        potvrdit_button["justify"] = "center"
        potvrdit_button.pack(side='left', padx=(10, 5), pady=(0, 10))

        zrusit_button = tk.Button(self.pass_popup)
        zrusit_button["text"] = 'Zrušit'
        zrusit_button["command"] = zrusit
        zrusit_button["fg"] = "#000000"
        zrusit_button["justify"] = "center"
        zrusit_button.pack(side='right', padx=(5, 10), pady=(0, 10))

        # Nastavení pozice okna uprostřed obrazovky
        self.pass_popup.update_idletasks()
        width = self.pass_popup.winfo_width()
        height = self.pass_popup.winfo_height()
        screen_width = self.pass_popup.winfo_screenwidth()
        screen_height = self.pass_popup.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.pass_popup.geometry(f"{width}x{height}+{x}+{y}")

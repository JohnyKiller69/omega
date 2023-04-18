from src.mainWindow import App
from tkinter import messagebox
import src.rezervaceDAO
import src.zakaznikDAO
import src.importDat
import src.viewDAO
import src.login
import src.rezervace
import tkinter as tk
import tkinter.font as tkFont

class App(App):

    def handle_registrace_close(self, root):
        self.is_rezervace_open = False
        root.destroy()


    def GButton_921_command(self):
        user_choice = messagebox.askyesno("Odhlášení", "Opravdu se chcete odhlásit?")
        if user_choice:
            self.root.destroy()
            root = tk.Tk()
            login = src.login.Login(root)
            root.mainloop()



    def close_rez_window(self):
        self.is_rez_open = False
        self.rez_window.destroy()


    def GButton_901_command(self):
        self.GMessage_503.config(state=tk.NORMAL)
        if self.rezervace:
            return
        elif self.prevod:
            return
        else:
            self.rezervace = True
            self.GMessage_503.insert(tk.END, "---Vytváření rezervace---\n")
            self.GLineEdit_985 = tk.Entry(self.root)
            self.GLineEdit_985["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_985["font"] = ft
            self.GLineEdit_985["fg"] = "#333333"
            self.GLineEdit_985["justify"] = "center"
            self.GLineEdit_985["text"] = "id"
            self.GLineEdit_985.place(x=1170, y=60, width=176, height=42)

            self.GLineEdit_797 = tk.Entry(self.root)
            self.GLineEdit_797["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_797["font"] = ft
            self.GLineEdit_797["fg"] = "#333333"
            self.GLineEdit_797["justify"] = "center"
            self.GLineEdit_797["text"] = "jm"
            self.GLineEdit_797.place(x=1170, y=140, width=177, height=39)

            self.GButton_689 = tk.Button(self.root)
            self.GButton_689["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times', size=10)
            self.GButton_689["font"] = ft
            self.GButton_689["fg"] = "#000000"
            self.GButton_689["justify"] = "center"
            self.GButton_689["text"] = "Rezervovat"
            self.GButton_689.place(x=1260, y=290, width=86, height=34)
            self.GButton_689["command"] = self.GButton_689_command

            self.GButton_690 = tk.Button(self.root)
            self.GButton_690["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times', size=10)
            self.GButton_690["font"] = ft
            self.GButton_690["fg"] = "#000000"
            self.GButton_690["justify"] = "center"
            self.GButton_690["text"] = "Zrušit"
            self.GButton_690.place(x=1060, y=290, width=86, height=34)
            self.GButton_690["command"] = self.GButton_690_command

            self.GLineEdit_549 = tk.Entry(self.root)
            self.GLineEdit_549["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_549["font"] = ft
            self.GLineEdit_549["fg"] = "#333333"
            self.GLineEdit_549["justify"] = "center"
            self.GLineEdit_549["text"] = "pr"
            self.GLineEdit_549.place(x=1170, y=220, width=178, height=37)

            self.GLabel_75 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_75["font"] = ft
            self.GLabel_75["fg"] = "#333333"
            self.GLabel_75["justify"] = "center"
            self.GLabel_75["text"] = "Id promítání"
            self.GLabel_75.place(x=1000, y=60, width=173, height=41)

            self.GLabel_287 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_287["font"] = ft
            self.GLabel_287["fg"] = "#333333"
            self.GLabel_287["justify"] = "center"
            self.GLabel_287["text"] = "Jméno"
            self.GLabel_287.place(x=1000, y=140, width=173, height=41)

            self.GLabel_42 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_42["font"] = ft
            self.GLabel_42["fg"] = "#333333"
            self.GLabel_42["justify"] = "center"
            self.GLabel_42["text"] = "Příjmení"
            self.GLabel_42.place(x=1000, y=220, width=173, height=41)
        self.GMessage_503.config(state=tk.DISABLED)

    def GButton_689_command(self):
        self.GMessage_503.config(state=tk.NORMAL)
        id = self.GLineEdit_985.get()
        jmeno = self.GLineEdit_797.get()
        prijmeni = self.GLineEdit_549.get()
        if id.isdigit():
            try:
                prom = int(id)
                if isinstance(prom, int) and prom > 0:
                    name = str(jmeno)
                    surname = str(prijmeni)
                    rezervace = src.rezervaceDAO.rezervace()
                    rezervace.vytvoreni_rezervace(prom, name, surname, 1)

                    self.GMessage_503.insert(tk.END, "Úspěšně uloženo\n")
                    self.rezervace = False

                    self.GButton_690_command()
                else:
                    raise Exception("Špatná hodnota id")
            except Exception as e:
                self.GMessage_503.insert(tk.END, "Error: {}\n".format(e))
        else:
            self.GMessage_503.insert(tk.END, "Id nezadáno\n")
        self.GMessage_503.config(state=tk.DISABLED)

    def GButton_690_command(self):
        self.GLineEdit_985.delete(0, "end")
        self.GMessage_503.insert(tk.END, "Konec vytváření rezervace\n")
        self.GLineEdit_797.delete(0, "end")
        self.GLineEdit_549.delete(0, "end")
        self.GLineEdit_985.destroy()
        self.GLineEdit_797.destroy()
        self.GLineEdit_549.destroy()
        self.GLabel_75.destroy()
        self.GLabel_287.destroy()
        self.GLabel_42.destroy()
        self.GButton_689.destroy()
        self.GButton_690.destroy()
        self.rezervace = False

    def GButton_62_command(self):

        if self.prevod:
            return
        elif self.rezervace:
            return
        else:
            self.prevod = True
            self.GLabel_336 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_336["font"] = ft
            self.GLabel_336["fg"] = "#333333"
            self.GLabel_336["justify"] = "center"
            self.GLabel_336["text"] = "Jméno"
            self.GLabel_336.place(x=1170, y=60, width=110, height=35)

            self.GLabel_633 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_633["font"] = ft
            self.GLabel_633["fg"] = "#333333"
            self.GLabel_633["justify"] = "center"
            self.GLabel_633["text"] = "Příjmení"
            self.GLabel_633.place(x=1170, y=120, width=110, height=35)

            self.GLabel_370 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_370["font"] = ft
            self.GLabel_370["fg"] = "#333333"
            self.GLabel_370["justify"] = "center"
            self.GLabel_370["text"] = "Email adresáta"
            self.GLabel_370.place(x=1170, y=180, width=110, height=35)

            self.GLabel_996 = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.GLabel_996["font"] = ft
            self.GLabel_996["fg"] = "#333333"
            self.GLabel_996["justify"] = "center"
            self.GLabel_996["text"] = "Počet bodů"
            self.GLabel_996.place(x=1170, y=240, width=110, height=35)

            self.GButton_770 = tk.Button(self.root)
            self.GButton_770["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times', size=10)
            self.GButton_770["font"] = ft
            self.GButton_770["fg"] = "#000000"
            self.GButton_770["justify"] = "center"
            self.GButton_770["text"] = "Převést"
            self.GButton_770.place(x=1330, y=310, width=70, height=25)
            self.GButton_770["command"] = self.GButton_770_command

            self.cancel = tk.Button(self.root)
            self.cancel["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times', size=10)
            self.cancel["font"] = ft
            self.cancel["fg"] = "#000000"
            self.cancel["justify"] = "center"
            self.cancel["text"] = "Zrušit"
            self.cancel.place(x=1230, y=310, width=70, height=25)
            self.cancel["command"] = self.cancel_cmd

            self.GLineEdit_380 = tk.Entry(self.root)
            self.GLineEdit_380["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_380["font"] = ft
            self.GLineEdit_380["fg"] = "#333333"
            self.GLineEdit_380["justify"] = "center"
            self.GLineEdit_380["text"] = "jm"
            self.GLineEdit_380.place(x=1290, y=60, width=110, height=35)

            self.GLineEdit_99 = tk.Entry(self.root)
            self.GLineEdit_99["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_99["font"] = ft
            self.GLineEdit_99["fg"] = "#333333"
            self.GLineEdit_99["justify"] = "center"
            self.GLineEdit_99["text"] = "pr"
            self.GLineEdit_99.place(x=1290, y=120, width=110, height=35)

            self.GLineEdit_340 = tk.Entry(self.root)
            self.GLineEdit_340["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_340["font"] = ft
            self.GLineEdit_340["fg"] = "#333333"
            self.GLineEdit_340["justify"] = "center"
            self.GLineEdit_340["text"] = "em"
            self.GLineEdit_340.place(x=1290, y=180, width=110, height=35)

            self.GLineEdit_971 = tk.Entry(self.root)
            self.GLineEdit_971["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=10)
            self.GLineEdit_971["font"] = ft
            self.GLineEdit_971["fg"] = "#333333"
            self.GLineEdit_971["justify"] = "center"
            self.GLineEdit_971["text"] = "bd"
            self.GLineEdit_971.place(x=1290, y=240, width=110, height=35)


    def GButton_770_command(self):
        self.GMessage_503.config(state=tk.NORMAL)
        name = self.GLineEdit_380.get()
        surname = self.GLineEdit_99.get()
        email = self.GLineEdit_340.get()
        points = self.GLineEdit_971.get()
        try:
            if not name:
                raise Exception("Vyplňte jméno!")
            elif not surname:
                raise Exception("Vyplňte příjmení!")
            elif not email:
                raise Exception("Vyplňte email!")
            elif not points:
                raise Exception("Zadejte počet bodů!")
            else:
                zakaznik = src.zakaznikDAO.zakaznik()
                zakaznik.uzv_exists_jm(name,surname)
                zakaznik.email_exists(email)
                result = zakaznik.prevod_kreditu(name, surname, email, points)
                self.GMessage_503.insert(tk.END, result + '\n')
                self.prevod = False
                self.cancel_cmd()
        except Exception as e:
            self.GMessage_503.insert(tk.END, "Error: {}\n".format(e))
        self.GMessage_503.config(state=tk.DISABLED)

    def cancel_cmd(self):
        self.prevod = False
        self.GLineEdit_380.delete(0, "end")
        self.GLineEdit_99.delete(0, "end")
        self.GLineEdit_340.delete(0, "end")
        self.GLineEdit_971.delete(0, "end")
        self.GLineEdit_380.destroy()
        self.GLineEdit_99.destroy()
        self.GLineEdit_340.destroy()
        self.GLineEdit_971.destroy()
        self.GLabel_996.destroy()
        self.GLabel_370.destroy()
        self.GLabel_633.destroy()
        self.GLabel_336.destroy()
        self.GButton_770.destroy()
        self.cancel.destroy()
import tkinter as tk
import tkinter.font as tkFont
import tkcalendar as tkc
import src.zakaznikDAO
import datetime
import re
class Zakaznik:
    def __init__(self, root):
        #setting title
        self.root = root
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_618=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "center"
        GLabel_618["text"] = "Registrace zákazníka"
        GLabel_618.place(x=200,y=20,width=200,height=45)

        GLabel_652=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_652["font"] = ft
        GLabel_652["fg"] = "#333333"
        GLabel_652["justify"] = "left"
        GLabel_652["text"] = "jméno"
        GLabel_652.place(x=90,y=110,width=70,height=25)

        GLabel_639=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_639["font"] = ft
        GLabel_639["fg"] = "#333333"
        GLabel_639["justify"] = "left"
        GLabel_639["text"] = "příjmení"
        GLabel_639.place(x=90,y=150,width=70,height=25)

        GLabel_568=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_568["font"] = ft
        GLabel_568["fg"] = "#333333"
        GLabel_568["justify"] = "left"
        GLabel_568["text"] = "email"
        GLabel_568.place(x=90,y=190,width=70,height=25)

        GLabel_148=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_148["font"] = ft
        GLabel_148["fg"] = "#333333"
        GLabel_148["justify"] = "left"
        GLabel_148["text"] = "telefon"
        GLabel_148.place(x=90,y=230,width=70,height=25)

        GLabel_978=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_978["font"] = ft
        GLabel_978["fg"] = "#333333"
        GLabel_978["justify"] = "left"
        GLabel_978["text"] = "narození"
        GLabel_978.place(x=90,y=270,width=70,height=25)

        self.GLineEdit_88=tk.Entry(root)
        self.GLineEdit_88["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_88["font"] = ft
        self.GLineEdit_88["fg"] = "#333333"
        self.GLineEdit_88["justify"] = "center"
        self.GLineEdit_88["text"] = "jmeno"
        self.GLineEdit_88.place(x=200,y=110,width=100,height=25)

        self.GLineEdit_843=tk.Entry(root)
        self.GLineEdit_843["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_843["font"] = ft
        self.GLineEdit_843["fg"] = "#333333"
        self.GLineEdit_843["justify"] = "center"
        self.GLineEdit_843["text"] = "prijmeni"
        self.GLineEdit_843.place(x=200,y=150,width=100,height=25)

        self.GLineEdit_258=tk.Entry(root)
        self.GLineEdit_258["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_258["font"] = ft
        self.GLineEdit_258["fg"] = "#333333"
        self.GLineEdit_258["justify"] = "center"
        self.GLineEdit_258["text"] = "eamil"
        self.GLineEdit_258.place(x=170,y=190,width=150,height=25)

        self.GLineEdit_815=tk.Entry(root)
        self.GLineEdit_815["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_815["font"] = ft
        self.GLineEdit_815["fg"] = "#333333"
        self.GLineEdit_815["justify"] = "center"
        self.GLineEdit_815["text"] = "telefon"
        self.GLineEdit_815.place(x=200,y=230,width=100,height=25)

        self.cal = tkc.Calendar(root, selectmode="day", year=2023, month=4, day=2)
        self.cal.place(x=200, y=270)



        GButton_646=tk.Button(root)
        GButton_646["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_646["font"] = ft
        GButton_646["fg"] = "#000000"
        GButton_646["justify"] = "center"
        GButton_646["text"] = "Registrovat"
        GButton_646.place(x=80,y=470,width=100,height=25)
        GButton_646["command"] = self.GButton_646_command

    def display_error(self, message):
        error_label = tk.Label(self.root, text=message, fg="red")
        error_label.place(x=250, y=60)

    def remove_error(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget('fg') == 'red':
                widget.destroy()
    def GButton_646_command(self):
        jmeno = self.GLineEdit_88.get()
        prijmeni = self.GLineEdit_843.get()
        email = self.GLineEdit_258.get()
        telefon = self.GLineEdit_815.get()
        datum = self.cal.selection_get()
        today = datetime.date.today()
        vek = today.year - datum.year - ((today.month, today.day) < (datum.month, datum.day))
        if not jmeno:
            self.remove_error()
            self.display_error("Error: vyplňte jméno!")
        if 2 > len(jmeno) > 20:
            self.remove_error()
            self.display_error("Error: Jméno musí být v rozsahu 2 až 20 znaků!")
        elif not prijmeni:
            self.remove_error()
            self.display_error("Error: vyplňte příjmení.")
        elif not email:
            self.remove_error()
            self.display_error("Error: vyplňte email.")
        elif not telefon:
            self.remove_error()
            self.display_error("Error: vyplňte telefon.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.remove_error()
            self.display_error("Error: špatný formát emailu.")
        elif not re.match(r"\d{9}", telefon):
            self.remove_error()
            self.display_error("Error: špatný formát telefoního čísla.")
        elif vek <= 15:
            self.remove_error()
            self.display_error("Error: Musí vám být minimálně 15let.")
        else:
            self.remove_error()
            try:
                reg = src.zakaznikDAO.zakaznik()
                reg.uzv_exists(email)
                send = reg.uzv_exists_jm_pr(jmeno,prijmeni,email,telefon,vek)
                if send:
                    self.show_popup()
                    self.GButton_303_command()
                else:
                    return

            except Exception as e:
                self.display_error(e)

    def show_popup(self):
        popup = tk.Toplevel()
        popup.title("Registrace úspěšná!")
        popup.geometry("300x100")
        # získání rozměrů obrazovky
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        # výpočet pozice pro zarovnání na střed
        x = (screen_width - popup.winfo_reqwidth()) / 2
        y = (screen_height - popup.winfo_reqheight()) / 2
        # nastavení pozice
        popup.geometry("+%d+%d" % (x, y))
        label = tk.Label(popup, text="Registrace proběhla úspěšně!")
        label.pack(pady=10)
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack()


    def GButton_303_command(self):
        self.GLineEdit_88.delete(0, "end")
        self.GLineEdit_843.delete(0, "end")
        self.GLineEdit_258.delete(0, "end")
        self.GLineEdit_815.delete(0, "end")






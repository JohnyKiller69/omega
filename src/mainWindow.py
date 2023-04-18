import src.rezervaceDAO
import src.zakaznikDAO
import src.importDat
import src.viewDAO
import src.login
import src.rezervace
import src.zakaznik
import src.adminDAO as admin
import src.view
import src.profile
import src.delZakaznik
import src.admins
import src.filmy
from src.importData import open_drag_and_drop_window
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk, ImageDraw, ImageOps
from tkinter import PhotoImage, messagebox
import os
import sys


def resource_path(relative_path: str):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        relative_path = relative_path.replace('/', '\\')
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App:
    def __init__(self, root,logged_in_user=None):
        self.logged_in_user = logged_in_user
        #setting title
        root.title("Main window")
        self.root = root
        self.prevod = False
        self.rezervace = False
        self.is_rezervace_open = False
        self.is_rez_open = False
        self.is_zakaznik_open = False
        self.is_views_open = False
        self.user_window = None
        #setting window size
        width=1920
        height=1080
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        self.GMessage_503 = tk.Text(root, wrap=tk.WORD)
        ft = tkFont.Font(
            family='Times'
            , size=10
        )
        self.GMessage_503["font"] = ft
        self.GMessage_503["bg"] = "#1e9fff"

        self.GMessage_503.place(x=60, y=80, width=316, height=881)
        image = Image.open(resource_path("img/avtr.jpg"))
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)

        # apply the mask to the image
        output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        # convert to PhotoImage and create a label
        photo = ImageTk.PhotoImage(output)
        label = tk.Label(self.root, image=photo)
        label.image = photo  # prevent image from being garbage collected
        label.place(x=1570, y=10)
        label.bind("<Button-1>", lambda e: self.redirect_to_profile())


        # Create a scrollbar widget
        scrollbar = tk.Scrollbar(root,
                                 orient=tk.VERTICAL,
                                 command=self.GMessage_503.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Attach the scrollbar to the text widget
        self.GMessage_503.config(yscrollcommand=scrollbar.set)
        self.GMessage_503.config(state=tk.DISABLED)

        GButton_921 = tk.Button(root)
        GButton_921["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_921["font"] = ft
        GButton_921["fg"] = "#000000"
        GButton_921["justify"] = "center"
        GButton_921["text"] = "Odhlásit se"
        GButton_921.place(x=1760, y=1010, width=134, height=40)
        GButton_921["command"] = self.GButton_921_command

        GButton_901 = tk.Button(root)
        GButton_901["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#000000"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "Vytvořit rezervaci"
        GButton_901.place(x=500, y=40, width=342, height=30)
        GButton_901["command"] = self.GButton_901_command

        GButton_62 = tk.Button(root)
        GButton_62["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_62["font"] = ft
        GButton_62["fg"] = "#000000"
        GButton_62["justify"] = "center"
        GButton_62["text"] = "Převod kreditů"
        GButton_62.place(x=500, y=110, width=342, height=30)
        GButton_62["command"] = self.GButton_62_command

        GButton_843 = tk.Button(root)
        GButton_843["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_843["font"] = ft
        GButton_843["fg"] = "#000000"
        GButton_843["justify"] = "center"
        GButton_843["text"] = "Úprava rezervací"
        GButton_843.place(x=500, y=180, width=341, height=30)
        GButton_843["command"] = self.GButton_843_command

        new_user = tk.Button(root)
        new_user["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        new_user["font"] = ft
        new_user["fg"] = "#000000"
        new_user["justify"] = "center"
        new_user["text"] = "Registrace zákazníka"
        new_user.place(x=500, y=250, width=341, height=30)
        new_user["command"] = self.new_user

        importy = tk.Button(root)
        importy["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        importy["font"] = ft
        importy["fg"] = "#000000"
        importy["justify"] = "center"
        importy["text"] = "Importovat data z CSV"
        importy.place(x=500, y=320, width=341, height=30)
        importy["command"] = self.importy

        viewy = tk.Button(root)
        viewy["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        viewy["font"] = ft
        viewy["fg"] = "#000000"
        viewy["justify"] = "center"
        viewy["text"] = "Viewy"
        viewy.place(x=500, y=390, width=341, height=30)
        viewy["command"] = self.viewy

        zakaznici = tk.Button(root)
        zakaznici["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        zakaznici["font"] = ft
        zakaznici["fg"] = "#000000"
        zakaznici["justify"] = "center"
        zakaznici["text"] = "Seznam zákazníků"
        zakaznici.place(x=500, y=460, width=341, height=30)
        zakaznici["command"] = self.zakaznici

        pracovnici = tk.Button(root)
        pracovnici["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        pracovnici["font"] = ft
        pracovnici["fg"] = "#000000"
        pracovnici["justify"] = "center"
        pracovnici["text"] = "Výpis pracovníků"
        pracovnici.place(x=500, y=530, width=341, height=30)
        pracovnici["command"] = self.pracovnici

        filmy = tk.Button(root)
        filmy["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        filmy["font"] = ft
        filmy["fg"] = "#000000"
        filmy["justify"] = "center"
        filmy["text"] = "Seznam filmů"
        filmy.place(x=500, y=600, width=341, height=30)
        filmy["command"] = self.filmy

    def redirect_to_profile(self):
        # check if user window is already open
        if self.user_window is None:
            # open a new window for the user profile
            self.user_window = src.profile.UserInfoWindow(self.root, self.logged_in_user, self.role(), self.pohlavi())
            # bind closing event to handle window close
            self.user_window.window.protocol("WM_DELETE_WINDOW", self.handle_user_window_close)
        else:
            self.user_window.window.deiconify()

    def pracovnici(self):
        role = self.role()
        if role =="Admin":
            root = tk.Tk()
            app = src.admins.Pracovnici(master=root)
            app.mainloop()
        else:
            messagebox.showerror("Chyba", "Do této sekce může pouze admin!")

    def filmy(self):
        root = tk.Tk()
        app = src.filmy.Filmy(master=root)
        app.mainloop()



    def handle_user_window_close(self):
        # reset user window variable when window is closed
        self.user_window.window.destroy()
        self.user_window = None




    def new_user(self):

        if not self.is_zakaznik_open:
            root = tk.Tk()
            zkz = src.zakaznik.Zakaznik(root)
            self.is_zakaznik_open = True
            self.zakaznik_window = root
            root.protocol("WM_DELETE_WINDOW",
                          lambda: self.handle_zakaznik_close(root))
            root.mainloop()
        else:
            root = self.zakaznik_window
            root.deiconify()

    def handle_zakaznik_close(self, root):
        self.is_zakaznik_open = False
        root.destroy()

    def GButton_843_command(self):
        if not self.is_rezervace_open:
            root = tk.Tk()
            rez = src.rezervace.ReservationEditor(root)
            self.is_rezervace_open = True
            self.rezervace_window = root
            root.protocol("WM_DELETE_WINDOW",
                          lambda: self.handle_registrace_close(root))
            root.mainloop()
        else:
            root = self.rezervace_window
            root.deiconify()

    def importy(self):
        open_drag_and_drop_window()

    def role(self):
        jmeno = self.logged_in_user
        spravce = admin.Admin()
        role = spravce.get_role(jmeno)
        return role[0]

    def pohlavi(self):
        jmeno = self.logged_in_user
        uzivatel = admin.Admin()
        pohlavi = uzivatel.get_pohlavi(jmeno)
        return pohlavi[0]

    def viewy(self):
        if not self.is_views_open:
            root = tk.Tk()
            views = src.view.View(root)
            self.is_views_open = True
            self.viewy_window = root
            root.protocol("WM_DELETE_WINDOW",
                          lambda: self.handle_view_close(root))
            root.mainloop()
        else:
            root = self.viewy_window
            root.deiconify()

    def handle_view_close(self, root):
        self.is_views_open = False
        root.destroy()

    def zakaznici(self):
        app = src.delZakaznik.Zakaznici()








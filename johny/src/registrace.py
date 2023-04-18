import src.registraceDAO
import tkinter as tk
import tkinter.font as tkFont
import re


class Registrace:
    def __init__(self, root):
        # setting title
        self.root = root

        self.radio_var = None
        root.title("Registrace")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_197 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_197["font"] = ft
        GLabel_197["fg"] = "#333333"
        GLabel_197["justify"] = "center"
        GLabel_197["text"] = "jméno"
        GLabel_197.place(x=80, y=30, width=160, height=30)

        GLabel_734 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_734["font"] = ft
        GLabel_734["fg"] = "#333333"
        GLabel_734["justify"] = "center"
        GLabel_734["text"] = "heslo"
        GLabel_734.place(x=80, y=70, width=160, height=30)

        GRadio_571 = tk.Radiobutton(root, variable=self.radio_var, value="1")
        ft = tkFont.Font(family='Times', size=10)
        GRadio_571["font"] = ft
        GRadio_571["fg"] = "#333333"
        GRadio_571["justify"] = "center"
        GRadio_571["text"] = "Muž"
        GRadio_571.place(x=140, y=150, width=120, height=25)
        GRadio_571["command"] = self.GRadio_571_command

        GRadio_17 = tk.Radiobutton(root, variable=self.radio_var, value="2")
        ft = tkFont.Font(family='Times', size=10)
        GRadio_17["font"] = ft
        GRadio_17["fg"] = "#333333"
        GRadio_17["justify"] = "center"
        GRadio_17["text"] = "Žena"
        GRadio_17.place(x=280, y=150, width=120, height=25)
        GRadio_17["command"] = self.GRadio_572_command

        self.GLineEdit_448 = tk.Entry(root)
        self.GLineEdit_448["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_448["font"] = ft
        self.GLineEdit_448["fg"] = "#333333"
        self.GLineEdit_448["justify"] = "center"
        self.GLineEdit_448["text"] = "jm"
        self.GLineEdit_448.place(x=250, y=30, width=100, height=25)

        self.GLineEdit_239 = tk.Entry(root, show="*")
        self.GLineEdit_239["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_239["font"] = ft
        self.GLineEdit_239["fg"] = "#333333"
        self.GLineEdit_239["justify"] = "center"
        self.GLineEdit_239["text"] = "he"
        self.GLineEdit_239.place(x=250, y=70, width=100, height=25)

        GLabel_678 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_678["font"] = ft
        GLabel_678["fg"] = "#333333"
        GLabel_678["justify"] = "center"
        GLabel_678["text"] = "heslo znovu"
        GLabel_678.place(x=80, y=110, width=160, height=25)

        self.GLineEdit_81 = tk.Entry(root, show="*")
        self.GLineEdit_81["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_81["font"] = ft
        self.GLineEdit_81["fg"] = "#333333"
        self.GLineEdit_81["justify"] = "center"
        self.GLineEdit_81["text"] = "he2"
        self.GLineEdit_81.place(x=250, y=110, width=100, height=25)

        self.GListBox_53 = tk.Listbox(root)
        self.GListBox_53["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GListBox_53["font"] = ft
        self.GListBox_53["fg"] = "#333333"
        self.GListBox_53["justify"] = "center"
        self.GListBox_53.insert(1, "Admin")
        self.GListBox_53.insert(2, "Pokladní")
        self.GListBox_53.insert(3, "Manager")
        self.GListBox_53.place(x=250, y=190, width=100, height=70)

        self.GButton_870 = tk.Button(root)
        self.GButton_870["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.GButton_870["font"] = ft
        self.GButton_870["fg"] = "#000000"
        self.GButton_870["justify"] = "center"
        self.GButton_870["text"] = "potvrdit"
        self.GButton_870.place(x=270, y=260, width=70, height=25)
        self.GButton_870["command"] = self.GButton_870_command

        GButton_303 = tk.Button(root)
        GButton_303["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_303["font"] = ft
        GButton_303["fg"] = "#000000"
        GButton_303["justify"] = "center"
        GButton_303["text"] = "vymazat"
        GButton_303.place(x=140, y=260, width=70, height=25)
        GButton_303["command"] = self.GButton_303_command

        GLabel_476 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_476["font"] = ft
        GLabel_476["fg"] = "#333333"
        GLabel_476["justify"] = "center"
        GLabel_476["text"] = "role"
        GLabel_476.place(x=80, y=190, width=160, height=25)

    def GRadio_571_command(self):
        self.radio_var = 0

    def GRadio_572_command(self):
        self.radio_var = 1

    def display_error(self, message):
        error_label = tk.Label(self.root)
        error_label ["text"]=message
        error_label ["fg"]="red"
        ft = tkFont.Font(family='Times', size=10)
        error_label["font"] = ft
        error_label["justify"] = "center"
        error_label.place(x=250, y=360)

    def remove_error(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget('fg') == 'red':
                widget.destroy()

    def GButton_870_command(self):
        selected_indexes = self.GListBox_53.curselection()
        role = None
        for index in selected_indexes:
            value = self.GListBox_53.get(index)
            role = value
        jmeno = self.GLineEdit_448.get()
        heslo = self.GLineEdit_239.get()
        heslo_kon = self.GLineEdit_81.get()
        specialni_znaky = "!@#$%^&*()-+?_=,<>/"
        if not jmeno:
            self.remove_error()
            self.display_error("Error: username or password cannot be empty.")
        elif len(jmeno) < 2 or len(jmeno) > 20:
            self.remove_error()
            self.display_error("Délka jména je mimo rozsah.")
        elif not re.match(r'^\w+$', jmeno):
            self.remove_error()
            self.display_error("Jméno nesmí obsahovat speciální znaky.")
        elif not heslo or not heslo_kon:
            self.remove_error()
            self.display_error("prazdne.")
        elif len(heslo) < 5 or len(heslo) > 20 or len(heslo_kon) < 5 or len(heslo_kon) > 20:
            self.remove_error()
            self.display_error("mimo royzash.")
        elif not any(char in specialni_znaky for char in heslo) \
                or not any(char in specialni_znaky for char in heslo_kon):
            self.remove_error()
            self.display_error("special ynak.")
        elif heslo != heslo_kon:
            self.remove_error()
            self.display_error("neshoduji se")
        elif self.radio_var == None:
            self.remove_error()
            self.display_error("vyberte pohlaví")
        elif not role:
            self.remove_error()
            self.display_error("vyberte roli")
        else:
            self.remove_error()
            try:
                registration = src.registraceDAO.registraceDB()
                send = registration.registrace(jmeno, heslo, self.radio_var, role)
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
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        x = (screen_width - popup.winfo_reqwidth()) / 2
        y = (screen_height - popup.winfo_reqheight()) / 2
        popup.geometry("+%d+%d" % (x, y))
        label = tk.Label(popup)
        label ["text"]="Registrace proběhla úspěšně!"
        ft = tkFont.Font(family='Times', size=10)
        label["font"] = ft
        label["fg"] = "#333333"
        label["justify"] = "center"
        label.pack(pady=10)

        ok_button = tk.Button(popup)
        ok_button ["text"]="OK"
        ft = tkFont.Font(family='Times', size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#333333"
        ok_button["justify"] = "center"
        ok_button ["command"]=popup.destroy
        ok_button.pack()

    def GButton_303_command(self):
        self.GLineEdit_448.delete(0, "end")
        self.GLineEdit_239.delete(0, "end")
        self.GLineEdit_81.delete(0, "end")
        self.GListBox_53.selection_clear(0, "end")

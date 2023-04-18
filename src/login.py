import tkinter as tk
import tkinter.font as tkFont
import src.registrace
import src.loginDAO
import src.adminDAO
import src.mainWindow2 as mw
import hashlib

from dbConn import databaseConnector
class Login:
    logged_in_user = None
    def __init__(self, root):
        self.root = root
        root.title("Login")
        self.database_connection = databaseConnector.MySQLConnection.getInstance()
        self.is_registrace_open = False

        width=506
        height=408
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_739=tk.Button(root)
        GButton_739["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_739["font"] = ft
        GButton_739["fg"] = "#000000"
        GButton_739["justify"] = "center"
        GButton_739["text"] = "přihlásit se"
        GButton_739.place(x=280,y=320,width=113,height=30)
        GButton_739["command"] = self.GButton_739_command

        registrace = tk.Button(root)
        registrace["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        registrace["font"] = ft
        registrace["fg"] = "#000000"
        registrace["justify"] = "center"
        registrace["text"] = "registrace"
        registrace.place(x=120, y=320, width=113, height=30)
        registrace["command"] = self.registrace_cmd

        self.GLineEdit_766=tk.Entry(root, show="*")
        self.GLineEdit_766["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_766["font"] = ft
        self.GLineEdit_766["fg"] = "#333333"
        self.GLineEdit_766["justify"] = "center"
        self.GLineEdit_766["text"] = "heslo"
        self.GLineEdit_766.place(x=200,y=220,width=132,height=30)
        self.GLineEdit_766.bind('<Return>', lambda event: self.GButton_739_command())

        GLabel_974=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_974["font"] = ft
        GLabel_974["fg"] = "#333333"
        GLabel_974["justify"] = "center"
        GLabel_974["text"] = "heslo"
        GLabel_974.place(x=100, y=220, width=70, height=25)

        GLabel_150 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_150["font"] = ft
        GLabel_150["fg"] = "#333333"
        GLabel_150["justify"] = "center"
        GLabel_150["text"] = "jméno"
        GLabel_150.place(x=100, y=170, width=70, height=25)

        self.GLineEdit_279 = tk.Entry(root)
        self.GLineEdit_279["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_279["font"] = ft
        self.GLineEdit_279["fg"] = "#333333"
        self.GLineEdit_279["justify"] = "center"
        self.GLineEdit_279["text"] = "jméno"
        self.GLineEdit_279.place(x=200, y=170, width=133, height=30)

    def display_error(self, message):
        error_label = tk.Label(self.root)
        error_label["text"] = message
        error_label["fg"] = "red"
        error_label.place(x=250, y=360)

    def remove_error(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget('fg') == 'red':
                widget.destroy()

    def registrace_cmd(self):
        if not self.is_registrace_open:
            root = tk.Tk()
            registrace = src.registrace.Registrace(root)
            self.is_registrace_open = True
            self.registrace_window = root
            root.protocol("WM_DELETE_WINDOW", lambda: self.handle_registrace_close(root))
            root.mainloop()
        else:
            root = self.registrace_window
            root.deiconify()

    def handle_registrace_close(self,root):
        self.is_registrace_open = False
        root.destroy()
    def GButton_739_command(self):
        def hash_password(password):
            """Hashes a password using SHA-256."""
            salt = b'somesalt'  # Change this to a random value for production use
            password = password.encode('utf-8')
            return hashlib.sha256(salt + password).hexdigest()
        username = self.GLineEdit_279.get()
        password = self.GLineEdit_766.get()

        if username == '' or password == '':
            self.remove_error()
            self.display_error("Error: username or password cannot be empty.")

        elif len(username) < 2 or len(username) > 20:
            self.remove_error()
            self.display_error("Error: username must be between 3 and 20 characters long.")
            # Query the database to check if the username and password combination exists
        elif len(password) < 4 or len(password) > 20:
            self.remove_error()
            self.display_error("Error: password must be between 4 and 20 characters long.")
        else:
            hashed_password = hash_password(password)
            login = src.loginDAO.loginDB()
            result = login.prihlaseni(username, hashed_password)


            if result:
                # If the query returns a result, the user is authenticated
                self.logged_in_user = username
                self.root.destroy()
                user = src.adminDAO.Admin()
                user_id = user.get_id(self.logged_in_user)
                root = tk.Tk()
                app = mw.App(root, logged_in_user=user_id[0])
                root.mainloop()

                # Add code here to navigate to the main application window
            else:
                # If the query returns no result, the user is not authenticated
                self.remove_error()
                self.display_error("Invalid username or password")

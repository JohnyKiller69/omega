import tkinter as tk
import tkinter.font as tkFont
import src.viewDAO
class View:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_504=tk.Button(root)
        GButton_504["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_504["font"] = ft
        GButton_504["fg"] = "#000000"
        GButton_504["justify"] = "center"
        GButton_504["text"] = "Výdělek"
        GButton_504.place(x=40,y=30,width=160,height=30)
        GButton_504["command"] = self.GButton_504_command

        GButton_60=tk.Button(root)
        GButton_60["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_60["font"] = ft
        GButton_60["fg"] = "#000000"
        GButton_60["justify"] = "center"
        GButton_60["text"] = "Návštěvnost"
        GButton_60.place(x=40,y=170,width=160,height=30)
        GButton_60["command"] = self.GButton_60_command

        self.text_widget = tk.Text(root, wrap=tk.NONE, width=300, height=300)
        self.text_widget.place(x=250, y=0, width=350, height=300)

        scroll_y = tk.Scrollbar(self.text_widget, orient=tk.VERTICAL, command=self.text_widget.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scroll_y.set)

        scroll_x = tk.Scrollbar(self.text_widget, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_widget.config(xscrollcommand=scroll_x.set)

    def GButton_504_command(self):
        view_instance = src.viewDAO.Viewy()
        data = view_instance.vydelek()
        self.show_view_window('Vydelek', data)


    def show_view_window(self, window_title, data):
        if data.empty:
            return

        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, window_title + "\n")
        self.text_widget.insert(tk.END, "-" * 30 + "\n")

        column_count = len(data.columns)

        # Find the maximum width for each column
        column_widths = [max(data[col].apply(lambda x: len(str(x)))) for col in data.columns]

        # Display column values
        for index, row in data.iterrows():
            if row is None:
                self.text_widget.insert(tk.END, "None\n")
            else:
                for col in range(column_count):
                    cell_value = str(row[col])
                    cell_width = column_widths[col]

                    # Center the cell value based on the column width
                    centered_value = cell_value.center(cell_width)
                    self.text_widget.insert(tk.END, f"{centered_value}\t")
                self.text_widget.insert(tk.END, "\n")

        self.text_widget.config(state=tk.DISABLED)


    def GButton_60_command(self):
        view_instance = src.viewDAO.Viewy()
        data = view_instance.nejsledovanejsi()
        self.show_view_window('Nejsledovanejsi', data)




import tkinter as tk
from tkinter import ttk
import csv
import os
import src.promitaniDAO
import src.filmDAO
from tkinterdnd2 import DND_FILES, TkinterDnD

import threading

drag_window_lock = threading.Lock()

def load_data_to_array(file_path):
    """
    Metod slouží k načtení kódu z CSV souboru a převední do pole.
    :param file_path: Cesta k souboru.
    :return: Pole s načtenými daty.
    """
    data = []
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

def on_drop(event):
    """

    :param event: Přetáhnutí souboru.
    :return: None.
    """
    global data_array
    dropped_file_path = event.data.strip("{}")
    if os.path.splitext(dropped_file_path)[1].lower() == ".csv":
        data_array = load_data_to_array(dropped_file_path)
        display_data(data_array)

def save_data_to_table(table_name):
    global data_array
    if data_array:
        if table_name == "promitani":
            try:
                insert = src.promitaniDAO.promitani()
                for row in data_array[1:]:
                    insert.insert(row[0],row[1],row[2],row[3],row[4])
                succes()
            except:
                show_popup()

        elif table_name == "film":
            try:
                insert = src.filmDAO.film()
                for row in data_array[1:]:  # Přeskočíme první řádek, protože obsahuje názvy sloupců
                    insert.insert_film(row[0], row[1], row[2], row[3])
                succes()
            except:
                show_popup()
        text_widget.delete("1.0", tk.END)
        data_array = None

def display_data(data_array):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    for row in data_array:
        text_widget.insert(tk.END, ','.join(row) + '\n')
    text_widget.config(state=tk.DISABLED)

def open_drag_and_drop_window():
    if not drag_window_lock.acquire(blocking=False):
        return
    root = TkinterDnD.Tk()
    root.geometry("400x300")
    root.title("Drag and Drop CSV")

    global data_array
    data_array = None

    label = ttk.Label(root)
    label ["text"]="Přetáhněte sem CSV soubor"
    label ["font"]=("Arial", 16)
    label.pack(expand=True, pady=20)

    kino_button = ttk.Button(root)
    kino_button ["text"]="Uložit do tabulky Promítání"
    kino_button ["command"]=lambda: save_data_to_table("promitani")
    kino_button.pack(expand=True, pady=10)

    promitani_button = ttk.Button(root)
    promitani_button ["text"]="Uložit do tabulky Film"
    promitani_button ["command"]=lambda: save_data_to_table("film")
    promitani_button.pack(expand=True, pady=10)

    global text_widget
    text_widget = tk.Text(root)
    text_widget ["wrap"]=tk.NONE
    text_widget.pack(expand=True, fill=tk.BOTH)
    text_widget.config(state=tk.DISABLED)

    def on_close():
        drag_window_lock.release()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()


def show_popup():
    popup = tk.Toplevel()
    popup.title("Neúspěšný import!")
    popup.geometry("300x100")
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width - popup.winfo_reqwidth()) / 2
    y = (screen_height - popup.winfo_reqheight()) / 2
    popup.geometry("+%d+%d" % (x, y))
    label = tk.Label(popup)
    label ["text"]="Import dat neproběhl. Zkuste soubor vložit znovu."
    label.pack(pady=10)
    ok_button = tk.Button(popup)
    ok_button ["text"]="OK"
    ok_button ["command"]=popup.destroy
    ok_button.pack()

def succes():
    popup = tk.Toplevel()
    popup.title("Úspěšný import!")
    popup.geometry("300x100")
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width - popup.winfo_reqwidth()) / 2
    y = (screen_height - popup.winfo_reqheight()) / 2
    popup.geometry("+%d+%d" % (x, y))
    label = tk.Label(popup)
    label ["text"]="Data se uložila do databáze."
    label.pack(pady=10)
    ok_button = tk.Button(popup)
    ok_button ["text"]="OK"
    ok_button ["command"]=popup.destroy
    ok_button.pack()

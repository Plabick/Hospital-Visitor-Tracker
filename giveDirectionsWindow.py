import tkinter as tk
from tkinter import messagebox

import dbUtils as db


def giveDirections():
    def findDirections():
        print(f"finding directions for {vfn.get()} {vln.get()}")
        message = db.getDirections(vfn.get(), vln.get())
        messagebox.showinfo("Directions", f"{vfn.get()} {vln.get()} is going to {message}")
        master.destroy()  # close window once directions given

    master = tk.Tk()
    master.title("Visitor Directions")

    tk.Label(master,
             text="Visitor First Name").grid(row=0)
    tk.Label(master,
             text="Visitor Last Name").grid(row=1)

    vfn = tk.Entry(master)  # visitor first name
    vln = tk.Entry(master)  # visitor last name
    find = tk.Button(master, text='Find', command=findDirections)

    vfn.grid(row=0, column=1)
    vln.grid(row=1, column=1)
    find.grid(row=2, column=1)

    master.mainloop()

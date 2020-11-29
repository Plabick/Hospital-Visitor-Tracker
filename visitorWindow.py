import tkinter as tk
from tkinter import messagebox
from dbUtils import canHaveVisitor

import dbUtils as db


def visitorWindow():
    def quit():
        master.destroy()  # Exit Window

    def addVistor():
        # Add the visitor or return an error
        if(canHaveVisitor(pfn.get(),pln.get())):
         # pfn, pln, vfn, vln, exposure, oos, symptoms, screenerID
             message = db.addVisitor(pfn.get(), pln.get(), vfn.get(), vln.get(), False, False, False, 1)

             messagebox.showinfo("Visit Approved",
                                f"{vfn.get()} {vln.get()} is approved to visit {pfn.get()} {pln.get()} today"
                                f".\nLocation: {message}")
        else:
            messagebox.showerror("Do Not Admit", f"{vfn.get()} {vln.get()} can not visit {pfn.get()} {pln.get()} today")


    master = tk.Tk()
    master.title("Add Visitor")

    tk.Label(master,
             text="Visitor First Name").grid(row=0)
    tk.Label(master,
             text="Visitor Last Name").grid(row=1)

    tk.Label(master,
             text="Patient First Name").grid(row=2)

    tk.Label(master,
             text="Patient Last name").grid(row=3)
    tk.Label(master,
             text="OOS Travel?").grid(row=4)
    tk.Label(master,
             text="COVID-19 Exposure?").grid(row=5)
    tk.Label(master,
             text="COVID-19 Symptoms?").grid(row=6)

    vfn = tk.Entry(master)  # visitor first name
    vln = tk.Entry(master)  # visitor last name
    pfn = tk.Entry(master)  # patient first name
    pln = tk.Entry(master)  # patient last name

    tk.Button(master, text="Quit", command=quit).grid(row=7, column=1)
    tk.Button(master, text="Add", command=addVistor).grid(row=7)
    oosVar = tk.IntVar()
    oos = tk.Checkbutton(master, variable=oosVar)
    symptomsVar = tk.IntVar()
    symptoms = tk.Checkbutton(master, variable=symptomsVar)
    exposureVar = tk.IntVar()
    exposure = tk.Checkbutton(master, variable=exposureVar)

    vfn.grid(row=0, column=1)
    vln.grid(row=1, column=1)
    pfn.grid(row=2, column=1)
    pln.grid(row=3, column=1)
    oos.grid(row=4, column=1)
    symptoms.grid(row=5, column=1)
    exposure.grid(row=6, column=1)

    master.mainloop()

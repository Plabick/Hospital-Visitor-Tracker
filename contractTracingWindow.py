import tkinter as tk
from tkinter import messagebox

from dbUtils import contactTracePatient, contactTraceVisitor


def contractTrace():
    def contractTraceVisitor():
        print(f"contract tracing for visitor {vfn.get()} {vln.get()}")
        message = contactTraceVisitor(vfn.get(), vln.get())
        messagebox.showinfo("Contract Tracing Report", f"The following people had contact with {pfn.get()} {pln.get()} "
                                                       f"in the last 14 days\n{message}")

    def contractTracePatient():
        print(f"contract tracing for patient {pfn.get()} {pln.get()}")
        message = contactTracePatient(pfn.get(), pln.get())
        messagebox.showinfo("Contract Tracing Report", f"The following people had contact with {vfn.get()} {vln.get()} "
                                                       f"in the last 14 days\n{message}")

        ## do the query

    master = tk.Tk()
    master.title("ContractTracing")

    tk.Label(master, text="Visitor First Name").grid(row=0)
    tk.Label(master, text="Visitor Last Name").grid(row=1)
    tk.Label(master, text="OR").grid(row=2)
    tk.Label(master, text="Patient First Name").grid(row=3)
    tk.Label(master, text="Patient Last Name").grid(row=4)

    vfn = tk.Entry(master)  # visitor first name
    vln = tk.Entry(master)  # visitor last name
    pfn = tk.Entry(master)  # patient first name
    pln = tk.Entry(master)  # patient last name
    vct = tk.Button(master, text='Contact Trace Visitor', command=contractTraceVisitor)  # visitor contact trace
    pct = tk.Button(master, text='Contact Trace Patient', command=contractTracePatient)

    vfn.grid(row=0, column=1)
    vln.grid(row=1, column=1)
    pfn.grid(row=3, column=1)
    pln.grid(row=4, column=1)
    vct.grid(row=5, column=0)
    pct.grid(row=5, column=1)

    master.mainloop()

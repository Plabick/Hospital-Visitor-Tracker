import tkinter as tk
from tkinter import messagebox

from dbUtils import wrongPersonAdmitted, avgTimeToScreen


def performanceReview():
    def checkPerformance():
        print(f"Calculating performance report for {vfn.get()} {vln.get()}")
        result = wrongPersonAdmitted(vfn.get(), vln.get())
        result2 = avgTimeToScreen(vfn.get(),vln.get())
        messagebox.showinfo("Performance Report" ,f"{vfn.get()} {vln.get()}\nSick Visitors Let In: {result}"
                                                 f"\nAverage Time To Screen: {result2}")


    master = tk.Tk()
    master.title("Employee Performance")

    tk.Label(master,
             text="Screener First Name").grid(row=0)
    tk.Label(master,
             text="Screener Last Name").grid(row=1)

    vfn = tk.Entry(master)  # visitor first name
    vln = tk.Entry(master)  # visitor last name
    find = tk.Button(master, text='Compute', command=checkPerformance)

    vfn.grid(row=0, column=1)
    vln.grid(row=1, column=1)
    find.grid(row=2, column=1)

    master.mainloop()

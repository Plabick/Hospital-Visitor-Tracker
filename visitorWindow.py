import tkinter as tk


def visitorWindow():
    def addVistor():
        print("VISITOR\nFirst Name: %s\nLast Name: %s" % (vfn.get(), vln.get()))
        print("PATIENT\nFirst Name: %s\nLast Name: %s" % (pfn.get(), pln.get()))
        ##Add the visitor or return an error
        master.destroy()  # Exit Window

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

    tk.Button(master, text="Add", command=addVistor).grid(row=7)
    var1 = tk.IntVar()
    oos = tk.Checkbutton(master, variable=var1)
    var2 = tk.IntVar()
    symptoms = tk.Checkbutton(master, variable=var2)
    var3 = tk.IntVar()
    exposure = tk.Checkbutton(master, variable=var3)

    vfn.grid(row=0, column=1)
    vln.grid(row=1, column=1)
    pfn.grid(row=2, column=1)
    pln.grid(row=3, column=1)
    oos.grid(row=4, column=1)
    symptoms.grid(row=5, column=1)
    exposure.grid(row=6, column=1)

    master.mainloop()

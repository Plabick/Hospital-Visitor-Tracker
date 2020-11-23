import tkinter as tk


def giveDirections():
    def findDirections():
        print(f"finding directions for {vfn.get()} {vln.get()}")
        ## do the query

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

from tkinter import *
import visitorWindow
import giveDirectionsWindow
import contractTracingWindow
import employeePerformanceWindow

window = Tk()
window.title("Visitor Screening Tool")
window.geometry('155x200')

lbl = Label(window, text="Hello")

window.configure(bg='#ffffff')

photo = PhotoImage(file='logo.ppm')
photo = photo.subsample(2)
label = Label(image=photo)
label.grid(column=0, row=0)


def addVisitorWindow():
    visitorWindow.visitorWindow()


def getDirectionsWindow():
    giveDirectionsWindow.giveDirections()


def contactTraceWindow():
    contractTracingWindow.contractTrace()


def analyticsWindow():
    employeePerformanceWindow.performanceReview()


addVisitor = Button(window, text="Add a Visitor", command=addVisitorWindow)
getDirections = Button(window, text="Give Directions", command=getDirectionsWindow)
contractTrace = Button(window, text="Contract Tracing", command=contactTraceWindow)
analytics = Button(window, text="Employee Performance", command=analyticsWindow)

addVisitor.grid(column=0, row=1)
getDirections.grid(column=0, row=2)
contractTrace.grid(column=0, row=3)
analytics.grid(column=0, row=4)

window.mainloop()

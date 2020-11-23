import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="visitorDBUser",
    password="password",
    database="visitordb"
)

mycursor = mydb.cursor()

## Test of DB connection
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


def addVisitor(pfn, pln, vfn, vln, exposure, oos, symptoms, screener):
    # Insert visitor into visitor database
    # First check if visitor is eligible to visit
    # Then check if patient can receive visitor
    # Add a visit to the visit db if possible
    # Return "Unable to enter due to {reason}" or "Cleared to enter, go to {location}"
    print("addVisitor called")
    return "TEST LOCATION"


def getDirections(vfn, vln):
    # Return location of patient connected to visitor or error
    print("get directions called")


def contactTracePatient(pfn, pln):
    # Return visitors who visited  patient in the last 14 days
    print("contactTracePatient called")


def contactTraceVisitor(vfn, vln):
    # Return screeners, patients, and visitors who interacted with visitor in the last 14 days
    print("contactTracePatient called")


def wrongPersonAdmitted(efn, eln):  # employee first name, last name
    # Return number of wrong visitors allowed in by a screener as a string (or "none")
    print("wrongPersonAdmitted called")


def avgTimeToScreen(efn, eln):  # employee first name, last name
    # return Avg time visitors spend in lobby connected to given screener
    print("avgTimeToScreen called")

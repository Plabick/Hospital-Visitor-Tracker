import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="visitorDBUser",
    password="password",
    database="visitordb"
)

mycursor = mydb.cursor()


## Test of DB connection
# mycursor.execute("SHOW TABLES")


def addVisitor(pfn, pln, vfn, vln, exposure, oos, symptoms, screener):
    # Insert visitor into visitor database
    # First check if visitor is eligible to visit
    # Then check if patient can receive visitor
    # Add a visit to the visit db if possible
    # Return destination {location}"
    return "TEST LOCATION"

def canHaveVisitor(pfn,pln):
   query = f"select patient_eol = true or patient_precaution = \"none\" from patient " \
           f"where patient_first_name = \"{pfn}\" and patient_last_name = \"{pln}\";"

   mycursor.execute(query)

   for(x) in mycursor:
    result = x
    x = cleanString(repr(x))
    return eval(x)



def getDirections(vfn, vln):
    # Return location of patient connected to visitor or error
    name = f"{vfn} {vln}"
    mycursor.execute(f" select patient_building, patient_room from visit join visitor using (visitor_id) join patient "
                     f"using (patient_id) where visitor_name =\"{name}\";")

    return cleanString(repr(mycursor.next()))


def contactTracePatient(pfn, pln):
    # Return visitors who visited  patient in the last 14 days
    pfn = repr(pfn).replace(" ", "")
    pln = repr(pln).replace(" ", "")

    print("contactTracePatient called")
    query = f"select visitor_name from visit join visitor using (visitor_id) join patient using (patient_id) where " \
            f"patient_first_name ={pfn} and patient_last_name ={pln}; "
    mycursor.execute(query)
    result = "Visitors:\n"
    for (x) in mycursor:
        result += f"{cleanString(repr(x))}\n"
    print(result)
    return result


def contactTraceVisitor(vfn, vln):
    # Return screeners and patients who interacted with the given visitor in the last 14 days

    print("contactTraceVisitor called")

    query = f"select patient_first_name, patient_last_name from visit join visitor using (visitor_id) join patient " \
            f"using (patient_id) where " \
            f"visitor_name like \"{vfn} {vln}\";"

    result = "\nPatients:\n"

    mycursor.execute(query)
    for (x) in mycursor:
        result += f"{cleanString(repr(x))}\n"

    result += "\nScreeners:\n"
    query = f"select screener_name from visit join visitor using (visitor_id) join patient " \
            f"using (patient_id) join screener using (screener_id) where " \
            f"visitor_name = \"{vfn} {vln}\"; "

    mycursor.execute(query)
    for (x) in mycursor:
        result += f"{cleanString(repr(x))}\n"

    print(result)
    return result


def wrongPersonAdmitted(efn, eln):  # employee first name, last name
    # Return number of wrong visitors allowed in by a screener as a string (or "none")
    print("wrongPersonAdmitted called")


def avgTimeToScreen(efn, eln):  # employee first name, last name
    # return Avg time visitors spend in lobby connected to given screener
    print("avgTimeToScreen called")


# Utility method to clean the given query result into a string
def cleanString(str):
    str = str.replace('(', '').replace(')', '').replace(',', '').replace('\'', '')
    return str

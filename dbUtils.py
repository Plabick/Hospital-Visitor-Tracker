from datetime import date, time, datetime

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

    query = f"insert into visitor(visitor_name) values(\"{vfn} {vln}\");"
    mycursor.execute(query)

    patientID = findPatientID(pfn, pln);
    print("PID: ", patientID)
    visitorID = findVisitorID(vfn,vln);
    print("VID: ", visitorID)


    query = f"insert into visit(patient_id , screener_id , visitor_id, visit_date, visit_start, visit_end, let_in)\
     values (\"{patientID}\",1,\"{visitorID}\",CURDATE(),CURTIME(),CURTIME(), true);"
    mycursor.execute(query)

    return getDirections(vfn, vln)

def canHaveVisitor(pfn, pln):
    query = f"select patient_eol = true or patient_precaution = \"none\" from patient " \
            f"where patient_first_name = \"{pfn}\" and patient_last_name = \"{pln}\";"

    mycursor.execute(query)

    for (x) in mycursor:
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
    query = f"select TIME_FORMAT(TIME(AVG(SUBTIME(visit_end, visit_start))), \"%H:%i:%s\") from screener \
      join visit using (screener_id) where screener_name = \"{efn} {eln}\""

    mycursor.execute(query)
    result = "999"
    for (x) in mycursor:
        result = f"{cleanString(repr(x))}\n"
    return result


def avgTimeToScreen(efn, eln):  # employee first name, last name
    # return Avg time visitors spend in lobby connected to given screener
    print("avgTimeToScreen called")


# Utility method to clean the given query result into a string
def cleanString(str):
    str = str.replace('(', '').replace(')', '').replace(',', '').replace('\'', '')
    return str

def findPatientID(pfn,pln):
   query = f"select patient_id from patient where patient_first_name =\"{pfn}\" and patient_last_name =\"{pln}\";"

   mycursor.execute(query)

   result = "null"
   for (x) in mycursor:
       result = f"{cleanString(repr(x))}\n"

   return int(result)

def findVisitorID (vfn, vln):
    query = f"select visitor_id from visitor where visitor_name =\"{vfn} {vln}\";"

    mycursor.execute(query)

    result = "null"
    for (x) in mycursor:
        result = f"{cleanString(repr(x))}\n"

    return int(result)
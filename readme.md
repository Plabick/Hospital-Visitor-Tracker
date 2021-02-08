# Hospital Visitor Database

This project is an SQL database and related python application for a hospital to track and manage visitors during the covid-19 pandemic. The application was made with business logic based on the [Mass General Brigham Visitor Rules](https://www.massgeneralbrigham.org/covid19/visitor-policy) as of November 3rd, 2020. 

Features:
* Visitor Management
  * Add visitors, record their answer to screening questions, and link them to a patient
  * Determine if a patient is eligible to receive a visitor for the day
  * Record personal exceptions to visitation rules
* PHI-free directions
  * Once a patient and visitor are linked, the visitor can ask staff for directions to the patient's room without exchanging information about the patient. The visitor can give their name to the program and get their destination without providing the patient's name or DOB.
* Contract Tracing
  * Find visitors who had contact with an infected patient, patients who had contact with an infected visitor, and visitors who had contact with infected staff in the last *n* days.
* Employee Performance Review
  * Ties in data from the EHR to determine if screeners let in visitors who should not have been allowed in
  * Calculates the average time a screen takes to screen one visitor

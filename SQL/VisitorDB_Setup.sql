-- To use the python code as is, plz set up your system like this
-- USER: visitorDBUser
-- PASSWORD: password
drop schema if exists visitorDB;
CREATE SCHEMA visitorDB;
use visitorDB;

DROP TABLE IF EXISTS patient;
CREATE TABLE IF NOT EXISTS patient (
  patient_id INT NOT NULL,
  patient_first_name VARCHAR(50) NOT NULL,
  patient_last_name VARCHAR(50) NOT NULL,
  patient_dob DATE,
  patient_classification ENUM("inpatient", "outpatient", "icu", "er", "ob") NOT NULL,
  patient_precaution ENUM("none", "contact", "airborne") NOT NULL,
  patient_eol TINYINT NOT NULL,
  patient_building ENUM("Tower", "CWN", "Shapiro", "Hale") NULL,
  patient_room INT NULL,
  PRIMARY KEY (patient_id));


DROP TABLE IF EXISTS visitor ;
CREATE TABLE IF NOT EXISTS visitor (
  visitor_id INT NOT NULL,
  visitor_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (visitor_id));


DROP TABLE IF EXISTS screener ;
CREATE TABLE IF NOT EXISTS screener (
  screener_id INT NOT NULL,
  screener_name VARCHAR(50) NOT NULL,
  screener_station INT NOT NULL,
  PRIMARY KEY (screener_id));


DROP TABLE IF EXISTS visit ;
CREATE TABLE IF NOT EXISTS visit (
  visit_id INT NOT NULL,
  patient_id INT NOT NULL,
  screener_id INT NOT NULL,
  visitor_id INT NOT NULL,
  visit_date DATETIME NOT NULL,
  visit_end TIME NOT NULL,
  let_in tinyint NOT NULL,
  PRIMARY KEY (visit_id),
  FOREIGN KEY (patient_id) REFERENCES patient (patient_id),
  FOREIGN KEY (screener_id) REFERENCES screener (screener_id),
  FOREIGN KEY (visitor_id) REFERENCES visitor (visitor_id));


DROP TABLE IF EXISTS question ;
CREATE TABLE IF NOT EXISTS question (
  question_id INT NOT NULL,
  question_text varchar(255) NOT NULL UNIQUE,
  question_correct_answer tinyint NOT NULL,
  PRIMARY KEY (question_id));


DROP TABLE IF EXISTS visitor_has_answer ;
CREATE TABLE IF NOT EXISTS visitor_has_answer (
  visitor_id INT NOT NULL,
  date DATETIME NOT NULL,
  question_id INT NOT NULL,
  visitor_answer tinyint NOT NULL,
  FOREIGN KEY (visitor_id) REFERENCES visitor (visitor_id),
  FOREIGN KEY (question_id)REFERENCES question (question_id));
  
-- INSERTS
insert into question
(question_id, question_text, question_correct_answer) 
values
(1,"In the last 14 days, have you traveled out of state?", false),
(2,"In the last 14 days, have you been exposure to anyone with covid-19?", false),
(3,"Are you experiencing any symptoms of covid-19?", false);

insert into screener
(screener_id, screener_name, screener_station)
values
 (1,"Peter Labick",1),
 (2,"Marla Davis",2),
 (3,"Tommy Nelson",2), -- Shares a desk (for contact tracing)
 (4, "Paul Vicks", 3), 
 (5, "Dave Heinz", 4),
 (6, "Joe James", 4); -- Shares a desk (for contact tracing)
 

insert into patient
(patient_id, patient_first_name, patient_last_name, patient_classification, patient_precaution , patient_eol, patient_building , patient_room )
values
(1, "Jimmy", "Smith", "inpatient", "none", false, "Tower", 614), -- normal patient
(2, "Joseph", "Jane", "inpatient", "none", false, "Shapiro", 411), -- normal patient
(3, "Lisa", "Smith", "inpatient", "airborne", false, "CWN", 523), -- No visitors due to airborne precautions
(4, "Mickey", "Mouse", "inpatient", "none", true, "Tower", 723), -- No visitor limit due to EOL
(5, "Jane", "Doe", "icu", "contact", false, "Hale", 247), -- No visitors due to contact precuations
(6, "John", "Doe", "outpatient", "none", false, "CWN", 133), -- normal patient
(7, "Alice", "Doe", "er", "none", false, "Shapiro", 313), -- normal patient
(8, "James", "Doe", "ob", "none", false, "Tower", 412); -- normal patient

insert into visitor
(visitor_id, visitor_name)
values
(1,"John Mack"), -- normal visitor
(2,"Sara Smith"), -- shouldn't be allowed in to due answer
(3,"Christy English"),  -- shouldn't be allowed in due to 2nd visitor of day for given patient
(4, "Paul Smith"), -- normal visitor
(5, "Alex Ingles"), -- normal visitor
(6, "Alexa Jane"), -- normal visitor
(7, "Jerry Smithe"); -- should not be allowed based on answers, but will be to add a negative report for employee performance

select * from visitor_has_answer;

 
 insert into visitor_has_answer
 (visitor_id, date, question_id, visitor_answer)
 values
 (1,DATE("2020-11-23"), 1, false), -- Accepted Answers
 (1,DATE("2020-11-23"), 2, false),
 (1,DATE("2020-11-23"), 3, false),
 (2,DATE("2020-11-23"), 1, false), -- Sick Man's answers
 (2,DATE("2020-11-23"), 2, false),
 (2,DATE("2020-11-23"), 3, true), -- Sick Man is sick
 (3,DATE("2020-11-23"), 1, false), -- Accepted Answers
 (3,DATE("2020-11-23"), 2, false),
 (3,DATE("2020-11-23"), 3, false),
 (4,DATE("2020-11-24"), 1, false), -- Accepted Answers
 (4,DATE("2020-11-24"), 2, false),
 (4,DATE("2020-11-24"), 3, false),
 (5,DATE("2020-11-24"), 1, false), -- Accepted Answers
 (5,DATE("2020-11-24"), 2, false),
 (5,DATE("2020-11-24"), 3, false),
 (6,DATE("2020-11-25"), 1, false), -- Accepted Answers
 (6,DATE("2020-11-25"), 2, false),
 (6,DATE("2020-11-25"), 3, false),
 (7,DATE("2020-11-25"), 1, false), -- Sick Man answers
 (7,DATE("2020-11-25"), 2, false),
 (7,DATE("2020-11-25"), 3, true);  -- Visitor 7 is sick, however is mistakenly let in as a visitor


insert into visit
(visit_id, patient_id , screener_id , visitor_id, visit_date, visit_end, let_in)
values
(1,1,1,1,DATE("2020-11-23 01:30:00"),time("02:30:00"), true), -- normal visit
(2,2,2,4, DATE("2020-11-24 04:30:00"), time("05:00:00"), true), -- normal visit
(3,6,3,5, DATE("2020-11-24 06:30:00"),time("08:00:00"), true), -- normal visit
(4,7,1,6, DATE("2020-11-25 03:30:00"), time("06:00:00"), true), -- normal visit
(5,2,2,7, DATE("2020-11-25 07:30:00"), time("08:30:00"), true); -- Visit should not be let in. this will be refelcted in the performance report

 -- Test query 
 select patient_building, patient_room from visit join visitor using (visitor_id) join patient using (patient_id) where visitor_name ="Joe Mamma";
 select visitor_name from visit join visitor using (visitor_id) join patient using (patient_id) where patient_first_name ="<tkinter.Entryobject.!entry3>" and patient_last_name ="<tkinter.Entryobject.!entry4>"; 

select patient_first_name, patient_last_name from visit join visitor using (visitor_id) join patient using (patient_id) where visitor_name like "Joe Mamma"; 

select patient_eol = true or patient_precaution="none" from patient where patient_first_name = "Joe" and patient_last_name = "Mamma";





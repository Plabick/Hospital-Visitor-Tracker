-- To use the python code as is, plz set up your system like this
-- USER: visitorDBUser
-- PASSWORD: password
CREATE SCHEMA IF NOT EXISTS visitorDB;
use visitorDB;


DROP TABLE IF EXISTS patient;
CREATE TABLE IF NOT EXISTS patient (
  patient_id INT NOT NULL,
  patient_name VARCHAR(50) NOT NULL,
  patient_dob DATE NOT NULL,
  patient_classification ENUM("inpatient", "outpatient", "icu", "er", "ob") NOT NULL,
  patient_precaution ENUM("none", "contact", "airborne") NOT NULL,
  patient_eol TINYINT NOT NULL,
  patient_building ENUM("tower", "cwn", "shapiro", "hale") NULL,
  patient_room INT NULL,
  PRIMARY KEY (patient_id));


DROP TABLE IF EXISTS visitor ;
CREATE TABLE IF NOT EXISTS visitor (
  visitor_id INT NOT NULL,
  visitor_name VARCHAR(50) NOT NULL,
  let_in TINYINT NOT NULL,
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
  visit_start TIME NOT NULL,
  visit_end TIME NOT NULL,
  PRIMARY KEY (visit_id),
  FOREIGN KEY (patient_id) REFERENCES patient (patient_id),
  FOREIGN KEY (screener_id) REFERENCES screener (screener_id),
  FOREIGN KEY (visitor_id) REFERENCES visitor (visitor_id));


DROP TABLE IF EXISTS question ;
CREATE TABLE IF NOT EXISTS question (
  question_id INT NOT NULL,
  question_text VARCHAR(255) NOT NULL UNIQUE,
  question_correct_answer VARCHAR(255) NOT NULL,
  PRIMARY KEY (question_id));


DROP TABLE IF EXISTS visitor_has_answer ;
CREATE TABLE IF NOT EXISTS visitor_has_answer (
  visitor_id INT NOT NULL,
  date DATETIME NOT NULL,
  question_id INT NOT NULL,
  visitor_answer VARCHAR(255) NOT NULL,
  FOREIGN KEY (visitor_id) REFERENCES visitor (visitor_id),
  FOREIGN KEY (question_id)REFERENCES question (question_id));
  


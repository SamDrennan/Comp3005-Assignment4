Use the command below to install psycopg2

python3 -m pip install psycopg2

Create the database in pgAdmin4 using the command below
	
CREATE DATABASE "Assignment4"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
Running the main.py program will automatically populate and create the students table.

There may need to be changes to the password portion of the connection.

Functions:

getAllStudents():
prints all students in the students table

addStudent(first_name, last_name, email, enrollment_date):
adds the student using the user defined information

updateStudentEmail(student_id, new_email):
updates the email associated with the specified student id

deleteStudent(student_id):
deletes the specified student

resetDatabase():
deletes the students table and recreates it

main():
contains all the function calls for testing

Video Link:
https://youtu.be/Yjh1S4ZSbL0
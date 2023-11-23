import psycopg2 

global conn

def getAllStudents():
    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
    print("")


def addStudent(first_name, last_name, email, enrollment_date):
    
    cursor = conn.cursor()
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES('"+first_name+"', '"+last_name+"', '"+email+"', '"+enrollment_date+"')"
    cursor.execute(query)

    conn.commit()


def updateStudentEmail(student_id, new_email):
    
    cursor = conn.cursor()
    query = "UPDATE students SET email='"+new_email+"' WHERE student_id="+student_id
    cursor.execute(query)
    
    conn.commit()


def deleteStudent(student_id):
    
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE student_id=%s",student_id)

    conn.commit()


def resetDatabase():
    
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE students")
    
    cursor.execute("create table students(student_id	int GENERATED ALWAYS AS IDENTITY, first_name	varchar(255) NOT NULL,last_name	varchar(255) NOT NULL, email	varchar(255) NOT NULL UNIQUE, enrollment_date	date,primary key (student_id));")
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES('John', 'Doe', 'john.doe@example.com', '2023-09-01'),('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')")

    conn.commit()


def main():
    resetDatabase()

    print("TESTING getAllStudents:\n")
    getAllStudents()

    print("TESTING deleteStudent:\n")
    deleteStudent(input("Student ID: "))

    getAllStudents()

    print("TESTING updateStudentEmail:\n")
    id = input("Student ID: ")
    email = input("Email: ")
    updateStudentEmail(id, email)

    getAllStudents()

    print("TESTING addStudent:\n")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    enroll_date = input("Enrollment Date: ")
    addStudent(first_name, last_name, email, enroll_date)

    getAllStudents()

    input()

    conn.close()


if __name__ == "__main__":
    conn = psycopg2.connect(host='localhost',database='Assignment4',user='postgres',password='1234',port='5432')

    main()



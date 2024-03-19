import psycopg2
from psycopg2 import sql

class postgresCrud:
    def __init__(self, connection):
        self.connection = connection

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.connection)
            self.cur = self.conn.cursor()
            print("Connected to DB")
            
        except psycopg2.Error as e:
            print("Cant connect to DB:", e)

    def runQuery(self, query, modifyDb=None):
        try:
            self.cur.execute(query, modifyDb)
            self.conn.commit()
            
        except psycopg2.Error as e:
            print("Error running query:", e)

    def getAllStudents(self):
        query = "SELECT * FROM students;"
        self.cur.execute(query)
        return self.cur.fetchall()

    def addStudent(self, first_name, last_name, email, enrollment_date):
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
        modifyDb = (first_name, last_name, email, enrollment_date)
        self.runQuery(query, modifyDb)

    def updateStudentEmail(self, student_id, new_email):
        query = "UPDATE students SET email = %s WHERE student_id = %s;"
        modifyDb = (new_email, student_id)
        self.runQuery(query, modifyDb)

    def deleteStudent(self, student_id):
        query = "DELETE FROM students WHERE student_id = %s;"
        modifyDb = (student_id,)
        self.runQuery(query, modifyDb)

def main():

    connectToDb = postgresCrud("dbname=a3 user=postgres password= host=localhost")
    
    connectToDb.connect()

    connectToDb.addStudent("Rami", "Salame", "rami.salame@example.com", "2024-03-18")

    connectToDb.updateStudentEmail(1, "update.email.john.doe@example.com")

    connectToDb.deleteStudent(3)

    print("\nModified DB:")
    for student in connectToDb.getAllStudents():
        print(student)

if __name__ == "__main__":
    main()

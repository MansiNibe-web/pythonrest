from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import os
# Initialize the FastAPI
app = FastAPI()

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="firstdb"
)

# Model to represent the data or we can say the structure of the table in the database
class Student(BaseModel):
    id: int
    name: str
    mob: str

@app.get("/get_all_student")
def get_all_student():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Student")  # Fixed the incorrect reassignment of db
    result = cursor.fetchall()
    cursor.close()  # Close the cursor
    return result

# POST method to insert data into the database
@app.post("/add_student")
def add_student(std: Student):
    cursor = db.cursor()
    cursor.execute("INSERT INTO Student (id, name, mob) VALUES (%s, %s, %s)",
                   (std.id, std.name, std.mob)) 
    db.commit()
    cursor.close()  # Close the cursor
    return {"message": "Student added successfully"}

@app.put("/update_student/{student_id}")
def update_student(student_id: int, updated_student: Student):
    cursor = db.cursor()
    cursor.execute("UPDATE Student SET name = %s, mob = %s WHERE id = %s",
                   (updated_student.name, updated_student.mob, student_id))
    db.commit()
    cursor.close()
    
    return {"message": "Student updated successfully!"}



@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Student WHERE id = %s", (student_id,))
    db.commit()
    cursor.close()
    
    return {"message": "Student deleted successfully!"}


if __name__ == "__main__":
    import uvicorn
    port = os.getenv("PORT", 8080)  #here i set the port  to 8080 from default 8000
    uvicorn.run(app, host="127.0.0.1", port=port)
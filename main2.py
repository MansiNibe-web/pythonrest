from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import os
# Initialize the FastAPI
app = FastAPI()


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="firstdb"
    )
    print("Database connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")


# Model to represent the data or we can say the structure of the table in the database
class Student(BaseModel):
    id: int
    name: str
    mob: str



@app.post("/add_student")
def add_student(std: Student):
    cursor = db.cursor()
    cursor.execute("INSERT INTO Student (id, name, mob) VALUES (%s, %s, %s)",
                   (std.id, std.name, std.mob))  # Use std instead of emp
    db.commit()
    return {"message": "Student added successfully"}



if __name__ == "__main__":
    import uvicorn
    port = os.getenv("PORT", 8080)  # Default to 8080 if PORT is not set
    uvicorn.run(app, host="127.0.0.1", port=port)
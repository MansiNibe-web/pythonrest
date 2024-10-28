# # main file for the CRUD operations

# # Imports
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List  
# from studentdb import get_db
# from studentmodel import Student

# app = FastAPI()

# @app.post("/add_student", response_model=Student)
# def add_student(stud: Student, db: Session = Depends(get_db)):
#     db.add(stud)  # Add new student 
#     db.commit()   # Save all the new changes
#     db.refresh(stud)  # Refresh to get info of the new Student 
#     return stud  # Return the new updated or added Student 

# @app.get("/get_students", response_model=List[Student])  
# def get_all_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):  
#     students = db.query(Student).offset(skip).limit(limit).all()  
#     return students

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("student:app", host="127.0.0.1", port=8080, reload=True)  


# main.py

# main.py (student.py)
# main.py (student.py)
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from studentdb import get_db
from studentmodel import Student as StudentModel  # Import your SQLAlchemy model
from studentmodel import StudentCreate, Student as StudentPydantic  # Adjust your imports

app = FastAPI()

@app.post("/add_student", response_model=StudentPydantic)
def add_student(stud: StudentCreate, db: Session = Depends(get_db)):
    stud_model = StudentModel(**stud.dict())  # This should not include id
    db.add(stud_model)  # Add new student
    db.commit()  # Save changes
    db.refresh(stud_model)  # Refresh to get updated information
    return stud_model  # Return the new student with id

@app.get("/get_students", response_model=List[StudentPydantic])
def get_all_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return students





if __name__ == "__main__":
    import uvicorn
    #uvicorn.run("StudentOperation:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("student:app", host="127.0.0.1", port=8080, reload=True)
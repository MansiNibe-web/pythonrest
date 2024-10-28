from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# SQLAlchemy setup
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/p99"  # Change this to your database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Model
class StudentModel(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing id
    name = Column(String(100), index=True)  # Specify length for VARCHAR
    age = Column(Integer)
    email = Column(String(100), unique=True) 

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class StudentBase(BaseModel):
    name: str
    age: int
    email: str

class StudentCreate(StudentBase):
    pass  # No id field for creation

class Student(StudentBase):
    id: int  # Include id for retrieval

    class Config:
        orm_mode = True  # Allows the use of SQLAlchemy ORM

# FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
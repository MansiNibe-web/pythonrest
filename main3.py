from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database3 import SessionLocal, engine
from models3 import Users
from pydantic import BaseModel
app = FastAPI()
# Create database tables
# This avoids circular imports by ensuring Base.metadata.create_all is in main.py
from models3 import Users  # Import models after engine is created
Users.metadata.create_all(bind=engine)
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Pydantic schema for response model
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    # class Config:
    #     orm_mode = True
# Pydantic schema for user creation
class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str
# Route to get all users
@app.get("/users", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(Users).all()
# Route to create a new user
@app.post("/users", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    u = Users(name=user.name, email=user.email, password=user.password)
    db.add(u)
    db.commit()
    db.refresh(u)  # To get the auto-generated id
    return u



if __name__ == "__main__":
    import uvicorn
    #uvicorn.run("StudentOperation:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("main3:app", host="127.0.0.1", port=8080, reload=True)


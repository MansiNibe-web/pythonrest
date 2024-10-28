from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Sports, SportsCreate, SportsRead, Base
from database import engine, get_db

# Initialize the FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# CORS settings for frontend access
origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,  
    allow_methods=["*"],    
    allow_headers=["*"],     
)

# Create a new sport
@app.post("/add_sports", response_model=SportsRead)
def add_sports(sport: SportsCreate, db: Session = Depends(get_db)):
    db_sport = Sports(**sport.dict())
    db.add(db_sport)
    db.commit()
    db.refresh(db_sport)
    return db_sport

# Read all sports
@app.get("/get_all_sports", response_model=list[SportsRead])
def get_all_sports(db: Session = Depends(get_db)):
    return db.query(Sports).all()

# Update a sport by ID
@app.put("/update_sports_id/{sportsid}", response_model=SportsRead)
#sports_update : variable to store the updated sport
# sportcreate : gives the permission to update the sport as the format which is set in the pydantic model
# session = Depends : interact dependency with the FastAPI
def update_sports_by_id(sportsid: int, sport_update: SportsCreate, db: Session = Depends(get_db)):
    db_sport = db.query(Sports).filter(Sports.id == sportsid).first()
    if db_sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    
    db.query(Sports).filter(Sports.id == sportsid).update(sport_update.dict())
    db.commit()
    db.refresh(db_sport)
    return db_sport

# Delete a sport by name
@app.delete("/delete_by_name/{gamename}")
def delete_by_name(gamename: str, db: Session = Depends(get_db)):
    db_sport = db.query(Sports).filter(Sports.name == gamename).first()
    if db_sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    db.delete(db_sport)
    db.commit()
    return {"message": "Sport deleted successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

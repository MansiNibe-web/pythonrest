from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# SQLAlchemy model for the Sports table
class Sports(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # Primary Key, Auto-Increment
    name = Column(String(50), nullable=False)  # required, max 50 characters
    location = Column(String(100), nullable=False)  # Required, max 100 characters
    gametype = Column(String(20), nullable=False)  # Required, max 20 characters
    duration = Column(String(20), nullable=False)  # Required, max 20 characters

# Pydantic model for creating a new sport
class SportsCreate(BaseModel):
    name: str
    location: str
    gametype: str
    duration: str

# Pydantic model for reading a sport, including `id`
class SportsRead(SportsCreate):
    id: int

    class Config:
        orm_mode = True  # Enable compatibility with ORM objects

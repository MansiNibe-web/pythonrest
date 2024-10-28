from sqlalchemy import Column, Integer, String
from database3 import Base  # Correctly importing Base from database.py
# SQLAlchemy Users model
# class Users(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), index=True)
#     email = Column(String(100), unique=True, index=True)
#     password = Column(String(200))
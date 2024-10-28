from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Replace with your actual MySQL database details
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/firstdb"
# SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# Session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class for creating models
Base = declarative_base()
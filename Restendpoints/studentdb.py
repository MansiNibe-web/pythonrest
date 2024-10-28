from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/p99"

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a base class for the declarative base
Base = declarative_base()

# Session maker: creates new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# Generator function for database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Yield the database session
    finally:
        db.close()  # Close the session when done

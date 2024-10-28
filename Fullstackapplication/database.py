from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your MySQL connection details
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/p99"

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Session maker to be used in dependency injection
# session local manage transactions with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to provide database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# PRACTICE 

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL="mysqlm+mysqlconnector://root:root@localhost/p99"

# engine= create_engine(DATABASE_URL)

# SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()
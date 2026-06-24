from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create connection engine to PostgreSQL
# pool_pre_ping=True checks if connection is alive before using it
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Session factory
# Every request gets its own database session from here
SessionLocal = sessionmaker(
    autocommit=False,   # Changes are saved only when db.commit() is called
    autoflush=False,    # Don't automatically send changes to DB
    bind=engine         # Use the engine created above
)

# Parent class for all database models
# Example: User(Base), Graph(Base)
Base = declarative_base()


# FastAPI dependency
# Creates a DB session for a request and closes it afterwards
def get_db():
    db = SessionLocal()

    try:
        # Give database session to route
        yield db

    finally:
        # Always close connection after request finishes
        db.close()
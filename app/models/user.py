from sqlalchemy import Column, Integer, String
from app.db.database import Base

# User table in PostgreSQL
class User(Base):

    # Name of table in database
    __tablename__ = "users"

    # Primary key
    # Unique identifier for every user
    id = Column(Integer, primary_key=True, index=True)

    # User's name
    name = Column(String, nullable=False)

    # Email must be unique
    # No two users can register with same email
    email = Column(
        String,
        unique=True,
        nullable=False
    )

    # Stores hashed password
    # Never store plain text passwords
    password = Column(
        String,
        nullable=False
    )
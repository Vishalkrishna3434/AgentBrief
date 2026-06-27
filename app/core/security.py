from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Configure bcrypt for password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# Converts a plain password into a secure hashed password
def hash_password(password: str):
    return pwd_context.hash(password)

# Checks whether the entered password matches the stored hash
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Creates a JWT access token with payload data and expiration time
def create_access_token(data: dict,expires_delta: timedelta | None = None):
    # Copy payload to avoid modifying original data
    to_encode = data.copy()

    # Set token expiry time (custom or default)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = (
            datetime.utcnow() +
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    # Add expiration claim to JWT payload
    to_encode.update({
        "exp": expire
    })

    # Encode payload using secret key and algorithm
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
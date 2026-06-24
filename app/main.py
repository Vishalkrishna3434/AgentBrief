from fastapi import FastAPI

# Base knows about all SQLAlchemy models
# engine is the connection to PostgreSQL
from app.db.database import Base
from app.db.database import engine

# Import models so SQLAlchemy registers them
from app.models.graph import Graph
from app.models.user import User

# Create all tables that inherit from Base
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="AgentBrief",
    version="1.0.0"
)

# Test route to verify server is running
@app.get("/")
def home():
    return {
        "Message": "AgentBrief Running"
    }
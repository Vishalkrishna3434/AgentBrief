from sqlalchemy import Column, String, Integer, JSON, ForeignKey
from app.db.database import Base


# Graph table in PostgreSQL
class Graph(Base):

    # Table name inside database
    __tablename__ = "graphs"

    # Primary key
    # Every graph gets a unique id
    id = Column(Integer, primary_key=True, index=True)

    # Graph title
    title = Column(String, nullable=False)

    # Optional description
    description = Column(String)

    # Stores graph nodes as JSON
    nodes = Column(JSON, nullable=False)

    # Stores graph edges as JSON
    edges = Column(JSON, nullable=False)

    # Links graph to the user who created it
    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )
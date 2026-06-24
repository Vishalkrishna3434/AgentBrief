from sqlalchemy import Column,String,Integer,JSON,ForeignKey
from app.db.database import Base

def Graph(Base):
    __tablename__ = "Graphs"
    
    id = Column(Integer,primary_key=True,index=True)
    
    title = Column(String,nullable=False)
    
    description = Column(String)
    
    nodes = Column(JSON,nullable=False)
    
    edges = Column(JSON,nullable=False)
    
    owner_id = Column(Integer,ForeignKey("users.id"))
    

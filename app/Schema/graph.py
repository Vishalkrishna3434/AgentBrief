from pydantic import BaseModel

class GraphCreate(BaseModel):
   title : str
   description : str
   nodes : list[str]
   edges : list[list[str]]
   

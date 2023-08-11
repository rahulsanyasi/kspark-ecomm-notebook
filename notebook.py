from pydantic import BaseModel

class Notebook(BaseModel):
    id: int
    notebook_type: str
    size: str
    pages: str
    type: str
    price: float
    
    def __init__(self, id):
        self.id = id
    
    

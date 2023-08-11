from fastapi import FastAPI
# from notebook import Notebook
from pydantic import BaseModel

# print(f"Loading Notebook api")

app = FastAPI()

class Notebook(BaseModel):
    id: int
    notebook_type: str
    size: str
    pages: str
    type: str
    price: float
    
notebooks_list = [{
    "id": 105,
    "notebook_type": "Exercise Book",
    "size": "20 x 26",
    "pages": "180",
    "type": "6 Subjects Note Book",
    "price": 180.00
}]

@app.get("/")
async def home():
    print(f"Inside root function")
    return {"message": "Welcome to Pragiti stationery shop!!"}

@app.get("/notebooks")
async def get_notebooks():
    print(f"Inside get_notebooks function...")
    return {"available_notebooks": notebooks_list}

@app.post("/new-notebook")
def add_new_notebook(notebook: Notebook):
    print(f"add_new_notebook method...")
    notebooks_list.append(notebook.dict())
    return notebooks_list

@app.get("/notebook/{id}")
def get_notebook_by_id(id: int):
    for notebook in notebooks_list:
        if notebook['id'] == id:
            return notebook
    return {"message": "Notebook not found"}

@app.delete("/notebook/{id}")
def delete_notebook_by_id(id: int):
    for notebook in notebooks_list:
        if notebook['id'] == id:
            notebook_id = notebooks_list.index(notebook)
            notebooks_list.pop(notebook_id)
            return notebooks_list
    return {"message": "Notebook not found"}
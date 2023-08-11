from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from main import app

# app = FastAPI()

client=TestClient(app=app)

def test_get_notebook():
    response = client.get("/")
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to Pragiti stationery shop!!"}
    
# def test_add_new_notebook():
#     response = client.post('/new-notebook',json={"id":105,"notebook_type":"Exercise Book","size":"20 x 26","pages":"180","type":"6 Subjects Note Book","price":180.0})
    
#     expected_status_code = 200
#     observed_status_code = response.status_code
#     assert expected_status_code == observed_status_code
    
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.json() == {"id":105,"notebook_type":"Exercise Book","size":"20 x 26","pages":"180","type":"6 Subjects Note Book","price":180.0}
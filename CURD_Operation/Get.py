
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()



data = [
    {"id": 1, "name": "Mansi", "salary": "5000000", "mob": "9112990778"},
    {"id": 2, "name": "John", "salary": "6000000", "mob": "9123456789"},
    {"id": 1, "name": "Mahi", "salary": "9000000","mob": "7774834341"}
]

class Employee(BaseModel):
    id:int   
    name:str
    salary:str
    mob:str


@app.get("/get_all_employee",response_model=List[Employee])
async def get_all_emp():
    return data




if __name__ == "__main__":
    import uvicorn
    #uvicorn.run("StudentOperation:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("Get:app", host="127.0.0.1", port=8080, reload=True)


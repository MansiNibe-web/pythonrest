from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()

data=[]

class Flower(BaseModel):
    id:int
    name:str
    color:str

@app.post("/add_flower", response_model=data)
def add_flower(flower: Flower):
    data.append(flower)
    return {"message": "Flower added successfully!","Flower":flower}

@app.post("/add_flowers",response_model=data)
def add_flowers(flower:Flower):
    data.append(flower)
    return{"Flower added successfully":flower}

@app.get("/get_flower",response_model=List[Flower])
def get_flower():
    return data

@app.put("/update_flower/{flower_id}")
def update_flower(flower_id: int, updated_flower: Flower):
    # Iterate through the list of flowers to find the one with the matching ID
    for flower in data:
        if flower.id == flower_id:
            # Update the flower's name and color
            flower.name = updated_flower.name
            flower.color = updated_flower.color
            return {"message": "Flower updated successfully!", "flower": updated_flower}
    
    # If flower is not found, raise a 404 exception
    raise HTTPException(status_code=404, detail="Flower not found")

@app.delete("/delete_flower/{flower_id}")
def delete_flower(flower_id: int):
    for flower in data:
        if flower.id == flower_id:
            data.remove(flower)  # Remove it from the list
            return {"message": "Flower deleted successfully!"}
    
    # If the flower is not found, raise an exception
    raise HTTPException(status_code=404, detail="Flower not found")


if __name__ == "__main__":
    import uvicorn
    #uvicorn.run("StudentOperation:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("Post:app", host="127.0.0.1", port=8080, reload=True)

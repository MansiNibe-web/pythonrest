from CURD_models import Sports
from CURD_database import db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os

app=FastAPI()


#url for the frontend which i want to allow 
origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],    
    allow_headers=["*"],     
)

@app.post("/add_sports")
async def add_sports(sp:Sports):
    cursor=db.cursor()
    cursor.execute("Insert into Sports(id, name, location, gametype, duration) values (%s,%s,%s,%s,%s)", (sp.id, sp.name, sp.location, sp.gametype, sp.duration))
    db.commit() 
    cursor.close()
    return {"message":"Sport added successfully !", "Sport":sp}



@app.get("/get_all_sports")
async def get_all_sports():
    cursor=db.cursor(dictionary=True)
    cursor.execute("select * from Sports")
    result= cursor.fetchall()
    cursor.close()
    return result


@app.put("/update_sports_id/{sportsid}")
async def update_sports_by_name(sportsid:int,updatedsports:Sports):
    cursor=db.cursor()
    cursor.execute("UPDATE Sports SET name = %s, location = %s, gametype = %s, duration = %s WHERE id = %s",
    (updatedsports.name, updatedsports.location, updatedsports.gametype, updatedsports.duration, sportsid))

    db.commit()
    cursor.close()
    return {"message":"Sports updated successfully ! ", "sports":updatedsports}

@app.delete("/delete_by_name/{gamename}")
async def delete_by_name(gamename: str):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Sports WHERE name = %s", (gamename,))
    db.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    
    return {"message": "Sports deleted successfully!"}

    

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run("StudentOperation:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("CURD_main:app", host="127.0.0.1", port=8080, reload=True)
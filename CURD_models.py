from pydantic import BaseModel

class Sports(BaseModel):
    id:int        # eg :  1
    name:str      # eg : "Cricket"
    location:str  # eg : "mumbai"
    gametype:str  # eg : "outdoor"
    duration:str  # eg : "90 minutes"

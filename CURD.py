from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date

app=FastAPI()  #app is a variable which is an intance of the FastAPI main point for the interaction off all the api 

data=[]

class Employee(BaseModel):
    id:int
    name:str
    salary:str
    mob:str
    dob:date


@app.post("/add_employee")
async def add_employee(emp:Employee):
    data.append(emp)
    return {"message":"employee added successfully !"}


@app.get("/get_all_employee", response_model=List[Employee])
def get_all_employee():
    return data


@app.get("/get_id/{empid}")
def getid(empid):
    return empid


@app.put("/update_employee_by_id/{emp_id}")
def update_by_id(emp_id: int, updated_emp: Employee):
    # Check if the employee ID exists in the data
    for emp in data:
        if emp.id == emp_id:
            # Update the employee's details
            emp.name = updated_emp.name
            emp.salary = updated_emp.salary
            emp.mob = updated_emp.mob
            emp.dob = updated_emp.dob
            return {"message": "Employee updated successfully!", "employee": emp}

    # If we finish the loop without finding the employee, raise an exception
    raise HTTPException(status_code=404, detail="ID not found!")



@app.delete("/delete_employee_by_name/{emp_name}")
def delete_emp_by_name(emp_name: str):
    for emp in data:
        if emp.name == emp_name:
            data.remove(emp)
            return {"message": "Employee deleted successfully!"}
    
    raise HTTPException(status_code=404, detail="Name not found")


# @app.delete("/delete_employee_by_name/{emp_name}")
# def delete_emp_by_name(emp_name: str):
#     for emp in data:
#         if emp.name == emp_name:
#             data.remove(emp)  # Remove the employee from the list
#             return {"message": "Employee deleted successfully!"}  # Return success message
            
#     # If we reach here, no employee was found with that name
#     raise HTTPException(status_code=404, detail="Name not found")

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run("StudentOperation:app", host="127.0.0.1", port=8001, reload=True)
    uvicorn.run("CURD_DB:app", host="127.0.0.1", port=8080, reload=True)

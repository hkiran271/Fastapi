from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

employees_data = [
    {"id": 1, "name": "John Doe", "department": "Engineering", "salary": 75000.0},
    {"id": 2, "name": "Jane Smith", "department": "Marketing", "salary": 65000.0},
    {"id": 3, "name": "Alice Johnson", "department": "HR", "salary": 60000.0}
]

app = FastAPI()


@app.get("/employees/", response_model=List[Employee])
def get_employees():
    return employees_data


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    for employee in employees_data:
        if employee["id"] == employee_id:
            return employee
    # raise HTTPException(status_code=404, detail="Employee not found")
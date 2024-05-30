from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

class Employee(BaseModel):
    id: int
    section: str
    year: str
    count: float

employees_data = [
    {"id": 1, "section": "A", "year": "first", "count": 100},
    {"id": 2, "section": "B", "year": "second", "count": 110},
    {"id": 3, "section": "C", "year": "thrid", "count": 90}
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
        
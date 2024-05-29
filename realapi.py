from fastapi import FastAPI
from pydantic import BaseModel


class Employee(BaseModel):
    dclass: str
    section: str 
    year: float
    count: float | None = None


app = FastAPI()


@app.get("/employee/")
async def read_employee():
    query = 'select * From employee'
    return Employee
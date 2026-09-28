from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# Address Models
# -------------------------

class AddressInput(BaseModel):
    city: str
    state: str
    pincode: int

class AddressOutput(BaseModel):
    city: str
    state: str

# -------------------------
# Student Models
# -------------------------

class StudentInput(BaseModel):
    name: str
    age: int
    email: str
    address: AddressInput

class StudentOutput(BaseModel):
    name: str
    age: int
    address: AddressOutput

# -------------------------
# API
# -------------------------

@app.post("/students", response_model=StudentOutput)
def create_student(student: StudentInput):

    return {
        "name": student.name,
        "age": student.age,
        "address": {
            "city": student.address.city,
            "state": student.address.state
        }
    }

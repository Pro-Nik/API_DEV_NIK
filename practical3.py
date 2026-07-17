from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Student(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=30
    )

    age: int = Field(
        gt=18,
        lt=60
    )

    email: EmailStr

    course: str = Field(
        min_length=2,
        max_length=20
    )

    fees: float

@app.post("/students")
def create_student(student: Student):

    return {
        "message": "Student Registered Successfully",
        "student": student
    }
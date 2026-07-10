# Get Method

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Nitish"},
    {"id": 2, "name": "Rahul"}
]

@app.get('/')
def home():
    return {"This is home page."}
@app.get("/students")
def fatch():
    return students


# Post Method

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

students = []

@app.post("/students")
def create_student(student: Student):
    students.append(student.dict())
    return {
        "message": "Student Created",
        "student": student
    }

@app.get("/student_data")
def student():
    return students

# Put Method

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {"name": "Nitish", "age": 23}
}

class Student(BaseModel):
    name: str
    age: int

@app.get("/")
def student_data():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    students[student_id] = student.dict()
    return students[student_id]

@app.get("/update_data")
def update_data():
    return students


# Delete method

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model
class Student(BaseModel):
    name: str
    age: int

# In-memory database
students = [
    {"id": 1, "name": "Nitish", "age": 23},
    {"id": 2, "name": "Rahul", "age": 22},
    {"id": 3, "name": "Amit", "age": 21}
]

# GET All Students
@app.get("/students")
def get_students():
    return students

# DELETE Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {
                "message": "Student deleted successfully",
                "deleted_student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


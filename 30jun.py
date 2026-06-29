# Get Method

# from fastapi import FastAPI

# app = FastAPI()

# students = [
#     {"id": 1, "name": "Nitish"},
#     {"id": 2, "name": "Rahul"}
# ]

# @app.get('/')
# def home():
#     return {"This is home page."}
# @app.get("/students")
# def get():
#     return students


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

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# students = {
#     1: {"name": "Nitish", "age": 23}
# }

# class Student(BaseModel):
#     name: str
#     age: int

# @app.put("/students/{student_id}")
# def update_student(student_id: int, student: Student):
#     students[student_id] = student.dict()
#     return students[student_id]


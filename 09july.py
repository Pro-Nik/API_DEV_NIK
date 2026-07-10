from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Student CRUD API",
    description="Simple CRUD Operations using FastAPI",
    version="1.0"
)

# -------------------------------
# Pydantic Model
# -------------------------------
class Student(BaseModel):
    name: str
    age: int

# -------------------------------
# In-Memory Database
# -------------------------------
students = [
    {"id": 1, "name": "Nitish", "age": 23},
    {"id": 2, "name": "Rahul", "age": 22},
    {"id": 3, "name": "Amit", "age": 21}
]

# =====================================================
# HOME PAGE
# =====================================================
@app.get("/")
def home():
    return {
        "message": "Welcome to Student CRUD API"
    }

# =====================================================
# GET ALL STUDENTS
# =====================================================
@app.get("/students")
def get_students():
    return students

# =====================================================
# GET STUDENT BY ID
# =====================================================
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )

# =====================================================
# CREATE STUDENT
# =====================================================
@app.post("/students")
def create_student(student: Student):

    new_id = max([s["id"] for s in students], default=0) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)

    return {
        "message": "Student Created Successfully",
        "student": new_student
    }

# =====================================================
# UPDATE STUDENT
# =====================================================
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for student in students:

        if student["id"] == student_id:

            student["name"] = updated_student.name
            student["age"] = updated_student.age

            return {
                "message": "Student Updated Successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )

# =====================================================
# DELETE STUDENT
# =====================================================
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student Deleted Successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )
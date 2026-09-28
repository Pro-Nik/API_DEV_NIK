from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


# Database Model
class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    age = fields.IntField()
    email = fields.CharField(max_length=100)

    class Meta:
        table = "students"


# Request Model
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str


# CREATE
@app.post("/students")
async def create_student(student: StudentCreate):

    new_student = await Student.create(
        name=student.name,
        age=student.age,
        email=student.email
    )

    return {
        "message": "Student created successfully",
        "id": new_student.id,
        "name": new_student.name,
        "age": new_student.age,
        "email": new_student.email
    }


# READ ALL
@app.get("/students")
async def get_students():

    students = await Student.all()

    return [
        {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email
        }
        for student in students
    ]


# READ ONE
@app.get("/students/{student_id}")
async def get_student(student_id: int):

    student = await Student.get_or_none(id=student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email
    }


# UPDATE
@app.put("/students/{student_id}")
async def update_student(
    student_id: int,
    student: StudentCreate
):

    existing_student = await Student.get_or_none(
        id=student_id
    )

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email

    await existing_student.save()

    return {
        "message": "Student updated successfully"
    }


# DELETE
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):

    student = await Student.get_or_none(
        id=student_id
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    await student.delete()

    return {
        "message": "Student deleted successfully"
    }


# Tortoise Configuration
register_tortoise(
    app,
    db_url="sqlite://students.db",
    modules={"models": ["main"]},
    generate_schemas=True,
    add_exception_handlers=True
)

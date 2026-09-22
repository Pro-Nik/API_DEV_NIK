from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session


# ------------------------------------------------
# 1. DATABASE CONNECTION
# ------------------------------------------------

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ------------------------------------------------
# 2. SQLALCHEMY DATABASE MODEL
# ------------------------------------------------

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


# Create the table
Base.metadata.create_all(bind=engine)


# ------------------------------------------------
# 3. DATABASE SESSION DEPENDENCY
# ------------------------------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------
# 4. PYDANTIC MODEL
# ------------------------------------------------

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str


# ------------------------------------------------
# 5. FASTAPI APPLICATION
# ------------------------------------------------

app = FastAPI()


# ------------------------------------------------
# 6. ADD STUDENT
# ------------------------------------------------

@app.post("/students")
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# ------------------------------------------------
# 7. GET ALL STUDENTS
# ------------------------------------------------

@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students


# ------------------------------------------------
# 8. GET ONE STUDENT
# ------------------------------------------------

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

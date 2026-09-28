from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1: "Nitish",
    2: "Rahul",
    3: "Amit"
}

@app.get("/students/{id}")
def get_student(id: int):

    if id not in students:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return {
        "Student Name": students[id]
    }

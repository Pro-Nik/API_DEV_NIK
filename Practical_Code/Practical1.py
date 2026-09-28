from fastapi import FastAPI

app1 = FastAPI()

@app1.get("/")
def home():

    return {
        "message":"Welcome to FastAPI"
    }


@app1.get("/students")
def get_students():

    students = [

        {
            "id":1,
            "name":"Nitish",
            "course":"AI"
        },

        {
            "id":2,
            "name":"Rahul",
            "course":"Data Science"
        },

        {
            "id":3,
            "name":"Amit",
            "course":"Cyber Security"
        }

    ]

    return students

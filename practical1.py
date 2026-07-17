from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {
        "message":"Welcome to FastAPI"
    }


@app.get("/students")
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
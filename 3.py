from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_data():
    students = [
        {
            "id" : 1,
            "name" : "Nitish"
        },
        {
            "id" : 2,
            "name" : "Sumit"
        },

    ]
    return students[1]

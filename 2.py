from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def get_student():

    with open("data/data.json", "r") as file:
        students= json.load(file)

    return students
from fastapi import FastAPI

app = FastAPI(
title="My First FastAPI App",
description="This is a simple FastAPI application for learning purposes.",
version="2.0.0"
)

@app.get("/")
def home():
    students = [
        {
        "id": 1,
        "name": "Nitish"
        },
        {
            "id": 2,
            "name":"Sumit"
        }
    ]

    return students

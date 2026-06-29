from fastapi import FastAPI 

app = FastAPI(
title="My First FastAPI App",
description="This is a simple FastAPI application for learning purposes.",
version="1.0.0"
)

@app.get("/")
def home():
    return {"Hello"}

@app.get("/about")
def about():
    return {"This is the about page"}




from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return {"Hello "}

@app.get("/about")
def about():
    return {"This is the about page"}




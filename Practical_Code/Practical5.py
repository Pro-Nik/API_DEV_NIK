from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Task Model
class Task(BaseModel):
    title: str
    completed: bool

# List to store tasks
tasks = []

# Home API
@app.get("/")
def home():
    return {"message": "Task Management API"}

# Create Task
@app.post("/tasks")
def create_task(task: Task):

    tasks.append(task)

    return {
        "message": "Task Added Successfully",
        "task": task
    }

# Get All Tasks
@app.get("/tasks")
def get_tasks():

    return tasks

# Update Task
@app.put("/tasks/{index}")
def update_task(index: int, task: Task):

    tasks[index] = task

    return {
        "message": "Task Updated",
        "task": task
    }

# Delete Task
@app.delete("/tasks/{index}")
def delete_task(index: int):

    tasks.pop(index)

    return {
        "message": "Task Deleted Successfully"
    }

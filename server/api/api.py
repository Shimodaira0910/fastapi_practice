from fastapi import FastAPI
from server.data.model import Task
from bussiness import TaskManager

app = FastAPI()
task_manager = TaskManager()

@app.get("/task/" , response_model=Task)
def read_task():
    return task_manager.get_tasks()
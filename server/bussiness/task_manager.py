from pydantic import BaseModel
from data.task_dao import TaskDao

class TaskManager():
    
    def __init__(self):
        self.task_dao = TaskDao()
        
    def get_tasks(self) -> list[BaseModel]:
        return self.task_dao.get_tasks
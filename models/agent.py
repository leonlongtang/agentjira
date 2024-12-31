import json
import datetime
from models.task import Task
from typing import List

class Agent:
    def __init__(self, _id: str, name: str, description: str, tasks: List[Task], role: str):
        self._id = _id
        self.name = name
        self.description = description
        self.tasks = tasks
        self.role = role
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'tasks': [task.name for task in self.tasks],
            'role': self.role,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def receive_task(self, task: Task):
        self.tasks.append(task)
        self.updated_at = datetime.datetime.now()

    def complete_task(self, task: Task):
        self.tasks.remove(task)
        self.updated_at = datetime.datetime.now()

    def get_tasks(self):
        return self.tasks

    def get_task(self, task: Task):
        return self.tasks.get(task)
    


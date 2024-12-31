from models.task import Task
from models.agent import Agent
from typing import List
import json
import datetime

class Jira:
    def __init__(self, name: str, tasks: List[Task], agents: List[Agent]):
        self.name = name
        self.tasks = tasks
        self.agents = agents
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)
    
    def to_dict(self):
        return {
            'name': self.name,
            'tasks': [task.name for task in self.tasks],
            'agents': [agent.name for agent in self.agents],
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.updated_at = datetime.datetime.now()

    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        self.updated_at = datetime.datetime.now()

    def remove_task(self, task: Task):
        self.tasks.remove(task)
        self.updated_at = datetime.datetime.now()

    def remove_agent(self, agent: Agent):
        self.agents.remove(agent)
        self.updated_at = datetime.datetime.now()

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_agents(self) -> List[Agent]:
        return self.agents

    def get_agent(self, name: str) -> Agent:
        return next((agent for agent in self.agents if agent.name == name), None)

    def get_task(self, name: str) -> Task:
        return next((task for task in self.tasks if task.name == name), None)
    
    def assign_tasks(self, tasks: List[Task], agent: Agent):
        for task in tasks:
            agent.receive_task(task)



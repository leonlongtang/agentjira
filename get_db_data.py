from database.agents import get_agents, update_agent
from database.tasks import get_tasks
from models.agent import Agent 
from models.task import Task
from models.jira import Jira

agents = get_agents()
tasks = get_tasks()

jira = Jira(name='Jira', tasks=[], agents=[])

for agent in agents:
    agent = Agent(agent['_id'], agent['name'], agent['description'], agent['tasks'], agent['role'])
    jira.add_agent(agent)

for task in tasks:
    task = Task(task['_id'], task['name'], task['description'], task['status'])
    jira.add_task(task)


agent1 = jira.get_agent('Agent 1')
tasks1 = jira.get_tasks()[:2]
jira.assign_tasks(tasks1, agent1)


agent2 = jira.get_agent('Agent 2')
tasks2 = jira.get_tasks()[2:4]
jira.assign_tasks(tasks2, agent2)

agent3 = jira.get_agent('Agent 3')
tasks3 = jira.get_tasks()[4:]
jira.assign_tasks(tasks3, agent3)

print(jira)

for agent in jira.agents:
    update_agent(agent)
    print(agent)


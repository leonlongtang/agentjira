from database.agents import add_agent, clear_agents
from database.tasks import add_task, clear_tasks
import json
import argparse

clear_agents()
clear_tasks()

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, required=True)
args = parser.parse_args()

json_file = open(args.file, 'r')
json_data = json.load(json_file)

for agent in json_data['agents']:
    add_agent(agent)

for task in json_data['tasks']:
    add_task(task)

from pathlib import Path
from json import dumps, loads
from datetime import datetime

tasks = {
        "tasks": [
            { "task": "Bay a house", "done": False, "created_at": str(datetime.now())[:10] },
            { "task": "Work to office tomorrow", "done": False, "created_at": str(datetime.now())[:10] },
            { "task": "Fix crapping worker bug", "done": True, "created_at": str(datetime.now())[:10] },
            { "task": "Do something", "done": False, "created_at": str(datetime.now())[:10] }
        ]
    }

# convert a list to json and indent
convert_tasks_to_json = dumps(tasks, indent=1)

# write the tasks to json file
"""
Path("tasks/tasks.json") \
    .write_text(convert_tasks_to_json)
"""

# read datas from json
tasks_data = Path("tasks/tasks.json").read_text()
convert_tasks_json_to_list = loads(tasks_data)

for index, task in enumerate(convert_tasks_json_to_list["tasks"]):
    print(index, task)

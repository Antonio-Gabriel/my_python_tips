from datetime import datetime
from operator import itemgetter

tasks = [
    { "task": "Bay a house", "done": False, "created_at": str(datetime.now()) },
    { "task": "Work to office tomorrow", "done": False, "created_at": str(datetime.now()) },
    { "task": "Fix crapping worker bug", "done": True, "created_at": str(datetime.now()) },
    { "task": "Do something", "done": False, "created_at": str(datetime.now()) }
]

tasks.sort(key=itemgetter("task"))

print("Iterate all tasks and sort by task name \n")

# Iterate all tasks and sort by task
for index, task in enumerate(tasks):
    print(index, task)


print("\n")

print("Filter all tasks that already done \n")
# filter all tasks that already done
for index, task in enumerate(list(
    filter(lambda task: task["done"] == True, tasks)
    )):    
    print(index, task)


print("\n")

print("Mapping all tasks and marke as done \n")
# map and marke as done all tasks

def marke_as_done(task):
    """marke as done the task"""
    task["done"] = True

    return task

for index, task, in enumerate(list(map(marke_as_done, tasks))):
    print(index, task)

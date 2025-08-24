# core/storage.py

import os
from models.task import Task

FILE_NAME = "task.txt"


def get_user_file(username):
    # Every user gets their own file
    return f"tasks_{username}.txt"


def save_task(tasks, username):
    filename = get_user_file(username)
    with open(filename, 'w') as file:
        for task in tasks:
            status = "1" if task.completed else "0"
            file.write(f"{status}|{task.title}\n")


def load_tasks(username):
    filename = get_user_file(username)
    tasks = []
    if not os.path.exists(filename):
        return tasks
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                status, title = line.strip().split("|", 1)
                completed = (status == "1")
                tasks.append(Task(title, completed))
    return tasks

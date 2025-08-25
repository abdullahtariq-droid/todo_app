# core/storage.py

import json
import os
from typing import List
from models.task import Task

TASKS_FILE = "tasks.json"


def load_all_tasks() -> dict:
    """Load all users' tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_all_tasks(data: dict) -> None:
    """Save all users' tasks to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_tasks(user_id: str) -> List[Task]:
    """Load tasks for a specific user ID."""
    data = load_all_tasks()
    user_tasks = data.get(user_id, [])
    tasks: List[Task] = [Task(t["task"], t["done"]) for t in user_tasks]
    return tasks


def save_tasks(tasks: List[Task], user_id: str) -> None:
    """Save tasks for a specific user ID."""
    data = load_all_tasks()
    # Convert Task objects into dicts
    data[user_id] = [{"task": t.title, "done": t.completed} for t in tasks]
    save_all_tasks(data)

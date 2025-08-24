# core/task_manager.py

from models.task import Task
from core import storage


class TaskManager:
    def __init__(self, username):
        self.username = username
        self.tasks = storage.load_tasks(username)

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        storage.save_task(self.tasks, self.username)

    def list_tasks(self):
        if not self.tasks:
            print("\n=== Your Tasks ===")
            print("No tasks found.")
            print("==================\n")
            return

        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        pending = total - completed
        print("\n=== Your Tasks ===")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✔" if task.completed else "✗"
        print(f"{idx}. {task.title} [{status}]")
        print("-------------------")
        print(f"Total: {total} | Completed: {completed} | Pending: {pending}")
        print("===================\n")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            storage.save_task(self.tasks, self.username)
        else:
            print("Invalid task number")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            storage.save_task(self.tasks, self.username)
        else:
            print("Invalid task number")

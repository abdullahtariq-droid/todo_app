# models / task.py

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"

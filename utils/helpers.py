# utils/helpers.py

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("=======================")


def get_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return None


def get_task_index():
    try:
        return int(input("Enter task number: ")) - 1
    except ValueError:
        return None

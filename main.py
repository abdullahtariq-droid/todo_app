# main.py

from core.task_manager import TaskManager
from utils.helpers import show_menu, get_choice, get_task_index


def main():
    username = input("Enter your username: ").strip()
    task_manager = TaskManager(username)
    while True:
        show_menu()
        choice = get_choice()
        if choice == 1:
            title = input("Enter task title: ")
            task_manager.add_task(title)
            print("Task added.")
        elif choice == 2:
            print("\nYour Tasks:")
            task_manager.list_tasks()
        elif choice == 3:
            task_manager.list_tasks()
            index = get_task_index()
            task_manager.complete_task(index)
            print("Task marked complete.")
        elif choice == 4:
            task_manager.list_tasks()
            index = get_task_index()
            task_manager.delete_task(index)
            print("Task deleted.")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

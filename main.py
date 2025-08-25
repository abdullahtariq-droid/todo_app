# main.py

from core.task_manager import TaskManager
from Authentication.auth import login, register
from utils.helpers import show_menu, get_choice, get_task_index


def main():
    # User authentication
    print("1. Login")
    print("2. Register")
    choice = input("Choose an option: ")
    user = None

    if choice == "1":
        while not user:
            user = login()
    elif choice == "2":
        username = input("New username: ")
        password = input("New password: ")
        user = register(username, password)
        if not user:
            return
    else:
        print("Invalid choice.")
        return

    # Initialize Task Manager
    # Create the TaskManager with user ID
    task_manager = TaskManager(user["id"])

    while True:
        show_menu()
        user_choice = get_choice()
        if user_choice == 1:
            title = input("Enter task title: ")
            task_manager.add_task(title)
            print("Task added.")
        elif user_choice == 2:
            task_manager.list_tasks()
        elif user_choice == 3:
            task_manager.list_tasks()
            index = get_task_index()
            task_manager.complete_task(index)
            print("Task marked complete.")
        elif user_choice == 4:
            task_manager.list_tasks()
            index = get_task_index()
            task_manager.delete_task(index)
            print("Task deleted.")
        elif user_choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

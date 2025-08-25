import json
import os
import uuid

USERS_FILE = "users.json"
TASKS_FILE = "tasks.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


def authenticate(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None


def register(username, password):
    users = load_users()
    if any(u["username"] == username for u in users):
        print("Username already exists!\n")
        return None
    user_id = "u" + uuid.uuid4().hex[:6]  # unique short ID
    user = {"id": user_id, "username": username, "password": password}
    users.append(user)
    save_users(users)
    print("Registration successful!\n")
    return user


def login():
    print("=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.json", "r") as f:
        users = json.load(f)  # users is a list

    for user in users:  # iterate through list
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return user   # return dict with id, username, password

    print("Invalid credentials.")
    return None

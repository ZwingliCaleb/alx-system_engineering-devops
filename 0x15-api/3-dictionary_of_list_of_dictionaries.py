#!/usr/bin/python3
"""
Export data in JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url).json()

    todo_all_employees = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for todo in todos:
            if todo.get("userId") == user_id:
                task = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                tasks.append(task)
        todo_all_employees[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_all_employees, json_file)


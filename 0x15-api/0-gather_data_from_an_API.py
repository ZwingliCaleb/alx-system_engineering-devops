#!/usr/bin/python3
""" This is a script to import data from an API """

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.
    """
    users_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    employee_name = ''
    total_tasks = 0
    completed_tasks = 0
    task_titles = []

    for user in users_response:
        if user['id'] == employee_id:
            employee_name = user['name']
            break

    for todo in todos_response:
        if todo['userId'] == employee_id:
            total_tasks += 1
            if todo['completed']:
                completed_tasks += 1
                task_titles.append(todo['title'])

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task_title in task_titles:
        print(f"\t{task_title}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide an employee ID.')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data.get('name')

        todo_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
        todo_response = requests.get(todo_url)

        if todo_response.status_code == 200:
            todos = todo_response.json()
            total_tasks = len(todos)
            completed_tasks = [todo for todo in todos if todo.get('completed')]
            num_completed_tasks = len(completed_tasks)

            print(f"Employee {employee_name} is done with tasks "
                  f"({num_completed_tasks}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t{task.get('title')}")
        else:
            print(f"Failed to retrieve TODO list for employee {employee_name}.")
    else:
        print(f"Employee with ID {employee_id} not found.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

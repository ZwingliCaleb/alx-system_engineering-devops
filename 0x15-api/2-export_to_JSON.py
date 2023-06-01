#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API and exports the data in JSON format.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and returns information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary containing the TODO list progress.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data.get('name')

        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todo_response = requests.get(todo_url)
        if todo_response.status_code == 200:
            todos = todo_response.json()
            total_tasks = len(todos)
            completed_tasks = [task for task in todos if task.get('completed')]
            num_completed_tasks = len(completed_tasks)

            employee_progress = {
                "employee_id": employee_id,
                "employee_name": employee_name,
                "tasks_completed": num_completed_tasks,
                "total_tasks": total_tasks,
                "completed_tasks": [{"task": task.get('title'), "completed": task.get('completed')} for task in completed_tasks]
            }

            return employee_progress

        print(f"No tasks found for employee {employee_name}.")
    else:
        print(f"Employee with ID {employee_id} not found.")

    return None


def export_to_json(employee_id, data):
    """
    Exports the data in JSON format to a file with the employee ID as the filename.

    Args:
        employee_id (int): The ID of the employee.
        data (dict): The data to be exported.

    Returns:
        None
    """
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename} successfully.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_progress = get_employee_todo_progress(employee_id)

    if employee_progress:
        export_to_json(employee_id, employee_progress)

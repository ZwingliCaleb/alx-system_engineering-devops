#!/usr/bin/env python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetching employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        if employee_response.status_code != 200:
            print(f"Error: Failed to retrieve employee data. Status code: {employee_response.status_code}")
            return

        # Fetch TODO list for employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        if todos_response.status_code != 200:
            print(f"Error: Failed to retrieve TODO list data. Status code: {todos_response.status_code}")
            return

        # Filtering done tasks and gather details
        completed_tasks = []
        for task in todos_data:
            if task['completed']:
                completed_tasks.append(task['title'])

        # Displaying the employee progress
        total_tasks = len(todos_data)
        completed_count = len(completed_tasks)
        print(f"Employee {employee_data['name']} is done with tasks({completed_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments. Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)


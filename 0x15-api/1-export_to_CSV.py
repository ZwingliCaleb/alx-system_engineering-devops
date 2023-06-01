#!/usr/bin/python3

import requests
import sys
import json

def export_employee_tasks_to_json(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        if employee_response.status_code != 200:
            print(f"Error: Failed to retrieve employee data. Status code: {employee_response.status_code}")
            return

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        if todos_response.status_code != 200:
            print(f"Error: Failed to retrieve TODO list data. Status code: {todos_response.status_code}")
            return

        # Filter and format employee tasks
        employee_tasks = []
        for task in todos_data:
            employee_tasks.append({
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_data['username']
            })

        # Create JSON data
        json_data = { str(employee_id): employee_tasks }

        # Export to JSON file
        file_name = f"{employee_id}.json"
        with open(file_name, 'w') as file:
            json.dump(json_data, file)

        print(f"Tasks exported to {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments. Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        export_employee_tasks_to_json(employee_id)


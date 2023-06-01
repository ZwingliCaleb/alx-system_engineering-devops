#!/usr/bin/python3

'''
    Gathers data from an API and exports it in CSV format.
'''

import csv
import requests
from sys import argv

def exportToCSV(user_id):
    '''
        Gets data from an API and exports it to CSV.
    '''
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    employee = None
    tasks = []

    for user in users:
        if user.get('id') == int(user_id):
            employee = user.get('name')
            break

    if employee is None:
        print(f"No employee found with ID {user_id}")
        return

    for todo in todos:
        if todo.get('userId') == int(user_id):
            task_title = todo.get('title')
            task_status = str(todo.get('completed'))
            tasks.append([user_id, employee, task_status, task_title])

    if len(tasks) == 0:
        print(f"No tasks found for employee {employee}")
        return

    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

    print(f"Data exported to {filename} successfully!")

if __name__ == '__main__':
    if len(argv) < 2:
        print("Please provide a user ID as a command-line argument.")
    else:
        exportToCSV(argv[1])
        

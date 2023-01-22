#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def tasks_done(id):
    " displays an employee completed TODO tasks """
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(api_url)
    response_json = response.json()
    employee_name = response_json.get("name")

    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(api_url)
    todos_json = todos.json()
    no_tasks = len(todos_json)

    completed_task = 0
    tasks = ""

    for task in todos_json:
        if task.get("completed") is True:
            completed_task += 1
            tasks += "\t " + task.get("title") + "\n"

    print("Employee {} is done with ({}/{}):".format(employee_name,
                                                    completed_task,
                                                    no_tasks))
    print(tasks[:-1])


if __name__ == "__main__":
    tasks_done(sys.argv[1])

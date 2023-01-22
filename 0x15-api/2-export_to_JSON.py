#!/usr/bin/python3
""" exports employee todo tasks to a json file """
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id)).json()
    with open("{}.json".format(sys.argv[1]), "w") as arg_id:
        json.dump({user_id: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': users.get('username')
        } for task in todos]}, arg_id)

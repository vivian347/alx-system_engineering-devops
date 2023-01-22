#!/usr/bin/python3
""" extend your Python script to export data in the CSV format. """

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    response = requests.get(api_url).json()
    username = response.get("username")
    req = requests.get(
            'https://jsonplaceholder.typicode.com/users/' +
        (user_id) + '/todos')
    with open("{}.csv".format(user_id), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([user_id, username,
                            task.get("completed"), task.get("title")])

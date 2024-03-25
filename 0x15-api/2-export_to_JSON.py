#!/usr/bin/python3
"""
Scrript using REST API for a given employee ID
Returns information about his/her TODO list progress (In JSON format)
"""

import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    url_todos = "{url}/todos".format(url=url)
    url_users = "{url}/users/{id}".format(url=url, id=sys.argv[1])
    response_user = requests.get(url_users)
    response_todos = requests.get(url_todos, params={'userId': sys.argv[1]})
    response_todos_json = response_todos.json()
    response_user_json = response_user.json()
    tasks = []
    for todos in response_todos_json:
        tasks.append({"task": todos.get('title'),
                      "completed": todos.get('completed'),
                      "username": response_user_json.get('username')})
    json_dict = {sys.argv[1]: tasks}
    with open(sys.argv[1] + ".json", mode='w') as employee_file:
        json.dump(json_dict, employee_file)

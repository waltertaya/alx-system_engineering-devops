#!/usr/bin/python3
"""
Scrript using REST API for a given employee ID
Returns information about his/her TODO list progress (In JSON format)
"""

import json
import requests

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    for id in range(1, 11):
        url_todos = "{url}/todos".format(url=url)
        url_users = "{url}/users/{id}".format(url=url, id=id)
        response_user = requests.get(url_users)
        response_todos = requests.get(url_todos, params={'userId': id})
        response_todos_json = response_todos.json()
        response_user_json = response_user.json()
        tasks = []
        for todos in response_todos_json:
            tasks.append({"task": todos.get('title'),
                          "completed": todos.get('completed'),
                          "username": response_user_json.get('username')})
        json_dict = {id: tasks}
        with open("todo_all_employees.json", mode='a') as employee_file:
            json.dump(json_dict, employee_file)
            employee_file.write("\n")

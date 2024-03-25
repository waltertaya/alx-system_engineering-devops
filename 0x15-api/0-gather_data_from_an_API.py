#!/usr/bin/python3
"""
Scrript using REST API for a given employee ID
Returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    employee_id  = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/{employee_id}".format(employee_id=employee_id)
    url_users = "https://jsonplaceholder.typicode.com/users/{employee_id}".format(employee_id=employee_id)
    response_user = requests.get(url_users)
    response = requests.get(url)
    response_json = response.json()
    response_user_json = response_user.json()
    print(response_json)
    print(response_user_json)
    #{'userId': 4, 'id': 67, 'title': 'quia voluptatibus voluptatem quos similique maiores repellat', 'completed': False}

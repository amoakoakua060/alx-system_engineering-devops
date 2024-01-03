#!/usr/bin/python3

"""
script to export data in the JSON format
"""


import json
import requests
import sys


if __name__ == "__main__":
    userUrl = f"https://jsonplaceholder.typicode.com/users"
    todosUrl = f"https://jsonplaceholder.typicode.com/todos"
    filename = f"todo_all_employees.json"

    res = requests.get(userUrl)
    users = res.json()
    res = requests.get(todosUrl)
    todos = res.json()

    final_dict = {}
    with open(filename, "w") as f:
        for user in users:
            id = user["id"]
            final_dict[id] = []
            userTodos = list(filter(lambda t: t["userId"] == id, todos))
            for t in userTodos:
                new_dict = {
                    "username": user["username"],
                    "task": t["title"],
                    "completed": t["completed"]
                }
                final_dict[id].append(new_dict)
        json.dump(final_dict, f)

#!/usr/bin/python3

"""
script to export data in the JSON format
"""


import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    userUrl = f"https://jsonplaceholder.typicode.com/users?id={id}"
    todosUrl = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    filename = f"{id}.json"

    res = requests.get(userUrl)
    user = res.json()[0]
    res = requests.get(todosUrl)
    todos = res.json()

    final_dict = {}
    final_dict[id] = []
    with open(filename, "w") as f:
        for t in todos:
            new_dict = {
                "task": t["title"],
                "completed": t["completed"],
                "username": user["username"],
            }
            final_dict[id].append(new_dict)
        json.dump(final_dict, f)

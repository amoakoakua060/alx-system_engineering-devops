#!/usr/bin/python3

"""
script to export data in the CSV format
"""


import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    userUrl = f"https://jsonplaceholder.typicode.com/users?id={id}"
    todosUrl = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    filename = f"{id}.csv"

    res = requests.get(userUrl)
    user = res.json()[0]
    res = requests.get(todosUrl)
    todos = res.json()

    with open(filename, "w") as f:
        for t in todos:
            f.write(f""""{t['userId']}","{user['username']}",\
"{t['completed']}","{t['title']}"\n""")

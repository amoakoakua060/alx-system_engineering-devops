#!/usr/bin/python3

"""
for a given employee ID, script returns information about his/her
TODO list progress
"""

if __name__ == "__main__":
    import requests
    import sys

    id = sys.argv[1]
    userUrl = f"https://jsonplaceholder.typicode.com/users?id={id}"
    todosUrl = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    res = requests.get(userUrl)
    user = res.json()[0]
    res = requests.get(todosUrl)
    todos = res.json()

    completed = len(list(filter(lambda x: x["completed"] is True, todos)))
    print(f"Employee {user['name']} is done with tasks({completed}/20):")
    for t in todos:
        if t["completed"]:
            print(f"\t {t['title']}")

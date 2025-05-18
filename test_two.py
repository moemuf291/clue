import json
import os


if os.path.exists("new.json"):
    pass
else:
    with open("new.json", "x") as file:
        json.dump({}, file)


with open("new.json", "r") as file:
    data = json.load(file)

first_name = input("first name: ")
last_name = input("last name: ")

data[first_name] = last_name


with open("new.json", "w") as file:
    json.dump(data, file, indent=4)


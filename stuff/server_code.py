import os
import json
import requests
from cryptography.fernet import Fernet


key = Fernet.generate_key().decode()

def check_file():
    if not os.path.exists("server_keys.json"):
        with open("server_keys.json", "x") as file:
            json.dump({}, file)
    else:
        pass


def save_phrase():
    try:
        url = "https://randomuser.me/api/"

        response = requests.get(url)

        if response.status_code == 200:
            print("connection success")
            req_data = response.json()

            open_data = req_data["results"][0]["name"]["first"]

            try:
                with open("server_keys.json", "r") as file:
                    save_data = json.load(file)

                    if open_data not in save_data:
                        save_data[open_data] = key

                        with open("server_keys.json", "w") as file:
                            json.dump(save_data, file, indent=4)
                        print("data was saved to file")

                    else:
                        print("repeating error")
            except (FileNotFoundError, Exception) as e:
                print(e)
    except (ConnectionError, Exception) as f:
        print(f)


def main():
    check_file()
    save_phrase()



main()
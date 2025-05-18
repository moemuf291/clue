import os
import json
import random
import string

def check_file():
    if os.path.exists("passwords.json"):
        pass
    else:
        try:
            with open("passwords.json", "x") as file:
                json.dump({}, file)

        except (FileExistsError) as e:
            print(e)


def gen_pass():
    length = random.randint(10,20)
    pass_word = "".join(random.sample(string.ascii_letters, k=length))

    return pass_word


def login(user_input, pass_word):
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

            data[user_input] = pass_word

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
                print(f"{user_input} was saved to passwords.json")
    except (FileNotFoundError, Exception) as e:
        print(e)


def get_login(login_info):
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

            user_login = data[login_info]

            print(user_login)
    except (FileNotFoundError, Exception) as e:
        print(e)




if __name__ == "__main__":
    check_file()
    pass_word = gen_pass()

    ask_user = input("how may I help you? ")

    if ask_user == "input pass":
        user_input = input("what is this password for: ")
        login(user_input, pass_word)
    
    elif ask_user == "get pass":
        login_info = input("what password are you looking for: ")
        get_login(login_info)

    else:
        print("error")
        pass



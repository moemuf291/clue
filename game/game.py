import os
import random
import requests
import json


def get_link():
    try:
        if not os.path.exists("link.json"):
            print("file could not be found")
        else:
            with open("link.json", "r") as file:
                data = json.load(file)

                url = data["api_link"]

                response = requests.get(url)

                if response.status_code == 200:
                    
                    req = response.json()

                    req_data = req["results"][0]
                    question = req_data["question"]

                    print(question)
                else:
                    print("Connection Error")
    except (FileNotFoundError) as e:
        print(e)


def create_file():
    if os.path.exists("correct.json"):
        pass
    else:
        with open("correct.json", "x") as file:
            json.dump({}, file)


def save_answer():
    try:
        with open("link.json", "r") as file:
            data = json.load(file)

            url = data["api_link"]

            response = requests.get(url)

            if response.status_code == 200:
                
                save_dat = response.json()

                save_open = save_dat["results"][0]
                save_question = save_open["question"]
                save_answer = save_open["correct_answer"]

                print(save_question)
                with open("correct.json", "r") as file:
                    saved_data = json.load(file)

                    saved_data = {"answer": saved_answer}

                    with open("correct.json", "w") as file:
                        json.dump(saved_data, file, indent=4)
    except (FileNotFoundError) as e:
        print(e)

            


def check_answer(user_input):
    try:
        with open("correct.json", "r") as file:
            data = json.load(file)

            get_answer = data["answer"]

            my_list_comp = ["good job", "great job", "your smart", "impressive"]
            my_list_dis = ["incorrect", "try again", "better luck next time"]

            if user_input.lower() == get_answer.lower():
                choice_comp = random.choice(my_list_comp)
                print(choice_comp)
            else:
                 choice_dis = random.choice(my_list_dis)
                 print(f"{choice_dis}, the correct answer is {get_answer}")
    except (FileNotFoundError) as e:
        print(e)



if __name__ == "__main__":
    get_link()
    create_file()
    save_answer()
    user_input = input("Answer with (true) or (false): ")
    check_answer(user_input)
            

        
                                            




                
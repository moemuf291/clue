import random
import string
import json
import os


def file_name():
    length = random.randint(1,20)
    key_name = "".join(random.sample(string.ascii_letters, k=length))
    return key_name


def create_file():
    if os.path.exists("database.json"):
        
        pass
    else:
        try:
            with open("database.json",'x') as file:
                json.dump({}, file) #creating a empty json key and variable slot in this file 
        except (FileExistsError) as e:
            print(e)



def save_to_file(key_phrase, user_input):
    

    try:
        with open("database.json", "r") as file:
            data = json.load(file)
    except (FileExistsError) as e:
        print(e)



    data[user_input] = key_phrase 

   
    try:
        with open("database.json", "w") as file:
            json.dump(data, file, indent=4)
            print(f"{user_input} saved as {key_phrase}")
    except (FileExistsError) as e:
        print(e)


def create_new(key_phrase):
    
    try:
        with open(key_phrase, "w") as file:
            file.write("hello")
    except (FileExistsError) as e:
        print(e) 



        



if __name__ == "__main__":
    key_phrase = file_name()
    create_file()

    user_input = input("Name file: ")

    save_to_file(key_phrase, user_input)
    create_new(key_phrase)

    







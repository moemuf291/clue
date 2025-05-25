import os
import json
from cryptography.fernet import Fernet

def get_value(user_input):
    try:
        with open("test_keys.json", "r") as file:
            data = json.load(file)

            value = data[user_input]
            return value
    except (Exception) as e:
        print(e)



def decrypt(encode_value, user_path, user_input):
    try:
        with open(user_path, "rb") as file:
            encrypted = file.read()

            Cipher = Fernet(encode_value.encode()) # placing it here means you dont need to do ".encode() every time you use it"
            decrypted = Cipher.decrypt(encrypted)

            decrypted_name = user_input + ".decrypted"

            with open(decrypted_name, "wb") as file:
                file.write(decrypted)
                os.write(user_path)
    except (Exception) as e:
        print(e)




if __name__ == "__main__":
    user_input = input("look at the file name and enter the name of that file before the .encrypted: ")
    encode_value = get_value(user_input)
    user_path = input("enter the path to the files: ")
    decrypt(encode_value, user_path, user_path)


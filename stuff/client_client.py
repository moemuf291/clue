import os
import json
import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(("localhost", 1234))

name = input("name: ")
key = input("key: ")
data_send = {"name": name, "key": key}

if not os.path.exists("to_server.json"):
    with open("to_server.json", "x") as file:
        json.dump({}, file)
else:
    pass

with open("to_server.json", "w") as file:
    json.dump(data_send, file, indent=4)


with open("to_server.json", "r") as file:
    data_from_file = json.load(file)

    

message = json.dumps(data_from_file).encode() # use json.dumps when you want to send stuff over a network and use json.dump() when you want to write anything to a json file
client_socket.sendall(message)




data = client_socket.recv(1024)
print(f"{data.decode()}")

client_socket.close()


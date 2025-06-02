import socket
import os
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(("localhost", 1234))

try:
    with open("pass_store.json", "r") as file:
        data = json.load(file)

        pull_data = data["hulu"]

        client_socket.sendall(pull_data.encode())
except (FileNotFoundError, Exception) as e:
    print(e)



data = client_socket.recv(1024)
print(f"{data.decode()}")

client_socket.close()